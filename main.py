# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:49:27 2021

@author: AYUSHI GUPTA
"""

import algo_types as at
import unsupervised as us
import tkinter
from tkinter import *

#import tkMessageBox
top=tkinter.Tk()
top.title("Machine Learning GUI")
#icon = tkinter.PhotoImage(file = "D:/Machine Learning/Assignments/ML.png")

# Finally, to display the image you will make use of the 'Label' method and pass the 'image' variriable as a parameter and use the pack() method to display inside the GUI.
#label = tkinter.Label(top, image = icon)
#label.pack()
labelfont = ('times', 20, 'bold')
label = Label(top,text="Let us have quick run to some Machine Learning Algorithms",fg="purple",bg='orange')
label.config(width=50)
label.config(height=20)
label.config(font=labelfont)
label.pack(expand=YES, fill=BOTH)
#label.pack()


B1=tkinter.Button(top,text="Supervised",command= at.progA,bg='#0052cc', fg="red")
B1.config(width=30)
B1.config(height=2)
B1.pack()
B2=tkinter.Button(top,text="Unsupervised",command= us.progA,bg='#0052cc', fg="red")     
B2.config(width=30)
B2.config(height=2)
B2.pack()
top.mainloop()

