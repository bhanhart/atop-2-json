import logging

import pyparsing as pp

from atop.LineHeaderGrammar import LineHeaderGrammar

class CpuLineGrammar( object ):
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

    HeaderGrammar = LineHeaderGrammar().getGrammar()

    def __init__( self, logger=None ):
        self.logger = logger or logging.getLogger( __name__ )

        category = pp.Literal( "CPU" ).suppress();
        ticksPerSecond = pp.Word( pp.nums )
        numProcessors = pp.Word( pp.nums )
        cpuSystem = pp.Word( pp.nums )
        cpuUser = pp.Word( pp.nums )
        cpuNice = pp.Word( pp.nums ).suppress()
        cpuIdle = pp.Word( pp.nums )
        cpuWait = pp.Word( pp.nums )
        cpuIrq = pp.Word( pp.nums )
        cpuSoftIrq = pp.Word( pp.nums )
        cpuSteal = pp.Word( pp.nums )
        cpuGuest = pp.Word( pp.nums )

        grammar = category
        grammar += self.HeaderGrammar
        grammar += ticksPerSecond( self.CPU_TICKS_PER_SECOND )
        grammar += numProcessors( self.CPU_NUM_PROCESSORS )
        grammar += cpuSystem( self.CPU_SYSTEM_TICKS )
        grammar += cpuUser( self.CPU_USER_TICKS )
        grammar += cpuNice
        grammar += cpuIdle( self.CPU_IDLE_TICKS )
        grammar += cpuWait( self.CPU_WAIT_TICKS )
        grammar += cpuIrq( self.CPU_IRQ_TICKS )
        grammar += cpuSoftIrq( self.CPU_SOFTIRQ_TICKS )
        grammar += cpuSteal( self.CPU_STEAL_TICKS )
        grammar += cpuGuest( self.CPU_GUEST_TICKS )

        self.myGrammar = grammar

    def getGrammar( self ):
        return self.myGrammar
