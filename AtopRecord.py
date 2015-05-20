import logging
import json

import MemLineGrammar
import CpuLineGrammar
import LineHeaderGrammar
import AtopIso8601Timestamp

class AtopRecord( object ):
    MemLineGrammar = MemLineGrammar.MemLineGrammar().getGrammar()
    CpuLineGrammar = CpuLineGrammar.CpuLineGrammar().getGrammar()

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

        self.fields["log_host"] = parseResults.get( LineHeaderGrammar.HOSTNAME )
        tsConvertor = AtopIso8601Timestamp.AtopIso8601Timestamp()
        self.fields["@timestamp"] = tsConvertor.toIso8601( parseResults.asDict() )
        self.fields["@version"] = 1

    def __parseCpuLine( self, line ):
        parseResults = self.CpuLineGrammar.parseString( line )

        ticksPerSecond = int( parseResults.get( CpuLineGrammar.CPU_TICKS_PER_SECOND ) )
        numProcessors = int( parseResults.get( CpuLineGrammar.CPU_NUM_PROCESSORS ) )
        cpuSystem = int( parseResults.get( CpuLineGrammar.CPU_SYSTEM_TICKS ) )

        self.fields["cpuSystemPercentage"] = ( ( cpuSystem / ticksPerSecond ) * 100 ) / numProcessors

        self.fields["log_host"] = parseResults.get( LineHeaderGrammar.HOSTNAME )
        tsConvertor = AtopIso8601Timestamp.AtopIso8601Timestamp()
        self.fields["@timestamp"] = tsConvertor.toIso8601( parseResults.asDict() )
        self.fields["@version"] = 1

