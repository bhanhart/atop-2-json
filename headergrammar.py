from pyparsing import Regex, Literal, Word, nums

class HeaderGrammar(object):
    HOSTNAME = "hostname"
    EPOCH = "epoch"
    LOG_INTERVAL = "log_interval"

    def __init__(self):
        host = Regex(r'([a-zA-Z0-9](?:(?:[a-zA-Z0-9-]*|(?<!-)\.(?![-.]))*[a-zA-Z0-9]+)?)')

        epoch = Word(nums)

        year = Word(nums)
        month = Word(nums)
        day = Word(nums)
        dateSep = Literal('/')

        date = year
        date += dateSep
        date += month
        date += dateSep
        date += day

        hour = Word(nums)
        minute = Word(nums)
        second = Word(nums)
        timeSep = Literal(':')

        time = hour
        time += timeSep
        time += minute
        time += timeSep
        time += second

        logInterval = Word(nums)

        grammar = host(self.HOSTNAME)
        grammar += epoch(self.EPOCH)
        grammar += date.suppress()
        grammar += time.suppress()
        grammar += logInterval(self.LOG_INTERVAL)

        self.cpu_line_grammar = grammar

    def get_grammar(self):
        return self.cpu_line_grammar
