'''
Created on May 24, 2015

@author: hsd
'''
import unittest

from memlinegrammar import MemLineGrammar

class Test(unittest.TestCase):


    def test_success_mem_grammar(self):
        atop_mem_line = "MEM tswp01 1431564003 2015/05/14 02:40:03 600 4096 1511773 987914 323548 136299 25938 44"

        grammar = MemLineGrammar().get_grammar()
        parse_results = grammar.parseString(atop_mem_line)

        self.assertEqual(
            "4096",
            parse_results.get(MemLineGrammar.MEM_PAGE_SIZE),
            "Failed to parse memory page size")
        self.assertEqual(
            "1511773",
            parse_results.get(MemLineGrammar.MEM_TOTAL),
            "Failed to parse physical memory size")
        self.assertEqual(
            "987914",
            parse_results.get(MemLineGrammar.MEM_FREE),
            "Failed to parse free memory size")
        self.assertEqual(
            "323548",
            parse_results.get(MemLineGrammar.MEM_PAGE_CACHE),
            "Failed to parse page cache size")
        self.assertEqual(
            "136299",
            parse_results.get(MemLineGrammar.MEM_BUFFER_CACHE),
            "Failed to parse buffer cache size")
        self.assertEqual(
            "25938",
            parse_results.get(MemLineGrammar.MEM_SLAB),
            "Failed to parse slab size")
        self.assertEqual(
            "44",
            parse_results.get(MemLineGrammar.MEM_NUM_DIRTY_PAGES),
            "Failed to parse number of dirty pages")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_mem_grammar_successful']
    unittest.main()
