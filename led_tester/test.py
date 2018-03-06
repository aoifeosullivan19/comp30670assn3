import re
import urllib.request
import requests
import sys

class LED: 
 
    def parseFile(input):
        if input.startswith('http'):
            uri=input
            req=urllib.request.urlopen(uri)
            buffer=req.read().decode('utf-8')
            r = requests.get(uri).text
            for line in r:
                return ('\n'.join(r.split('\n')))
        else:
            filename = sys.argv[1]
            with open (filename) as f:
                for line in f.readlines():
                    values = [line.rstrip('\n') for line in open (filename)]
                return values

    def grid_number(input):
        if input.startswith('http'):
            uri=input
            req=urllib.request.urlopen(uri)
            buffer=req.read().decode('utf-8')
            r = requests.get(uri).text
            for line in r:
                return int(('\n'.join(r.split('\n')[:1])))
        else:
            filename = sys.argv[1]
            with open (filename) as f:
                for line in f.readlines():
                    values = [line.rstrip('\n') for line in open (filename)]
                    grid_num=values[0]
                return int(grid_num)

    def grid(number):
        N=int(number)
        a2d=[ list(range(i*N, i*N + N)) for i in range(N) ]
        a2d=[False for i in range(N)]
        return a2d


input = sys.argv[1]
number=LED.grid_number(input)
print(LED.grid(number))
print(sum(LED.grid(number)))	
