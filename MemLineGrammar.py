import logging

from pyparsing import Literal, Word, nums

import LineHeaderGrammar

MEM_PAGE_SIZE = "mem_page_size"
MEM_TOTAL = "mem_total"
MEM_FREE = "mem_free"
MEM_PAGE_CACHE = "mem_page_cache"
MEM_BUFFER_CACHE = "mem_buffer_cache"
MEM_SLAB = "mem_slab"
MEM_NUM_DIRTY_PAGES = "mem_num_dirty_pages"

class MemLineGrammar(object):

    HeaderGrammar = LineHeaderGrammar.LineHeaderGrammar().getGrammar()

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

        category = Literal("MEM").suppress()
        pageSize = Word(nums)
        totalMem = Word(nums)
        freeMem = Word(nums)
        pageCache = Word(nums)
        bufferCache = Word(nums)
        slabMem = Word(nums)
        numDirtyPages = Word(nums)

        grammar = category
        grammar += self.HeaderGrammar
        grammar += pageSize(MEM_PAGE_SIZE)
        grammar += totalMem(MEM_TOTAL)
        grammar += freeMem(MEM_FREE)
        grammar += pageCache(MEM_PAGE_CACHE)
        grammar += bufferCache(MEM_BUFFER_CACHE)
        grammar += slabMem(MEM_SLAB)
        grammar += numDirtyPages(MEM_NUM_DIRTY_PAGES)

        self.myGrammar = grammar

    def getGrammar(self):
        return self.myGrammar
