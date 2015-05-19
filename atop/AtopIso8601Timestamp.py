from atop.LineHeaderGrammar import LineHeaderGrammar

class AtopIso8601Timestamp( object ):

    def toIso8601( self, parseResults ):
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

        return iso8601
