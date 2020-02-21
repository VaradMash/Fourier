from tkinter import *
import Fourier as f
import Test as t
root=Tk()

root.title('Harmonic Calculator')



        

def getandpass(event):

    n=float(e1.get())
    p=float(e0.get())

    x=[]
    x.append(float(e2.get()))
    x.append(float(e3.get()))
    x.append(float(e4.get()))
    x.append(float(e5.get()))
    x.append(float(e6.get()))
    x.append(float(e7.get()))

    y=[]
    y.append(float(e2y.get()))
    y.append(float(e3y.get()))
    y.append(float(e4y.get()))
    y.append(float(e5y.get()))
    y.append(float(e6y.get()))
    y.append(float(e7y.get()))

    
    
    h=f.calculatefull(x,y,n,p)
    t.showharmonic(h,n)
    

def getandpasscos(event):

    n=float(e1.get())
    p=float(e0.get())

    x=[]
    x.append(float(e2.get()))
    x.append(float(e3.get()))
    x.append(float(e4.get()))
    x.append(float(e5.get()))
    x.append(float(e6.get()))
    x.append(float(e7.get()))

    y=[]
    y.append(float(e2y.get()))
    y.append(float(e3y.get()))
    y.append(float(e4y.get()))
    y.append(float(e5y.get()))
    y.append(float(e6y.get()))
    y.append(float(e7y.get()))

    
    
    h=f.calculatehalfcos(x,y,n,p)
    t.showharmonic(h,n)
    

def getandpasssin(event):

    n=float(e1.get())
    p=float(e0.get())

    x=[]
    x.append(float(e2.get()))
    x.append(float(e3.get()))
    x.append(float(e4.get()))
    x.append(float(e5.get()))
    x.append(float(e6.get()))
    x.append(float(e7.get()))

    y=[]
    y.append(float(e2y.get()))
    y.append(float(e3y.get()))
    y.append(float(e4y.get()))
    y.append(float(e5y.get()))
    y.append(float(e6y.get()))
    y.append(float(e7y.get()))

    
    
    h=f.calculatehalfsin(x,y,n,p)
    t.showharmonic(h,n)
    




b1=Button(root,text='Full Range',bg='Turquoise')
b2=Button(root,text='Half Range Cosine',bg='Turquoise')
b3=Button(root,text='Half Range Sine',bg='Turquoise')

l2=Label(root,text='Enter required Harmonic')
e1=Entry(root)

l0=Label(root,text="Enter Period")
e0=Entry(root)


#First Row
l3=Label(root,text='Sr.No.')
l4=Label(root,text='x')
l5=Label(root,text='y')


#Serial Numbers
l6=Label(root,text='1')
l7=Label(root,text='2')
l8=Label(root,text='3')
l9=Label(root,text='4')
l10=Label(root,text='5')
l11=Label(root,text='6')

#XEntries
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e7=Entry(root)

#YEntries
e2y=Entry(root)
e3y=Entry(root)
e4y=Entry(root)
e5y=Entry(root)
e6y=Entry(root)
e7y=Entry(root)

l2.grid(row=0,column=0)
e1.grid(row=0,column=1)

#First Row
l3.grid(row=1,column=0)
l4.grid(row=1,column=1)
l5.grid(row=1,column=2)

#serial Number placement
l6.grid(row=2,column=0)
l7.grid(row=3,column=0)
l8.grid(row=4,column=0)
l9.grid(row=5,column=0)
l10.grid(row=6,column=0)
l11.grid(row=7,column=0)

#xEntries Placement
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)
e5.grid(row=5,column=1)
e6.grid(row=6,column=1)
e7.grid(row=7,column=1)

#Yentries placement
e2y.grid(row=2,column=2)
e3y.grid(row=3,column=2)
e4y.grid(row=4,column=2)
e5y.grid(row=5,column=2)
e6y.grid(row=6,column=2)
e7y.grid(row=7,column=2)


#Period Placement
l0.grid(row=10,column=0)
e0.grid(row=10,column=1)



#Button Placement
b1.grid(row=11,column=0)
b2.grid(row=11,column=1)
b3.grid(row=11,column=2)


#Button Code Binding
b1.bind('<Button-1>',getandpass)
b2.bind('<Button-1>',getandpasscos)
b3.bind('<Button-1>',getandpasssin)



root.mainloop()
