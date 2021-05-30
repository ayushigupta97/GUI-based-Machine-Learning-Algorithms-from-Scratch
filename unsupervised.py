# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:16:47 2021

@author: AYUSHI GUPTA
"""

def progA():
    import kMeansClustering as kmc
    import tkinter
    from tkinter import Label, Button
    class MyFirstGUI:
        def __init__(self, master):
            labelfont = ('times', 20, 'bold')
            self.master = master
            master.title("Unsupervised Algorithm")
    
            self.label = Label(master, text="Check this unsupervised algorithm",bg="orange",fg="purple")
            self.label.config(width=50)
            self.label.config(height=10)
            self.label.config(font=labelfont)
            self.label.pack()
            
            self.type_button = Button(master, text="Clustering", command=kmc.progC,bg="yellow",fg="green")
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

