'''
Created on May 21, 2015

@author: hsd
'''

import cpulinegrammar

from cpulinegrammar import CpuLineGrammar

class CpuLineParser(object):
    '''
        Parse all fields from an atop CPU line
    '''
    _cpu_grammar = CpuLineGrammar()

    def __init__(self, params):
        '''
        Constructor
        '''
        _ticks_per_second = None
        _num_processors = None
        _idle_ticks = None
        _system_ticks = None

    def parse(self, line):
        parse_results = self._cpu_grammar.parseString(line)

        self._tics_per_second = int(
            parse_results.get(cpulinegrammar.CPU_TICKS_PER_SECOND))
        self._num_processors = int(
            parse_results.get(cpulinegrammar.CPU_NUM_PROCESSORS))
        self._idle_ticks = int(
            parse_results.get(cpulinegrammar.CPU_IDLE_TICKS))
        self._system_ticks = int(
            parse_results.get(cpulinegrammar.CPU_SYSTEM_TICKS))

    def get_usage_percentage(self):
        return 100 - self._ticks_to_percentage(self._idle_ticks)

    def get_system_percentage(self):
        return self._ticks_to_percentage(self._system_ticks)

    def _ticks_to_percentage(self, num_ticks):
        return (num_ticks / self._tics_per_second) / self._num_processors
