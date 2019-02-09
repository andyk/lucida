#!/usr/bin/env python

import sys
sys.path.append('../')

from WeatherConfig import*

from lucidatypes.ttypes import QuerySpec
from lucidaservice import LucidaService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import json
import urllib
import re

class WeatherHandler(LucidaService.Iface):
    def create(self, LUCID, spec):
        """
        Do nothing
        """
        return

    def learn(self, LUCID, knowledge):
        """
        Do nothing
        """
        return


    def infer(self, LUCID, query):
        """
        Determine the weather based off input
        Parameters:
         - LUCID: ID of Lucida user
         - query: query
        """
        input_data = query.content[0].data[-1]
        result = 'No weather found for %s' % input_data

        #TODO - Figure out a better way to get the location out of the weather query.
        # Current method can only handle basic requests, doesn't do well with non USA cities or anywhere in new mexico

        print input_data

        input_data = re.sub('\[u', '', input_data)
        input_data = re.sub('[^A-Za-z0-9 ]+', '', input_data)

        location_string = input_data.split("in ")
        locations_input = str(location_string[-1]).split()
        location_pieces_count = locations_input.__len__()

        if location_pieces_count == 1:
            url_location = urllib.quote_plus(locations_input[-1]) # Handles when a location has only the city name
        elif location_pieces_count == 2:
            url_location = urllib.quote_plus(locations_input[-2] + ", " + locations_input[-1] + '\']') # Handles city name with state at end
        elif location_pieces_count == 3:
            url_location = urllib.quote_plus(locations_input[-3] + " " + locations_input[-2] + ", " + locations_input[-1] + '\']') # Handles multi part city with state at the end
        elif location_pieces_count == 4:
            url_location = urllib.quote_plus(locations_input[-4] + " " + locations_input[-3] + " " + locations_input[-2] + ", " + locations_input[-1] + '\']') # Handles multi part city with state at the end

        print 'Debug: var url_location - ', url_location

        try:
            f = urllib.urlopen(OWM_API_URL_BASE + \
                    'q=%s&appid=%s&units=imperial&type=like' % (url_location, OWM_API_KEY))
            # To help with debugging, enter what was "tried" in a web browser and that will let you see what the response is
            print "Tried: ", OWM_API_URL_BASE + \
                    'q=%s&appid=%s&units=imperial&type=like' % (url_location, OWM_API_KEY)
            json_string = f.read()
            parsed_json = json.loads(json_string)
            if 'cod' in parsed_json and 'message' in parsed_json:
                message = parsed_json['message']
                result = "Error using API, " + message
                return result
            if 'weather' in parsed_json and 'main' in parsed_json and 'name' in parsed_json:
                weather = parsed_json['weather'][0]['description']
                temp = parsed_json['main']['temp']
                city = parsed_json['name']
                # if city in input_data:
                result = 'Current weather in %s is %s, temperature is %s Fahrenheit' % (city, weather, temp)
                print 'From Open Weather Map: %s' % result
            f.close()
        except IOError as err:
            if 401 in err:
                result = 'Unauthorized Weather API keys'
            else:
                result = 'Weather Service is broken!'
        return result

# Set handler to our implementation
handler = WeatherHandler()
processor = LucidaService.Processor(handler)
transport = TSocket.TServerSocket(port=PORT)
tfactory = TTransport.TFramedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print 'WE at port  %d' % PORT
server.serve()
