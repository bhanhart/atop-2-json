"""
    Convert seconds since the epoch to ISO 8601 string format
"""

from datetime import datetime

class Iso8601Timestamp(object):
    """ Timestamp encapsulation """

    def __init__(self, epoch_seconds):
        """ Store seconds since the epoch in datetime object """
        self.timestamp = datetime.fromtimestamp(epoch_seconds)

    def to_iso8601(self):
        """ Return timestamp in ISO 8601 string format """
        return self.timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
