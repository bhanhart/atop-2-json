'''
Created on May 25, 2015

@author: hsd
'''
import unittest

from atoprecord import AtopRecord

class AtopRecordTests(unittest.TestCase):

    def test_success_record_parse(self):
        atop_mem_line = "MEM tswp01 1431564003 2015/05/14 02:40:03 600 4096 1511773 987914 323548 136299 25938 44"
        atop_cpu_line = "CPU tswp01 1431640203 2015/05/14 23:50:03 600 100 8 60140 121249 0 298071 423 7 61 0 0 12768 533"

        record = AtopRecord(99)
        record.parse_line(atop_mem_line)
        record.parse_line(atop_cpu_line)
        json_output = record.to_json()
        print("JSON output: " + str(json_output))
        pass

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_success_record_parse']
    unittest.main()
