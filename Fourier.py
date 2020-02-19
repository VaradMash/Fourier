from sympy import *
import numpy as np

def gettheta(l,n):
    global sintheta=[]
    global costheta=[]
    for i in range(6):
        t=np.sin((l[i])*(np.pi/3))
        c=np.cos((l[i])*(np.pi/3))
        sintheta.append(t)
        costheta.append(c)


    
