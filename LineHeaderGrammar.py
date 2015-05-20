from pyparsing import Regex, Literal, Word, nums

HOSTNAME = "hostname"
EPOCH = "epoch"
YEAR = "year"
MONTH = "month"
DAY = "day"
HOUR = "hour"
MINUTE = "minute"
SECOND = "second"
LOG_INTERVAL = "log_interval"

class LineHeaderGrammar(object):

    def __init__(self):
        host = Regex(r'([a-zA-Z0-9](?:(?:[a-zA-Z0-9-]*|(?<!-)\.(?![-.]))*[a-zA-Z0-9]+)?)')

        epoch = Word(nums)

        year = Word(nums)
        month = Word(nums)
        day = Word(nums)
        dateSep = Literal('/').suppress()

        date = year(YEAR)
        date += dateSep
        date += month(MONTH)
        date += dateSep
        date += day(DAY)

        hour = Word(nums)
        minute = Word(nums)
        second = Word(nums)
        timeSep = Literal(':').suppress()

        time = hour(HOUR)
        time += timeSep
        time += minute(MINUTE)
        time += timeSep
        time += second(SECOND)

        logInterval = Word(nums)

        grammar = host(HOSTNAME)
        grammar += epoch(EPOCH)
        grammar += date
        grammar += time
        grammar += logInterval(LOG_INTERVAL)

        self.myGrammar = grammar

    def getGrammar(self):
        return self.myGrammar
