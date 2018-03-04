import urllib.request
import requests
import sys

def parseFile(input):
	if input.startswith('http'):
		uri=input
		req=urllib.request.urlopen(uri)
		buff=req.read().decode('utf-8')
		r = requests.get(uri).text                     
		print('\n'.join(r.split('\n')[:5]))
	else:
		filename = "data/data.txt"
		with open (filename) as f:
			for line in f.readlines():
				values = line.strip().split()
			return

input = sys.argv[1]
parseFile(input)
