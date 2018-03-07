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
                lines=('\n'.join(r.split('\n')))
            print (lines.split('\n')[1])
            numbers=[int(s) for s in re.findall(r'\b\d+\b', lines.split('\n')[1])]
            x1=numbers[0]
            y1=numbers[1]
            x2=numbers[2]
            y2=numbers[3]    
               
            str1='turn on'
            str2='turn off'
            str3='switch'
            def turn_on(x1, y1, x2, y2):
                x_values = [True for i in range(x1, x2)]
                y_values = [True for i in range(y1, y2)]
                return sum(x_values +  y_values)
            match1=re.search(r'turn on', lines[1])
            match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', lines.split('\n')[1])
            match2=re.search(r'values[1]', str2)
            match3=re.search(r'values[1]', str3)
            if match1:
                return turn_on(x1, y1, x2, y2)
        else:
            filename = sys.argv[1]
            with open (filename) as f:
                for line in f.readlines():
                    values = [line.rstrip('\n') for line in open (filename)]
                    pat=re.match(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
                numbers=[int(s) for s in re.findall(r'\b\d+\b', values[1])]
                x1=numbers[0]
                y1=numbers[1]
                x2=numbers[2]
                y2=numbers[3]
                
                str1='turn on'
                str2='turn off'
                str3='switch'
                def turn_on(x1, y1, x2, y2):
                    x_values = [True for i in range(x1, x2)]
                    y_values = [True for i in range(y1, y2)]
                    return sum(x_values +  y_values)
                match1=re.search(r'turn on', values[1])
                match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', values[1])
                match2=re.search(r'values[1]', str2)
                match3=re.search(r'values[1]', str3)
                if match1:
                    return turn_on(x1, y1, x2, y2)
                    

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
a2d=LED.grid(number)
print(LED.parseFile(input))

