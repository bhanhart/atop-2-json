"""
    Define the structure of an atop CPU line.
"""

import logging

from pyparsing import Literal, Word, nums

import headergrammar

CPU_TICKS_PER_SECOND = "cpu_ticks_per_second"
CPU_NUM_PROCESSORS = "cpu_num_processors"
CPU_SYSTEM_TICKS = "cpu_system_ticks"
CPU_USER_TICKS = "cpu_user_ticks"
CPU_IDLE_TICKS = "cpu_idle_ticks"
CPU_WAIT_TICKS = "cpu_wait_ticks"
CPU_IRQ_TICKS = "cpu_irq_ticks"
CPU_SOFTIRQ_TICKS = "cpu_softirq_ticks"
CPU_STEAL_TICKS = "cpu_steal_ticks"
CPU_GUEST_TICKS = "cpu_guest_ticks"

class CpuLineGrammar(object):
    """ Specification in pyparsing format of an atop CPU line """

    _header_grammar = headergrammar.HeaderGrammar()

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

        category = Literal("CPU").suppress()
        ticks_per_second = Word(nums)
        num_processors = Word(nums)
        cpu_system = Word(nums)
        cpu_user = Word(nums)
        cpu_nice = Word(nums).suppress()
        cpu_idle = Word(nums)
        cpu_wait = Word(nums)
        cpu_irq = Word(nums)
        cpu_softirq = Word(nums)
        cpu_steal = Word(nums)
        cpu_guest = Word(nums)

        grammar = category
        grammar += self._header_grammar.get_grammar()
        grammar += ticks_per_second(CPU_TICKS_PER_SECOND)
        grammar += num_processors(CPU_NUM_PROCESSORS)
        grammar += cpu_system(CPU_SYSTEM_TICKS)
        grammar += cpu_user(CPU_USER_TICKS)
        grammar += cpu_nice
        grammar += cpu_idle(CPU_IDLE_TICKS)
        grammar += cpu_wait(CPU_WAIT_TICKS)
        grammar += cpu_irq(CPU_IRQ_TICKS)
        grammar += cpu_softirq(CPU_SOFTIRQ_TICKS)
        grammar += cpu_steal(CPU_STEAL_TICKS)
        grammar += cpu_guest(CPU_GUEST_TICKS)

        self.cpu_line_grammar = grammar

    def get_grammar(self):
        """ Returns the layout of an atop CPU line """
        return self.cpu_line_grammar
