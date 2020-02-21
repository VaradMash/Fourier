import numpy as np

def calculatefull(x,y,n,p):
    s,c = 0,0

    step=(2*np.pi)/p


    
    for i in range(len(y)):
        c+=float(y[i])*np.cos(n*float(x[i])*step)
        s+=float(y[i])*np.sin(n*float(x[i])*step)
        

    s=2*s/(len(x))
    c=2*c/(len(x))

    t=(s**2+c**2)**(0.5)

    return t


#Half Range Cosine
def calculatehalfcos(x,y,n,p):
    step=(np.pi)/p
    
    c = 0


    
    for i in range(len(y)):
        
        c+=float(y[i])*np.cos(n*float(x[i])*step)
        
        
    c=2*c/(len(x))

    t=c

    return t

#Half Range Sine
def calculatehalfsin(x,y,n,p):
    step=(np.pi)/p

    s = 0


    
    for i in range(len(y)):
        
        s+=float(y[i])*np.sin(n*float(x[i])*step)
        

    s=2*s/(len(x))

    t=s

    return t
