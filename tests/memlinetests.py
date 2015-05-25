'''
Created on May 25, 2015

@author: hsd
'''
import unittest

from memline import CpuLine

class MemLineTests(unittest.TestCase):

    def test_success_mem_line_parse(self):
        atop_mem_line = "MEM tswp01 1431564003 2015/05/14 02:40:03 600 4096 1511773 987914 323548 136299 25938 44"
        mem_line = CpuLine(atop_mem_line)
        fields = {}
        mem_line.addFields(fields)
        self.assertEqual(
            6192222,
            fields.get(CpuLine.MEM_TOTAL_KB),
            "Failed to retrieve correct total memory in kB")
        self.assertEqual(
            262193,
            fields.get(CpuLine.MEM_USED_KB),
            "Failed to retrieve correct used memory in kB")
        self.assertEqual(
            4,
            fields.get(CpuLine.MEM_USED_PERCENTAGE),
            "Failed to retrieve correct memory usage percentage")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_success_mem_line']
    unittest.main()
