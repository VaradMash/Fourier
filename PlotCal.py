import numpy as np
import Plotter as u

def graphfull(x1,y1,p):
    s,c,f1 = 0,0,0
    x=[]
    y=[]
    
    

    step=(2*np.pi)/p
    s1,c1=0,0

    for i in range(len(y1)):
        s1+=(float(y1[i])*np.sin(float(x1[i])*step))
        c1+=(float(y1[i])*np.cos(float(x1[i])*step))

    s1=2*s1/(len(x1))
    c1=2*c1/(len(x1))
    s1=s1**2
    c1=c1**2
    f1 =(s1+c1)**(0.5)
    


    for n in range(1,11):
        s,c=0,0
        
        for i in range(len(y1)):
            c+=float(y1[i])*np.cos(n*float(x1[i])*step)
            s+=float(y1[i])*np.sin(n*float(x1[i])*step)
        

        s=2*s/(len(x1))
        c=2*c/(len(x1))

        t=((s**2)+(c**2))**(0.5)
        
        

        x.append(n)
        r=t/f1
        y.append(r)
            

    u.plotg(x,y)

        

   


#Half Range Cosine
def graphhalfcos(x1,y1,p):
    step=(np.pi)/p
    
    c = 0
    x=[]
    y=[]
    c1=0
    f1=0
    for i in range(len(y1)):
        
        c1+=(float(y1[i])*np.cos(float(x1[i])*step))
    f1 =2*c1/len(x1)


    for n in range(1,11):
        c=0
        for i in range(len(y1)):
        
            c+=float(y1[i])*np.cos(n*float(x1[i])*step)
        
        
        c=2*c/(len(x1))

        t=c
        

        

        x.append(n)
        r=t/f1
        y.append(r)

    u.plotg(x,y)


        

#Half Range Sine
def graphhalfsin(x1,y1,p):
    step=(np.pi)/p
    
    s = 0
    x=[]
    y=[]
    s1=0
    f1=0
    for i in range(len(y1)):
        
        s1+=(float(y1[i])*np.sin(float(x1[i])*step))
    f1 =2*s1/len(x1)

    for n in range(1,11):
        s=0
    
        for i in range(len(y1)):
        
            s+=float(y1[i])*np.sin(n*float(x1[i])*step)
        

        s=2*s/(len(x1))

        t=s

        

        x.append(n)
        r=t/f1
        y.append(r)

    u.plotg(x,y)
