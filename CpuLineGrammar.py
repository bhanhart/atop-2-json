import logging

import pyparsing as pp

import LineHeaderGrammar

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

    HeaderGrammar = LineHeaderGrammar.LineHeaderGrammar().getGrammar()

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

        category = pp.Literal("CPU").suppress()
        ticksPerSecond = pp.Word(pp.nums)
        numProcessors = pp.Word(pp.nums)
        cpuSystem = pp.Word(pp.nums)
        cpuUser = pp.Word(pp.nums)
        cpuNice = pp.Word(pp.nums).suppress()
        cpuIdle = pp.Word(pp.nums)
        cpuWait = pp.Word(pp.nums)
        cpuIrq = pp.Word(pp.nums)
        cpuSoftIrq = pp.Word(pp.nums)
        cpuSteal = pp.Word(pp.nums)
        cpuGuest = pp.Word(pp.nums)

        grammar = category
        grammar += self.HeaderGrammar
        grammar += ticksPerSecond(CPU_TICKS_PER_SECOND)
        grammar += numProcessors(CPU_NUM_PROCESSORS)
        grammar += cpuSystem(CPU_SYSTEM_TICKS)
        grammar += cpuUser(CPU_USER_TICKS)
        grammar += cpuNice
        grammar += cpuIdle(CPU_IDLE_TICKS)
        grammar += cpuWait(CPU_WAIT_TICKS)
        grammar += cpuIrq(CPU_IRQ_TICKS)
        grammar += cpuSoftIrq(CPU_SOFTIRQ_TICKS)
        grammar += cpuSteal(CPU_STEAL_TICKS)
        grammar += cpuGuest(CPU_GUEST_TICKS)

        self.myGrammar = grammar

    def getGrammar(self):
        return self.myGrammar
