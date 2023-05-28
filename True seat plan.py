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
    
d=[]
def arrange(a,b,s,z,k):
    a=random.randint(z, k)
    
    s=a in b
    if(s!=True):
        b.append(a)
        print(a,end='   ')
        
    else:
        
        arrange(a,b,s,z,k)
        
        
    
    
for i in range(r):
    for j in range(col):
        c=random.randint(e, f)
        z=c in d
        if (z!=True):
            
            print(c,end='   ')
            d.append(c)
        else:
            arrange(c,d,z,e,f)
            
            
      
    print()

        