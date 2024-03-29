#!/usr/bin/env python
# Copyright 2010 Google Inc. All Rights Reserved.

"""Unittest for grr frontend server."""




from grr.lib import communicator
from grr.lib import config_lib
from grr.lib import data_store
from grr.lib import flags
from grr.lib import flow
from grr.lib import flow_runner
from grr.lib import rdfvalue
from grr.lib import scheduler
from grr.lib import test_lib
from grr.lib import utils


class SendingTestFlow(flow.GRRFlow):
  """Tests that sent messages are correctly collected."""

  @flow.StateHandler(next_state="Incoming")
  def Start(self):
    for i in range(10):
      self.CallClient("Test",
                      rdfvalue.DataBlob(string="test%s" % i),
                      data=str(i),
                      next_state="Incoming")


class GRRFEServerTest(test_lib.FlowTestsBaseclass):
  """Tests the GRRFEServer."""
  string = "Test String"

  def setUp(self):
    """Setup the server."""
    super(GRRFEServerTest, self).setUp()

    # Whitelist test flow.
    config_lib.CONFIG.Set("Frontend.well_known_flows", [utils.SmartStr(
        test_lib.WellKnownSessionTest.well_known_session_id)])

    # For tests, small pools are ok.
    config_lib.CONFIG.Set("Threadpool.size", 10)

    prefix = "pool-%s" % self._testMethodName
    self.server = flow.FrontEndServer(
        certificate=config_lib.CONFIG["Frontend.certificate"],
        private_key=config_lib.CONFIG["PrivateKeys.server_key"],
        threadpool_prefix=prefix)

  def CheckMessages(self, left, right):
    """Compares two lists of messages for equality.

    Args:
      left: A list of GrrMessage
      right: A list of (task, GrrMessage)

    Returns:
      True if they are the same.
    """
    if len(right) != len(left):
      return False

    for i in range(len(right)):
      if left[i] != right[i][1]:
        return False

    return True

  def testReceiveMessages(self):
    """Test Receiving messages with no status."""
    flow_obj = self.FlowSetup("FlowOrderTest")

    session_id = flow_obj.session_id
    messages = [rdfvalue.GrrMessage(request_id=1,
                                    response_id=i,
                                    session_id=session_id,
                                    args=str(i))
                for i in range(1, 10)]

    self.server.ReceiveMessages(messages)

    # Make sure the task is still on the client queue
    tasks_on_client_queue = scheduler.SCHEDULER.Query(self.client_id, 100,
                                                      token=self.token)
    self.assertEqual(len(tasks_on_client_queue), 1)

    # Check that messages were stored correctly
    for message in messages:
      stored_message, _ = data_store.DB.Resolve(
          flow_runner.FlowManager.FLOW_STATE_TEMPLATE % session_id,
          flow_runner.FlowManager.FLOW_RESPONSE_TEMPLATE % (
              1, message.response_id),
          decoder=rdfvalue.GrrMessage, token=self.token)

      self.assertProtoEqual(stored_message, message)

    return messages

  def testReceiveMessagesWithStatus(self):
    """Receiving a sequence of messages with a status."""
    messages = self.testReceiveMessages()

    # Now add the status message
    status = rdfvalue.GrrStatus(status=rdfvalue.GrrStatus.ReturnedStatus.OK)
    status_messages = [rdfvalue.GrrMessage(
        request_id=1, response_id=len(messages)+1,
        session_id=messages[0].session_id, payload=status,
        type=rdfvalue.GrrMessage.Type.STATUS)]

    self.server.ReceiveMessages(status_messages)

  def testWellKnownFlows(self):
    """Make sure that well known flows can run on the front end."""
    test_lib.WellKnownSessionTest.messages = []
    session_id = test_lib.WellKnownSessionTest.well_known_session_id

    messages = [rdfvalue.GrrMessage(request_id=0,
                                    response_id=0,
                                    session_id=session_id,
                                    args=str(i))
                for i in range(1, 10)]

    self.server.ReceiveMessages(messages)

    # Wait for async actions to complete
    self.server.thread_pool.Join()

    test_lib.WellKnownSessionTest.messages.sort()

    # Well known flows are now directly processed on the front end
    self.assertEqual(test_lib.WellKnownSessionTest.messages,
                     list(range(1, 10)))

    # There should be nothing in the client_queue
    self.assertEqual([], data_store.DB.ResolveRegex(self.client_id, "task:.*",
                                                    token=self.token))

  def testWellKnownFlowsRemote(self):
    """Make sure that flows that do not exist on the front end get scheduled."""
    test_lib.WellKnownSessionTest.messages = []
    session_id = test_lib.WellKnownSessionTest.well_known_session_id

    messages = [rdfvalue.GrrMessage(request_id=0,
                                    response_id=0,
                                    session_id=session_id,
                                    args=str(i))
                for i in range(1, 10)]

    # Delete the local well known flow cache is empty.
    self.server.well_known_flows = {}
    self.server.ReceiveMessages(messages)

    # Wait for async actions to complete
    self.server.thread_pool.Join()

    # None get processed now
    self.assertEqual(test_lib.WellKnownSessionTest.messages, [])

    # There should be nothing in the client_queue
    self.assertEqual([], data_store.DB.ResolveRegex(self.client_id, "task:.*",
                                                    token=self.token))

    # The well known flow messages should be waiting in the flow state now:
    queued_messages = []
    for predicate, _, _ in data_store.DB.ResolveRegex(
        "%s/state" % session_id, "flow:.*", token=self.token):
      queued_messages.append(predicate)

    self.assertEqual(len(queued_messages), 9)

  def testDrainUpdateSessionRequestStates(self):
    """Draining the flow requests and preparing messages."""
    # We set this so that task scheduler ids dont trivially correlate
    # with request_ids:
    scheduler.SCHEDULER.ts_id = 15

    # This flow sends 10 messages on Start()
    flow_obj = self.FlowSetup("SendingTestFlow")
    session_id = flow_obj.session_id

    # There should be 10 messages in the client's task queue
    tasks = scheduler.SCHEDULER.Query(self.client_id, 100,
                                      token=self.token)
    self.assertEqual(len(tasks), 10)

    # Check that the response state objects have the correct ts_id set
    # in the client_queue:
    for task in tasks:
      request_id = task.request_id

      # Retrieve the request state for this request_id
      request_state, _ = data_store.DB.Resolve(
          flow_runner.FlowManager.FLOW_STATE_TEMPLATE % session_id,
          flow_runner.FlowManager.FLOW_REQUEST_TEMPLATE % request_id,
          decoder=rdfvalue.RequestState, token=self.token)

      # Check that ts_id for the client message is correctly set in
      # request_state
      self.assertEqual(request_state.ts_id, task.task_id)

    # Now ask the server to drain the outbound messages into the
    # message list.
    response = rdfvalue.MessageList()

    self.server.DrainTaskSchedulerQueueForClient(
        self.client_id, 5, response)

    # Check that we received only as many messages as we asked for
    self.assertEqual(len(response.job), 5)

    for i in range(4):
      self.assertEqual(response.job[i].session_id, session_id)
      self.assertEqual(response.job[i].name, "Test")

  def testUpdateAndCheckIfShouldThrottle(self):
    self.server.SetThrottleBundlesRatio(1.0)

    # Let's assume that requests are flowing in every 10 seconds
    self.server.UpdateAndCheckIfShouldThrottle(0)
    self.server.UpdateAndCheckIfShouldThrottle(10)
    self.server.UpdateAndCheckIfShouldThrottle(20)
    self.server.UpdateAndCheckIfShouldThrottle(30)
    self.server.UpdateAndCheckIfShouldThrottle(40)
    self.server.UpdateAndCheckIfShouldThrottle(50)
    self.server.UpdateAndCheckIfShouldThrottle(60)

    self.server.SetThrottleBundlesRatio(0.3)

    # Now: average interval between requests is 10 seconds
    # According to throttling logic, requests will only be allowed if
    # the interval between them is 10 / 0.3 = 33.3 seconds
    result = self.server.UpdateAndCheckIfShouldThrottle(70)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(80)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(90)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(100)
    self.assertEquals(result, False)

    result = self.server.UpdateAndCheckIfShouldThrottle(110)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(120)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(130)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(140)
    self.assertEquals(result, False)

    # Now we throttle everything
    self.server.SetThrottleBundlesRatio(0)

    result = self.server.UpdateAndCheckIfShouldThrottle(141)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(142)
    self.assertEquals(result, True)

    result = self.server.UpdateAndCheckIfShouldThrottle(143)
    self.assertEquals(result, True)

    # Now we turn throttling off
    self.server.SetThrottleBundlesRatio(None)

    result = self.server.UpdateAndCheckIfShouldThrottle(144)
    self.assertEquals(result, False)

    result = self.server.UpdateAndCheckIfShouldThrottle(145)
    self.assertEquals(result, False)

    result = self.server.UpdateAndCheckIfShouldThrottle(146)
    self.assertEquals(result, False)

  def testHandleMessageBundle(self):
    """Check that HandleMessageBundles() requeues messages if it failed.

    This test makes sure that when messages are pending for a client, and which
    we have no certificate for, the messages are requeued when sending fails.
    """
    # Make a new fake client
    client_id = rdfvalue.ClientURN("C." + "2" * 16)

    class MockCommunicator(object):
      """A fake that simulates an unenrolled client."""

      def DecodeMessages(self, *unused_args):
        """For simplicity client sends an empty request."""
        return ([], client_id, 100)

      def EncodeMessages(self, *unused_args, **unused_kw):
        """Raise because the server has no certificates for this client."""
        raise communicator.UnknownClientCert()

    # Install the mock.
    self.server._communicator = MockCommunicator()

    # First request, the server will raise UnknownClientCert.
    request_comms = rdfvalue.ClientCommunication()
    self.assertRaises(communicator.UnknownClientCert,
                      self.server.HandleMessageBundles, request_comms, 2)

    # We can still schedule a flow for it
    flow.GRRFlow.StartFlow(client_id, "SendingFlow", message_count=1,
                           token=self.token)

    tasks = scheduler.SCHEDULER.Query(client_id, limit=100,
                                      token=self.token)

    self.assertRaises(communicator.UnknownClientCert,
                      self.server.HandleMessageBundles, request_comms, 2)

    new_tasks = scheduler.SCHEDULER.Query(client_id, limit=100,
                                          token=self.token)

    # The different in eta times reflect the lease that the server took on the
    # client messages.
    lease_time = (new_tasks[0].eta - tasks[0].eta)/1e6

    # This lease time must be small, as the HandleMessageBundles() call failed,
    # the pending client messages must be put back on the queue.
    self.assert_(lease_time < 1)

    # Since the server tried to send it, the ttl must be decremented
    self.assertEqual(tasks[0].task_ttl - new_tasks[0].task_ttl, 1)


def main(args):
  test_lib.main(args)


if __name__ == "__main__":
  flags.StartMain(main)
