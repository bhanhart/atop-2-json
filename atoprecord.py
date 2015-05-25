"""
    Representation of an atop sample.
"""
import logging
import json

from memline import MemLine
from cpuline import CpuLine
from iso8601timestamp import Iso8601Timestamp

class AtopRecord(object):
    """
        An atop sample taken on a host at a particular time.
    """

    def __init__(self, recordNo, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.record_no = recordNo
        self.hostname = None
        self.timestamp = None
        self.lines = []

    def parse_line(self, line):
        if line.startswith("MEM"):
            self.lines.append(MemLine(line))
        elif line.startswith("CPU"):
            self.lines.append(CpuLine(line))

    def to_json(self):
        if self.timestamp == None:
            self._finalise_record()
        fields = {}
        fields["@version"] = 1
        fields["@timestamp"] = Iso8601Timestamp(self.timestamp).to_iso8601()
        fields["host"] = self.hostname
        for line in self.lines:
            line.addFields(fields)

        return json.dumps(fields)

    def _finalise_record(self):
        assert len(self.lines) > 0
        first_record = self.lines[0]
        if self.hostname == None:
            self.hostname = first_record.get_host_name()
        if self.timestamp == None:
            self.timestamp = first_record.get_timestamp()

