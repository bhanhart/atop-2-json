'''
Created on May 21, 2015

@author: hsd
'''

from resourceline import ResourceLine

from headergrammar import HeaderGrammar
from cpulinegrammar import CpuLineGrammar

class CpuLine(ResourceLine):
    '''
        Parse all fields from an atop CPU line
    '''
    CPU_USAGE_PERCENTAGE = "cpu_usage_percentage"
    CPU_SYSTEM_PERCENTAGE = "cpu_system_percentage"
    CPU_USER_PERCENTAGE = "cpu_user_percentage"

    _grammar = CpuLineGrammar().get_grammar()

    def __init__(self, line):
        '''
        Constructor
        '''
        super(CpuLine, self).__init__()

        parse_results = self._grammar.parseString(line)
        self._store_parse_results(parse_results)

        self._log_interval = int(
            parse_results.get(HeaderGrammar.LOG_INTERVAL))
        self._tics_per_second = int(
            parse_results.get(CpuLineGrammar.CPU_TICKS_PER_SECOND))
        self._num_processors = int(
            parse_results.get(CpuLineGrammar.CPU_NUM_PROCESSORS))
        self._idle_ticks = int(
            parse_results.get(CpuLineGrammar.CPU_IDLE_TICKS))
        self._system_ticks = int(
            parse_results.get(CpuLineGrammar.CPU_SYSTEM_TICKS))
        self._user_ticks = int(
            parse_results.get(CpuLineGrammar.CPU_USER_TICKS))

    def addFields(self, fields):
        fields[self.CPU_USAGE_PERCENTAGE] = self._get_usage_percentage()
        fields[self.CPU_SYSTEM_PERCENTAGE] = self._get_system_percentage()
        fields[self.CPU_USER_PERCENTAGE] = self._get_user_percentage()

    def _get_usage_percentage(self):
        idle_cpu_percentage = self._ticks_to_percentage(self._idle_ticks)
        return 100 - int(idle_cpu_percentage)

    def _get_system_percentage(self):
        system_cpu_percentage = self._ticks_to_percentage(self._system_ticks)
        return int(system_cpu_percentage)

    def _get_user_percentage(self):
        user_cpu_percentage = self._ticks_to_percentage(self._user_ticks)
        return int(user_cpu_percentage)

    def _ticks_to_percentage(self, num_ticks):
        ticks_available = \
            self._tics_per_second * self._log_interval * self._num_processors
        return (num_ticks / ticks_available) * 100
