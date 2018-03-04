import re
import urllib.request
import requests
import sys

def parseFile(input):
    if input.startswith('http'):
        uri=input
        req=urllib.request.urlopen(uri)
        buff=req.read().decode('utf-8')
        r = requests.get(uri).text
    else:
        filename = sys.argv[1]
        with open (filename) as f:
            for line in f.readlines():
                values = [line.rstrip('\n') for line in open (filename)]
                grid_num=values[0]
            return int(grid_num) 

def grid(number):
    N=number
    a2d=[ list(range(i*N, i*N + N)) for i in range(N) ]
    a2d=[off for i in range(N)]
    global off = 0
    global on = 1
    return a2d.count(on)

input = sys.argv[1]
grid_num=parseFile(input)
grid(grid_num)
print(grid_num)
	
