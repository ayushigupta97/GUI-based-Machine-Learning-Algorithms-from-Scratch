# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:57:02 2021

@author: AYUSHI GUPTA
"""
def progA():
    import kMeansClustering as kmc
    import classification as cf
    import regression as rg
    import tkinter
    from tkinter import Label, Button
    class MyFirstGUI:
        def __init__(self, master):
            labelfont = ('times', 20, 'bold')
            self.master = master
            master.title("Classification or Regression Algorithms")
    
            self.label = Label(master, text="Select any of these algorithms",bg="orange",fg="purple")
            self.label.config(width=50)
            self.label.config(height=10)
            self.label.config(font=labelfont)
            self.label.pack()
    
            self.type_button = Button(master, text="Classification", command=cf.progB,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()
            
            self.type_button = Button(master, text="Regression", command=rg.progB,bg="yellow",fg="green")
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

