#!/usr/bin/env python
# Copyright 2010 Google Inc. All Rights Reserved.
"""A special worker responsible for initial enrollment of clients."""



# pylint: disable=unused-import,g-bad-import-order
from grr.lib import server_plugins
# pylint: enable=g-bad-import-order

from grr.lib import access_control
from grr.lib import config_lib
from grr.lib import flags
from grr.lib import rdfvalue
from grr.lib import startup
from grr.lib import type_info
from grr.lib import worker

# Make sure we also load the enroller module
from grr.lib.flows.caenroll import ca_enroller
# pylint: enable=W0611


def main(unused_argv):
  """Main."""
  config_lib.CONFIG.AddContext(
      "Enroller Context",
      "Context applied when running within the enroller process")

  # Initialise everything.
  startup.Init()

  # Start an Enroler.
  token = access_control.ACLToken("GRREnroller", "Implied.")
  enroller = worker.GRREnroler(queue=worker.DEFAULT_ENROLLER_QUEUE,
                               run_cron=False, token=token)

  enroller.Run()


if __name__ == "__main__":
  flags.StartMain(main)
