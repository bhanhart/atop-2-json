import pyparsing as pp

class LineHeaderGrammar( object ):
    HOSTNAME = "hostname"
    EPOCH = "epoch"
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    SECOND = "second"
    LOG_INTERVAL = "log_interval"

    def __init__( self ):
        host = pp.Regex( r'([a-zA-Z0-9](?:(?:[a-zA-Z0-9-]*|(?<!-)\.(?![-.]))*[a-zA-Z0-9]+)?)' )

        epoch = pp.Word( pp.nums )

        year = pp.Word( pp.nums )
        month = pp.Word( pp.nums )
        day = pp.Word( pp.nums )
        dateSep = pp.Literal( '/' ).suppress()

        date = year( self.YEAR )
        date += dateSep
        date += month( self.MONTH )
        date += dateSep
        date += day( self.DAY )

        hour = pp.Word( pp.nums )
        minute = pp.Word( pp.nums )
        second = pp.Word( pp.nums )
        timeSep = pp.Literal( ':' ).suppress()

        time = hour( self.HOUR )
        time += timeSep
        time += minute( self.MINUTE )
        time += timeSep
        time += second( self.SECOND )

        logInterval = pp.Word( pp.nums )

        grammar = host( self.HOSTNAME )
        grammar += epoch( self.EPOCH )
        grammar += date
        grammar += time
        grammar += logInterval( self.LOG_INTERVAL )

        self.myGrammar = grammar

    def getGrammar( self ):
        return self.myGrammar
