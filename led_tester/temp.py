filename = sys.argv[1]
            new_list=[]
            def slice(listname):
                for x in listname:
                    new_list=[]
                    new_list +=[x]
                    x1=listname[0:1]
                    y1=listname[1:2]
                    x2=listname[2:3]
                    y2=listname[3:4]

                return x1, y1, x2, y2
                print ("slice")
            def turn_on(x1, y1, x2, y2):
                x_values = [True for i in range(x1, x2)]
                y_values = [True for i in range(y1, y2)]
                print ("turn_on")
                print (sum(x_values +  y_values))
            def turn_off(x1, y1, x2, y2):
                x_values = [False for i in range (x1, x2)]
                y_values = [False for i in range (y1, y2)]
                return sum(x_values +  y_values)
                print ("turn_off")
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
                print ("switch")
                return sum(x1, y1, x2, y2)
  with open (filename) as f:
                lines=f.readlines()
                for line in f.readlines():
                    values=[line.rstrip('\n') for line in open(filename)]
                    values1=values[1:]
                    print (values1)
                for line in filename:


                    for i in lines:
                        values2=i

                        numbers=[int(s) for s in re.findall(r'\b\d+\b', str(values2))]

                        match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values2))
                        match2=re.findall(r'.*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values2))
                        match3=re.findall(r'.*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values2))


                        if match1:
                            print ("match1")
                            return turn_on(x1, y1, x2, y2)
                        if match2:
                            print ("match2")
                            return turn_off(x1, y1, x2, y2)
                        if match3:
                            print ("match3")
                            return switch(x1, y1, x2, y2)
                str1='turn on'
                str2='turn off'
                str3='switch'




                match1=re.findall(r'.*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values2))
                match2=re.findall(r'.*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values2))
                match3=re.findall(r'.*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*', str(values2))
                if match1:
                    return turn_on(x1, y1, x2, y2)
                if match2:
                    return turn_off(x1, y1, x2, y2)
                if match3:
                    return switch(x1, y1, x2, y2)
