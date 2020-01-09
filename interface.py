#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:46:18 2020

@author: leila.nedjar
"""

# coding: utf-8
from tkinter import *
from calculatrice import *

class Interface:
    
    def __init__(self):
        window = Tk()
        window.title("Calculatrice")

        f = Frame(window, height=200, width=200)
        f.pack_propagate(0) # don't shrink
        f.pack()
        btn = Button(window, text="click", command= lambda : self.callback(btn,label,c))
        label.pack()
        btn.pack()
    
        window.mainloop()

        
    var = StringVar()
    label = Label(window, text="Hello")
    
    c = 0 

    def callback(self,btn,label,c):
        if c == 1:
            btn.configure(text="ok")
            label.configure(text="World!")
            c = 0
        else:
            c = 1
    
  
if __name__=='__main__':
    
    # create window
    interface = Interface()
    