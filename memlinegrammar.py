import logging

from pyparsing import Literal, Word, nums

import headergrammar

class MemLineGrammar(object):
    MEM_PAGE_SIZE = "mem_page_size"
    MEM_TOTAL = "mem_total"
    MEM_FREE = "mem_free"
    MEM_PAGE_CACHE = "mem_page_cache"
    MEM_BUFFER_CACHE = "mem_buffer_cache"
    MEM_SLAB = "mem_slab"
    MEM_NUM_DIRTY_PAGES = "mem_num_dirty_pages"

    _header_grammar = headergrammar.HeaderGrammar()

    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(__name__)

        category = Literal("MEM").suppress()
        pageSize = Word(nums)
        totalMem = Word(nums)
        freeMem = Word(nums)
        pageCache = Word(nums)
        bufferCache = Word(nums)
        slabMem = Word(nums)
        numDirtyPages = Word(nums)

        grammar = category
        grammar += self._header_grammar.get_grammar()
        grammar += pageSize(self.MEM_PAGE_SIZE)
        grammar += totalMem(self.MEM_TOTAL)
        grammar += freeMem(self.MEM_FREE)
        grammar += pageCache(self.MEM_PAGE_CACHE)
        grammar += bufferCache(self.MEM_BUFFER_CACHE)
        grammar += slabMem(self.MEM_SLAB)
        grammar += numDirtyPages(self.MEM_NUM_DIRTY_PAGES)

        self.cpu_line_grammar = grammar

    def get_grammar(self):
        return self.cpu_line_grammar
