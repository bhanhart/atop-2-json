'''
Created on May 25, 2015

@author: hsd
'''
import unittest

from cpuline import CpuLine

class CpuLineTests(unittest.TestCase):

    def test_success_cpu_line_parse(self):
        atop_cpu_line = "CPU tswp01 1431640203 2015/05/14 23:50:03 600 100 8 60140 121249 0 298071 423 7 61 0 0 12768 533"
        cpu_line = CpuLine(atop_cpu_line)
        fields = {}
        cpu_line.addFields(fields)
        self.assertEqual(
            38,
            fields.get(CpuLine.CPU_USAGE_PERCENTAGE),
            "Failed to retrieve correct CPU usage percentage")
        self.assertEqual(
            12,
            fields.get(CpuLine.CPU_SYSTEM_PERCENTAGE),
            "Failed to retrieve correct CPU system mode usage percentage")
        self.assertEqual(
            25,
            fields.get(CpuLine.CPU_USER_PERCENTAGE),
            "Failed to retrieve correct CPU user mode usage percentage")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_success_cpu_line_parse']
    unittest.main()
