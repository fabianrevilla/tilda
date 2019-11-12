import re

file = open("text.txt")

reg_expr_w = re.compile('.*?td +class.*?weekColumn.*?>(v.*?)</td', re.I)
reg_expr_d = re.compile('.*?td.*?class.*?changeDateLink.*?headline.*?>([F-T][a-zåäög]) *(.+?)</td')
reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)</td')
reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)</td', re.I)

rad = 1
for line in file:
    week = reg_expr_w.match(line)
    day = reg_expr_d.match(line)
    time = reg_expr_t.match(line)
    info = reg_expr_i.match(line)
    if week != None:
        print("Rad %s matchas av första" %(rad))
    
    if day != None:
        print("Rad %s matchas av andra" %(rad))

    if time != None:
        print("Rad %s matchas av tredje" %(rad))

    if info != None:
        print("Rad %s matchas av fjärde" %(rad))

    rad = rad + 1
