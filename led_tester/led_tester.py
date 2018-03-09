import re
import urllib.request
import requests
import sys

class LED: 
 
    def instructions(input, grid):
        
        for x in input:
            
            numbers=[int(s) for s in re.findall(r'\b\d+\b', x)]
            x1=numbers[0]
            y1=numbers[1]
            x2=numbers[2]
            y2=numbers[3]    
            
            match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', x)
            match2=re.findall(r'.*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', x)
            match3=re.findall(r'.*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', x)
            newsum=0
            newsum1=0
            newsum2=0
            if match1:
                def turn_on(x1, y1, x2, y2):
                    x_values = [True for i in range(x1, x2)]
                    y_values = [True for i in range(y1, y2)]
                    return sum(x_values +  y_values)
                newsum=(sum(a2d) + turn_on(x1, y1, x2, y2))
             
            if match2:
                def turn_off(x1, y1, x2, y2):
                    x_values = [False for i in range (x1, x2)]
                    y_values = [False for i in range (y1, y2)]
                    return sum(x_values +  y_values)
               
                newsum1=newsum+turn_off(x1, y1, x2, y2)
                
            if match3:
                def switch(x1, y1, x2, y2):
                    if x1 == True:
                        x1_value=[False for i in range(x1)]
                    else:
                        x1_value=[True for i in range(x1)]
                    if x2 == True:
                        x2_value=[False for i in range(x2)]
                    else:
                        x2_value=[True for i in range(x2)]
                    if y1 == True:
                        y1_value=[False for i in range(y1)]
                    else:
                        y1_value=[True for i in range(y1)]
                    if y2 == True:
                        y2_value=[False for i in range(y2)]
                    else:
                        y2_value=[True for i in range(y2)]
                    
                    return (x1_value + y1_value + x2_value + y2_value)
                
                
                newsum2=newsum1+sum(switch(x1, y1, x2, y2))
                return newsum2
                
                

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
            return sum(x1, y1, x2, y2)

        
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

    def readfile(input):
        if input.startswith('http'):
            uri=input
            req=urllib.request.urlopen(uri)
            buffer=req.read().decode('utf-8')
            r = requests.get(uri).text
            for line in r:
                
                lines= ('\n'.join(r.split('\n')[1:]))
                return lines.splitlines()
            
        else:
            filename = sys.argv[1]
            with open (filename) as f:
                for line in f.readlines():
                    values = [line.rstrip('\n') for line in open (filename)]
                    values1=values[1:]    
                    return values1
                              


    def grid(number):
        N=int(number)
        a2d=[ list(range(i*N, i*N + N)) for i in range(N) ]
        a2d=[False for i in range(N)]
        return a2d


input = sys.argv[1]
number=LED.grid_number(input)
a2d=LED.grid(number)

lines = str(LED.readfile(input))

print (LED.instructions(LED.readfile(input), a2d))
