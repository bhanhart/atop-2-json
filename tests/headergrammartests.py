'''
Created on May 24, 2015

@author: hsd
'''
import unittest

from headergrammar import HeaderGrammar

class HeaderGrammarTest(unittest.TestCase):

    def test_succes_header_grammar(self):
        atop_header_line = "tswp01 1431564603 2015/05/14 02:50:03 600"
        grammar = HeaderGrammar().get_grammar()
        parse_results = grammar.parseString(atop_header_line)
        self.assertEqual(
            "tswp01",
            parse_results.get(HeaderGrammar.HOSTNAME),
            "Hostname parsing failed")

        self.assertEqual(
            "1431564603",
            parse_results.get(HeaderGrammar.EPOCH),
            "Hostname parsing failed")

        self.assertEqual(
            "600",
            parse_results.get(HeaderGrammar.LOG_INTERVAL),
            "Hostname parsing failed")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
