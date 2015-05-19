import logging

from atop import AtopRecord

class AtopFileParser( object ):
    def __init__( self, logger ):
        self.logger = logger or logging.getLogger( __name__ )
        self.currentRecord = None
        self.records = []

    def parse( self, atopFileName ):
        self.logger.debug( "Processing file '" + atopFileName + "'" )

        with open( atopFileName, 'r' ) as atopFile:
            self.load( atopFile )

    def newRecord( self, recordNo ):
        self.logger.debug( "Creating record " + str( recordNo ) )
        self.currentRecord = AtopRecord.AtopRecord( recordNo )

    def storeRecord( self ):
        self.records.append( self.currentRecord )
        self.currentRecord = None

    def load( self, atopFile ):
        inTotalsSinceBoot = False
        recordNo = 0
        for line in atopFile:
            line = line.rstrip()
            if line == "RESET":
                inTotalsSinceBoot = True
            elif line == "SEP":
                recordNo += 1
                if inTotalsSinceBoot:
                    inTotalsSinceBoot = False
                else:
                    self.storeRecord()
                self.newRecord( recordNo )
            else:
                if inTotalsSinceBoot:
                    continue
                self.currentRecord.parseLine( line )

        self.__saveToJsonFile()

    def __saveToJsonFile( self ):
        with open( "/home/hsd/work/atop.mem.json", 'w' ) as outputFile:
            for record in self.records:
                outputFile.write( str( record ) )
                outputFile.write( "\n" )
#        print( '%s' % '\n'.join( map( str, self.records ) ) )
