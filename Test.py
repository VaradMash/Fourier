import tkinter
from tkinter import messagebox

def showharmonic(h,n):
    # message box display
    s='Harmonic '+str(int(n))+ '= '+str(h)
    messagebox.showinfo("RESULT",s)
