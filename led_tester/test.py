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
            print (lines.split('\n')[2])
            numbers=[int(s) for s in re.findall(r'\b\d+\b', lines.split('\n')[2])]
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
            def turn_off(x1, y1, x2, y2):
                x_values = [False for i in range (x1, x2)]
                y_values = [False for i in range (y1, y2)]
                return sum(x_values +  y_values)
            def switch(x1, y1, x2, y2):
                if x1 == True:
                    x1 = False
                elif x1 == False:
                    x1 = True
                elif x2 == True:
                    x2 = False
                elif x2 == False:
                    x2 = True
                elif y1 == True:
                    y1 = False
                elif y1 == False:
                    y1 = True
                elif y2 == True:
                    y2 = False
                elif y2 == False:
                    y2 = True


            match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', lines.split('\n')[2])
            match2=re.findall(r'.*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', lines.split('\n')[2])
            match3=re.findall(r'.*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', lines.split('\n')[2])
            if match1:
                return turn_on(x1, y1, x2, y2)
            if match2:
                return turn_off(x1, y1, x2, y2)
            if match3:
                return switch(x1, y1, x2, y2)
        else:
            filename = sys.argv[1]
            with open (filename) as f:
                for line in f.readlines():
                    values1 = [line.rstrip('\n') for line in open (filename)]
                
                values2 = values1[1:]
                numbers=[int(s) for s in re.findall(r'\b\d+\b', str(values2))]
                for i in numbers:

                    x1=numbers[0]
                    y1=numbers[1]
                    x2=numbers[2]
                    y2=numbers[3]
                    print (x1, y1, x2, y2)    
                str1='turn on'
                str2='turn off'
                str3='switch'
                def turn_on(x1, y1, x2, y2):
                    x_values = [True for i in range(x1, x2)]
                    y_values = [True for i in range(y1, y2)]
                    return sum(x_values +  y_values)
                def turn_off(x1, y1, x2, y2):
                    x_values = [False for i in range (x1, x2)]
                    y_values = [False for i in range (y1, y2)]
                    return sum(x_values +  y_values)
                def switch(x1, y1, x2, y2):
                    if x1 == True:
                        x1 = False
                    elif x1 == False:
                        x1 = True
                    elif x2 == True:
                        x2 = False
                    elif x2 == False:
                        x2 = True
                    elif y1 == True:
                        y1 = False
                    elif y1 == False:
                        y1 = True
                    elif y2 == True:
                        y2 = False
                    elif y2 == False:
                        y2 = True

                
                match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values))
                match2=re.findall(r'.*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values))
                match3=re.findall(r'.*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values))
                if match1:
                    return turn_on(x1, y1, x2, y2)
                if match2:
                    return turn_off(x1, y1, x2, y2)
                if match3:
                    return switch(x1, y1, x2, y2)    

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

