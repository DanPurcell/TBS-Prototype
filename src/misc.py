from math import *

def dist(a,b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
                    
    return sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

def bonusDamage(dam, pen, res):    
    diff = res - pen
       
    diff = 100.0/(100.0 + diff)

    bdam = dam * diff
    
    print dam, pen, res, diff, bdam
    
    return bdam