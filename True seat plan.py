# -*- coding: utf-8 -*-
"""
Created on Sun May 28 04:05:45 2023

@author: USER
"""

import random
e=int(input("First roll:"))
f=int(input("Last roll:"))
r=int(input("Row no:"))
col=int(input("Column no:"))
x=1
    
d=[]
def arrange(a,b,s,z,k):
    a=random.randint(z, k)
    
    s=a in b
    if(s!=True):
        b.append(a)
        
        
    else:
        
        arrange(a,b,s,z,k)
        
        
    
    
for i in range(r):
    for j in range(col):
        c=random.randint(e, f)
        z=c in d
        if (z!=True):
            
            print(x,"th roll:",c,end='     ')
            d.append(c)
            x=x+1
        else:
            arrange(c,d,z,e,f)
            print(x,"th roll:",c,end='     ')
            x=x+1
            
            
      
    print()

        
