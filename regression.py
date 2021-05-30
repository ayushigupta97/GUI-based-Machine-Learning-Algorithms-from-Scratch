# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:14:09 2021

@author: AYUSHI GUPTA
"""

def progB():
    
    import linear_regression as LR
    import multivariateLR as mlr
    import tkinter
    from tkinter import Label, Button
    class MyFirstGUI:
        def __init__(self, master):
            labelfont = ('times', 20, 'bold')
            self.master = master
            master.title("Regression Algorithms")
    
            self.label = Label(master, text="Select any of the Regression Algorithm you want",bg="orange",fg="purple")
            self.label.config(width=50)
            self.label.config(height=10)
            self.label.config(font=labelfont)
            self.label.pack()
            
            self.type_button = Button(master, text="Linear Regression", command=LR.progC,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()
            
            self.type_button = Button(master, text="Multivariate Linear Regression", command=mlr.progC,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()
    
            self.close_button = Button(master, text="Close", command=master.quit,bg="yellow",fg="green")
            self.close_button.config(width=30)
            self.close_button.config(height=2)
            self.close_button.pack()
    
        
    
    root = tkinter.Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
