'''
Created on May 25, 2015

@author: hsd
'''
from headergrammar import HeaderGrammar

class ResourceLine(object):
    '''
       Base class for all atop resource lines
    '''

    def __init__(self):
        self._parse_results = None
        pass

    def get_host_name(self):
        return self._parse_results.get(HeaderGrammar.HOSTNAME)

    def get_timestamp(self):
        return int(self._parse_results.get(HeaderGrammar.EPOCH))

    def addFields(self, fields):
        pass

    def _store_parse_results(self, parse_results):
        self._parse_results = parse_results
