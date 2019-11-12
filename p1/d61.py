## LAB1
# Kopiera det här programmet, du kan markera allt med C-a och kopiera med C-c och lägg det i en fil som du döper till p1.a.py och exekvera programmet med python3 p1.a.py


############################################################
#
# Labb 1
#

# global variables

a="DD1321.htm"
url = "https://cloud.timeedit.net/kth/web/public01/ri177359X80Z0QQ5Z16g3YZ5yQ086Y75Z0QgQY5Q5027o5p4ll55q1W97.html"

############################################################
#
# imports and defs
#
import re, getopt, sys, urllib.request


class info:
    def __init__(self):
        self.tid= ''
        self.titel= []
        self.veckodag= ''
        self.veckonr= ''
        self.datum= ''
    
    
    def __str__(self):
        s = "{ " + self.veckonr + " " + self.veckodag + " " + self.datum + " " + self.tid
        if len(self.titel) > 3:
            s += " : " + self.titel[0] + " " + self.titel[1] + " " + self.titel[2] + " " + self.titel[3]
        s += " }"
        return s
    
    def __contains__(self, x):
        if x in self.veckonr:
            return True
        elif x in self.tid:
            return True
        elif x in self.titel:
            return True
        elif x in self.veckodag:
            return True
        elif x in self.datum:
        	return True

###########################################################################
##
## Funktion som hämtar data ur filen file_content
##
## IN: filen file_content
##
## OUT: Veckodagar, datum, veckonr & titlar
##
def parse_url_file(file_content):
    vecko_var=''
    veckodag_var=''
    datum=''
    datum_old=''
    vecka_old=''
    veckodag_old=''
    vek = []
    
    reg_expr_w = re.compile('.*?td +class.*?weekColumn.*?>(v.*?)</td', re.I)
    reg_expr_d = re.compile('.*?td.*?class.*?changeDateLink.*?headline.*?>([F-T][a-zåäög]) *(.+?)</td')
    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)</td')
    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)</td', re.I)
    
    lines = file_content.split('\n')
    qq = info()
    newEntry = False
    for j, line in enumerate(lines):
        
        m = reg_expr_d.match(line)#dag
        if (m != None) :
            veckodag_old = m.group(1)
            datum_old = m.group(2)#lägger undan datumet i en variabel
            next
            
        m = reg_expr_w.match(line)#vecka
        if (m != None) :         
            vecka_old=m.group(1)
            next
    
        m = reg_expr_i.match(line)#info
        if (m != None) :
            qq.titel.append(m.group(1))
            newEntry=True#första titeln -> sätt newEntry till True
            datum=datum_old
            vecko_var = vecka_old#vid ny titel visas den förra veckan
            veckodag_var=veckodag_old
            next
        
        m = reg_expr_t.match(line)#tid
        if (m != None) :
            if newEntry == True:
                vek.append(qq)
   
            qq = info()
            qq.tid = m.group(1)
            next
        qq.datum=datum    
        qq.veckodag = veckodag_var
        qq.veckonr = vecko_var
        
    vek.append(qq)#lägger till sista schemahändelsen i vek
    return vek


###########################################################################
##
## get file content
##
## IN file_name
##
## OUT file_content
##
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("No such file", file_name, " please run with --update")
        print ("    python", sys.argv[0], "--update")
        sys.exit()
    
    #file_content = infil.readlines()
    file_content = infil.read()#läser in hela filen som en enda text-sträng
    return file_content

###########################################################################
##
## usage
##
## IN tar indata från kommandoraden med sys.argv
##
## OUT visar version av schema
##
def usage():
    print ("Usage example:")
    print ("python" , sys.argv[0] ,  "--update ")
    print ("    updates Time Edit schedule")
    print ("python" , sys.argv[0] ,  '--check "v 49"')
    print ("    checks schedule for week 49")
    print ("python" , sys.argv[0])
    print ("    prints previously downloaded schedule")

###########################################################################
##
## parse_command_line_args
##
## IN Input från kommandoraden
##
## OUT Returnerar en dictionary, med info om vilken vecka som ska kollas upp, att hjälp att använda programmet behövs eller att scehmat behövs uppdateras
##
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print ("Unknown option")
        usage()
        sys.exit(2)
    
    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"]=value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo

###########################################################################
##
## print_schedule
##
## IN Data med alla schema-händelser
##
## OUT Schema-händelser
##
def print_schedule(data):
    print ("----------- Schedule -------------")
    for item in data:
        print (item)

###########################################################################
##
## search_data
##
## IN "What", det som ska sökas efter i schemat. Indata från parse_command_line_args() är vilken vecka som ska kollas upp
##
## OUT Item - den sökta datan i dataset.
##
def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print (item)
    if (found == False):
        print ("Nothing happens", what)

###########################################################################
##
## main
##
## IN DD1321.htm, kursinfo
##
## OUT Utskrivet schema
##
def main():
    
    
    global url
    # get command line options
    todo = parse_command_line_args()
    
    # update time edit file
    if 'update' in todo:
        print ("fetching url ...")
        urllib.request.urlretrieve(url, a)
        print ("         done")
    
    # Get schedule from disc
    filedata  = get_file_content(a)
    sched = parse_url_file(filedata)
    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)


###########################################################################

if __name__ == "__main__":
    main()


