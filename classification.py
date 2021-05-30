# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 13:05:50 2021

@author: AYUSHI GUPTA
"""

def progB():
    
    import Single_perceptron as sp
    import Logistic_Regression as lr
    import NaiveBayes as nb
    import knn
    import tkinter
    from tkinter import Label, Button
    class MyFirstGUI:
        def __init__(self, master):
            labelfont = ('times', 20, 'bold')
            self.master = master
            master.title("Classification Algorithms")
    
            self.label = Label(master, text="Select any one of the Classification Algorithm",bg="orange",fg="purple")
            self.label.config(width=50)
            self.label.config(height=10)
            self.label.config(font=labelfont)
            self.label.pack()
    
            '''self.type_button = Button(master, text="K Means Clustering algorithm", command=kmc.progC,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()'''
            
            self.type_button = Button(master, text="Single Perceptron", command=sp.progC,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()
            
            self.type_button = Button(master, text="Naive Bayes", command=nb.progC,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()
            
            self.type_button = Button(master, text="k Nearest Neighbour", command=knn.progC,bg="yellow",fg="green")
            self.type_button.config(width=30)
            self.type_button.config(height=2)
            self.type_button.pack()
            
            self.type_button = Button(master, text="Logistic Regression", command=lr.progC,bg="yellow",fg="green")
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
