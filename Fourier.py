import numpy as np

def calculatefull(x,y,n):
    s,c = 0,0


    
    for i in range(6):
        c+=float(y[i])*np.cos(n*float(x[i])*(np.pi)/3)
        s+=float(y[i])*np.sin(n*float(x[i])*(np.pi)/3)
        

    s=s/3
    c=c/3

    t=(s**2+c**2)**(0.5)

    return t


#Half Range Cosine
def calculatehalfcos(x,y,n):
    c = 0


    
    for i in range(6):
        
        c+=float(y[i])*np.cos(n*float(x[i])*(np.pi)/6)
        
        
    c=c/3

    t=c

    return t

#Half Range Sine
def calculatehalfsin(x,y,n):
    s = 0


    
    for i in range(6):
        
        s+=float(y[i])*np.sin(n*float(x[i])*(np.pi)/6)
        

    s=s/3

    t=s

    return t
