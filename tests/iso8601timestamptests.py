'''
Created on May 21, 2015

@author: hsd
'''
import unittest

import time

from iso8601timestamp import Iso8601Timestamp

class Iso8601TimestampTests(unittest.TestCase):
    def test_succesful_construction(self):
        test_time_input = (2015, 5, 24, 12, 10, 20, 0, 1, -1)
        test_time_output = "2015-05-24T12:10:20Z"
        epoch = time.mktime(test_time_input)
        timestamp = Iso8601Timestamp(int(epoch))
        self.assertEqual(
            timestamp.to_iso8601(),
            test_time_output,
            "ISO6801 time conversion failure")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testCpuLineGrammar']
    unittest.main()
