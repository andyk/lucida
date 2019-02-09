"""
Weather API configuration details
"""

import ConfigParser, sys, config

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[asection]\n'

    def readline(self):
        if self.sechead:
            try: 
                return self.sechead
            finally: 
                self.sechead = None
        else: 
            return self.fp.readline()

cp = ConfigParser.SafeConfigParser()
cp.readfp(FakeSecHead(open("../../config.properties")))
port_dic = dict(cp.items('asection'))
PORT = int(port_dic['we_port'])

# Open Weather Map API key
# https://openweathermap.org/api
OWM_API_URL_BASE = 'http://api.openweathermap.org/data/2.5/weather?'
OWM_API_KEY = config.OWM_API_KEY
