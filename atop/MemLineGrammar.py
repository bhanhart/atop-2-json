import logging

import pyparsing as pp

from atop.LineHeaderGrammar import LineHeaderGrammar

class MemLineGrammar( object ):
    MEM_PAGE_SIZE = "mem_page_size"
    MEM_TOTAL = "mem_total"
    MEM_FREE = "mem_free"
    MEM_PAGE_CACHE = "mem_page_cache"
    MEM_BUFFER_CACHE = "mem_buffer_cache"
    MEM_SLAB = "mem_slab"
    MEM_NUM_DIRTY_PAGES = "mem_num_dirty_pages"

    HeaderGrammar = LineHeaderGrammar().getGrammar()

    def __init__( self, logger=None ):
        self.logger = logger or logging.getLogger( __name__ )

        category = pp.Literal( "MEM" ).suppress();
        pageSize = pp.Word( pp.nums )
        totalMem = pp.Word( pp.nums )
        freeMem = pp.Word( pp.nums )
        pageCache = pp.Word( pp.nums )
        bufferCache = pp.Word( pp.nums )
        slabMem = pp.Word( pp.nums )
        numDirtyPages = pp.Word( pp.nums )

        grammar = category
        grammar += self.HeaderGrammar
        grammar += pageSize( self.MEM_PAGE_SIZE )
        grammar += totalMem( self.MEM_TOTAL )
        grammar += freeMem( self.MEM_FREE )
        grammar += pageCache( self.MEM_PAGE_CACHE )
        grammar += bufferCache( self.MEM_BUFFER_CACHE )
        grammar += slabMem( self.MEM_SLAB )
        grammar += numDirtyPages( self.MEM_NUM_DIRTY_PAGES )

        self.myGrammar = grammar

    def getGrammar( self ):
        return self.myGrammar
