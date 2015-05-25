"""
    Representation of an atop sample.
"""
import logging
import json

from memline import MemLine
from cpuline import CpuLine
from iso8601timestamp import Iso8601Timestamp

class AtopSample(object):
    """
        An atop sample taken on a host at a particular time.
    """

    def __init__(self, sample_no, logger=None):
        self._logger = logger or logging.getLogger(__name__)
        self.sample_no = sample_no
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
            self._finalise_sample()
        fields = {}
        fields["@version"] = 1
        fields["@timestamp"] = Iso8601Timestamp(self.timestamp).to_iso8601()
        fields["host"] = self.hostname
        for line in self.lines:
            line.addFields(fields)

        self._logger.debug("Atop sample " + str(self.sample_no) +
            ": host=" + fields["host"] + ", timestamp=" + fields["@timestamp"])

        return json.dumps(fields, sort_keys=True)

    def _finalise_sample(self):
        assert len(self.lines) > 0
        first_line = self.lines[0]
        if self.hostname == None:
            self.hostname = first_line.get_host_name()
        if self.timestamp == None:
            self.timestamp = first_line.get_timestamp()

