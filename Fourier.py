import numpy as np

def calculate(x,y,n):
    s,c = 0,0

    for i in range(6):
        c+=float(y[i])*np.cos(n*float(x[i])*(np.pi)/3)
        s+=float(y[i])*np.sin(n*float(x[i])*(np.pi)/3)
        

    s=s/3
    c=c/3

    t=(s**2+c**2)**(0.5)

    return t
