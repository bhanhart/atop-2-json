'''
Created on May 25, 2015

@author: hsd
'''

from resourceline import ResourceLine
from memlinegrammar import MemLineGrammar

class MemLine(ResourceLine):

    MEM_TOTAL_KB = "mem_total_kb"
    MEM_USED_KB = "mem_used_kb"
    MEM_USED_PERCENTAGE = "mem_used_percentage"

    _grammar = MemLineGrammar().get_grammar()

    def __init__(self, line):
        super(MemLine, self).__init__()

        self._total_kb = None
        self._used_kb = None
        self._used_percentage = None

        parse_results = self._grammar.parseString(line)
        self._store_parse_results(parse_results)

        page_size = int(parse_results.get(MemLineGrammar.MEM_PAGE_SIZE))
        total = int(parse_results.get(MemLineGrammar.MEM_TOTAL))

        self._total_kb = self._calculate_total_kb(total, page_size)
        self._used_kb = self._calculate_used_kb(parse_results, total, page_size)
        self._used_percentage = self._calcuate_used_percentage(parse_results)

    def addFields(self, fields):
        fields[self.MEM_TOTAL_KB] = self._total_kb
        fields[self.MEM_USED_KB] = self._used_kb
        fields[self.MEM_USED_PERCENTAGE] = self._used_percentage

    def _calculate_total_kb(self, total, page_size):
        return int((total * page_size) / 1000)

    def _calculate_used_kb(self, parse_results, total, page_size):
        free = parse_results.get(MemLineGrammar.MEM_FREE)
        page_cache = parse_results.get(MemLineGrammar.MEM_PAGE_CACHE)
        buffer_cache = parse_results.get(MemLineGrammar.MEM_BUFFER_CACHE)
        available = int(free) + int(page_cache) + int(buffer_cache)
        return int(((total - available) * page_size) / 1000)

    def _calcuate_used_percentage(self, parse_results):
        return int((self._used_kb / self._total_kb) * 100)
