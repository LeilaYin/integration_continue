#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 14:46:18 2020

@author: leila.nedjar
"""

# coding: utf-8
from tkinter import *
from calculatrice import *

# create window
window = Tk()
window.title("Calculatrice")

def callback():
    btn.configure(text="click")
    
btn = Button(window, text="ok", command=callback)
btn.pack()

window.mainloop()
