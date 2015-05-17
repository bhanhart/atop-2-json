import logging
import json

from atop.MemLineGrammar import MemLineGrammar
from atop.CpuLineGrammar import CpuLineGrammar
from atop.LineHeaderGrammar import LineHeaderGrammar

class AtopRecord( object ):
    MemLineGrammar = MemLineGrammar().getGrammar()
    CpuLineGrammar = CpuLineGrammar().getGrammar()

    def __init__( self, recordNo, logger=None ):
        self.logger = logger or logging.getLogger( __name__ )
        self.recordNo = recordNo
        self.fields = {}

    def __str__( self ):
        return json.dumps( self.fields )

    def parseLine( self, line ):
        if line.startswith( "MEM" ):
            self.__parseMemLine( line )
        elif line.startswith( "CPU" ):
            self.__parseCpuLine( line )

    def __parseMemLine( self, line ):
        parseResults = self.MemLineGrammar.parseString( line )

        memTotal = int( parseResults.get( MemLineGrammar.MEM_TOTAL ) )
        memFree = int( parseResults.get( MemLineGrammar.MEM_FREE ) )
        memUsedPct = ( ( memTotal - memFree ) / memTotal ) * 100

        self.fields["memUsedPercentage"] = memUsedPct

        year = parseResults.get( LineHeaderGrammar.YEAR )
        month = parseResults.get( LineHeaderGrammar.MONTH )
        day = parseResults.get( LineHeaderGrammar.DAY )
        hour = parseResults.get( LineHeaderGrammar.HOUR )
        minute = parseResults.get( LineHeaderGrammar.MINUTE )
        second = parseResults.get( LineHeaderGrammar.SECOND )
        iso8601 = year
        iso8601 += "-"
        iso8601 += month
        iso8601 += "-"
        iso8601 += day
        iso8601 += "T"
        iso8601 += hour
        iso8601 += ":"
        iso8601 += minute
        iso8601 += ":"
        iso8601 += second
        iso8601 += "Z"
        self.fields["@timestamp"] = iso8601
        self.fields["@version"] = 1

    def __parseCpuLine( self, line ):
        parseResults = self.CpuLineGrammar.parseString( line )

        ticksPerSecond = int( parseResults.get( CpuLineGrammar.CPU_TICKS_PER_SECOND ) )
        numProcessors = int( parseResults.get( CpuLineGrammar.CPU_NUM_PROCESSORS ) )
        cpuSystem = int( parseResults.get( CpuLineGrammar.CPU_SYSTEM_TICKS ) )
        self.fields["cpuSystemPercentage"] = ( ( cpuSystem / ticksPerSecond ) * 100 ) / numProcessors

        self.fields["@version"] = 1

