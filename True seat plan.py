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
        if(x==f+1):
            break
        if (z!=True):
            if(x==1):
                print(x,"st roll:",c,end='     ')
                d.append(c)
                x=x+1
            elif (x==2):
                print(x,"nd roll:",c,end='     ')
                d.append(c)
                x=x+1
            elif (x==3):
                print(x,"rd roll:",c,end='     ')
                d.append(c)
                x=x+1
            
            else:
                print(x,"th roll:",c,end='     ')
                d.append(c)
                x=x+1
            
                
                
        else:
            arrange(c,d,z,e,f)
            if(x==1):
                print(x,"st roll:",c,end='     ')
                x=x+1
            elif (x==2):
                print(x,"nd roll:",c,end='     ')
                x=x+1
            elif (x==3):
                print(x,"rd roll:",c,end='     ')
                x=x+1
            else:
                print(x,"th roll:",c,end='     ')
                x=x+1
            
            
      
    print()
