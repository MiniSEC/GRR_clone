#!/usr/bin/env python
# Copyright 2012 Google Inc. All Rights Reserved.

"""Parser for OSX launchd jobs."""




import re


class OSXLaunchdJobDict(object):
  """Cleanup launchd jobs reported by the service management framework.

  Exclude some rubbish like logged requests that aren't real jobs (see
  launchctl man page).  Examples:

  Exclude 0x7f8759d30310.anonymous.launchd
  Exclude 0x7f8759d1d200.mach_init.crash_inspector
  Keep [0x0-0x21021].com.google.GoogleDrive

  We could probably just exclude anything starting with a memory address, but
  I'm being more specific here as a tradeoff between sensible results and places
  for malware to hide.
  """

  def __init__(self, launchdjobs):
    """Initialize.

    Args:
      launchdjobs: NSCFArray of NSCFDictionarys containing launchd job data from
                   the ServiceManagement framework.
    """
    self.launchdjobs = launchdjobs

    self.blacklist_regex = [
        re.compile(r'^0x[a-z0-9]+\.anonymous\..+$'),
        re.compile(r'^0x[a-z0-9]+\.mach_init\.(crash_inspector|Inspector)$'),
        ]

  def Parse(self):
    """Parse the list of jobs and yield the good ones."""
    for item in self.launchdjobs:
      if not self.FilterItem(item):
        yield item

  def FilterItem(self, launchditem):
    """Should this job be filtered.

    Args:
      launchditem: job NSCFDictionary
    Returns:
      True if the item should be filtered (dropped)
    """
    for regex in self.blacklist_regex:
      if regex.match(launchditem.get('Label', '')):
        return True
    return False
