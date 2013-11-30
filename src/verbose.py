VB = False
vIndent = 0

def vprint(string):
    global verbose
    if VB == False:
        return
    
    s = ""

    for i in range(vIndent):
        s = s + " "

    s = s + string

    print s

def indent(i):
    global vIndent
    vIndent += i
