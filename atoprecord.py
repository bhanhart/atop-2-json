import logging
import json

from headergrammar import HeaderGrammar
from memlinegrammar import MemLineGrammar
from cpulinegrammar import CpuLineGrammar

class AtopRecord(object):
    memlinegrammar = MemLineGrammar().get_grammar()
    cpulinegrammar = CpuLineGrammar().get_grammar()

    def __init__(self, recordNo, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.record_no = recordNo
        self.host = None
        self.timestamp = None
        self.fields = {}

    def __str__(self):
        return json.dumps(self.fields)

    def parseLine(self, line):
        if line.startswith("MEM"):
            self._parseMemLine(line)
        elif line.startswith("CPU"):
            self._parseCpuLine(line)

    def _parseMemLine(self, line):
        parse_results = self.memlinegrammar.parseString(line)

        memTotal = int(parse_results.get(MemLineGrammar.MEM_TOTAL))
        memFree = int(parse_results.get(MemLineGrammar.MEM_FREE))
        memUsedPct = ((memTotal - memFree) / memTotal) * 100

        if (self.host == None):
            self.host = parse_results.get(HeaderGrammar.HOSTNAME)
        if (self.timestamp == None):
            self.timestamp = int(parse_results.get(HeaderGrammar.EPOCH))

        self.fields["memUsedPercentage"] = memUsedPct

    def _parseCpuLine(self, line):
#        cpu_parser = cpulineparser()
#        cpu_parser.parse(line)

        parse_results = self.cpulinegrammar.parseString(line)

        if (self.host == None):
            self.host = parse_results.get(HeaderGrammar.HOSTNAME)
        if (self.timestamp == None):
            self.timestamp = int(parse_results.get(HeaderGrammar.EPOCH))

