# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:01:18 2020

@author: AYUSHI GUPTA
"""
def progC():
    import tkinter as tk
    #from tkinter import *
    #import streamlit as st
    import matplotlib
    import numpy as np
    import matplotlib.pyplot as plt
    matplotlib.use("TkAgg")
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import pandas as pd
    import math
    import PIL
    from PIL import Image,ImageTk 
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from io import StringIO
    
    #plot the dataset for visualization
    def plot(data,root):
        figure2=plt.figure(figsize=(6, 6))
        plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
        scatter3=FigureCanvasTkAgg(figure2,root)
        scatter3.get_tk_widget().pack()
        plt.xlabel('Eruption time in mins')
        plt.ylabel('Waiting time to next eruption')
        plt.title('Visualization of raw data')
        return
    
    def plot_classify(data,lab,x1,y1,x2,y2,root):
        figure2=plt.figure(figsize=(6, 6))
        data1=[]
        data2=[]
        for i in range(len(lab)):
            x=[]
            x.append(data[i][0])
            x.append(data[i][1])
            if(lab[i]==0):
                data1.append(x)
            else:
                data2.append(x)
        data1=np.array(data1)
        data2=np.array(data2)
        xdata1=[]
        ydata1=[]
        xdata2=[]
        ydata2=[]
        for i in range(len(data1)):
            xdata1.append(data1[i][0])
            ydata1.append(data1[i][1])
        for i in range(len(data2)):
            xdata2.append(data2[i][0])
            ydata2.append(data2[i][1])
        plt.scatter(xdata1,ydata1,s=30,c='green', label='cluster1')
        plt.scatter(xdata2,ydata2,s=30,c='blue', label='cluster2')
        scatter3=FigureCanvasTkAgg(figure2,root)
        scatter3.get_tk_widget().pack()
        plt.plot(x1,y1,'ro',marker='*',c='r', label='centroid1')
        plt.plot(x2,y2,'ro', marker='*',c='r', label='centroid2')
        plt.legend()
        plt.xlabel('Eruption time in mins')
        plt.ylabel('Waiting time to next eruption')
        plt.title('Visualization of clustered data', fontweight='bold')
        
    #Now assume the number of clusters
        
    def cal_centroid(data,df):
        label=[]
        for i in range(len(data)):
            x=math.sqrt(math.pow(data[i][0]-df[0][0],2)+math.pow(data[i][1]-df[0][1],2))
            y=math.sqrt(math.pow(data[i][0]-df[1][0],2)+math.pow(data[i][1]-df[1][1],2))
            if(x<=y):
                label.append(0)
            else:
                label.append(1)
        x1=0
        y1=0
        x2=0
        y2=0
        n1=0
        n2=0
        for i in range(len(label)):
            if(label[i]==0):
                x1=x1+data[i][0]
                y1=y1+data[i][1]
                n1=n1+1
            else:
                x2=x2+data[i][0]
                y2=y2+data[i][1]
                n2=n2+1
        x1=x1/n1
        y1=y1/n1
        x2=x2/n2
        y2=y2/n2
        return x1,y1,x2,y2,label
    
    def new_centroid(data,label):
        x1=0
        y1=0
        x2=0
        y2=0
        n1=0
        n2=0
        for i in range(len(label)):
            if(label[i]==0):
                x1=x1+data[i][0]
                y1=y1+data[i][1]
                n1=n1+1
            else:
                x2=x2+data[i][0]
                y2=y2+data[i][1]
                n2=n2+1
        x1=x1/n1
        y1=y1/n1
        x2=x2/n2
        y2=y2/n2
        df=np.array([[x1,y1],[x2,y2]])
        return df
    
    data=pd.read_csv("D:/Machine Learning/Assignments/faithful.csv")
    data=data.iloc[:,1:3]
    print(data)
    root = tk.Tk()
    canvas = tk.Canvas(root, width = 300, height = 300)  
    canvas.pack()  
    #img = ImageTk.PhotoImage(Image.open("D:\Machine Learning\Assignments\kcluster1.png"))  
    #canvas.create_image(20, 20, image=img) 
   
    plot(data,root)
    label=[]
    df=data.sample(n=2)
    print(df)
    data=data.to_numpy()
    df=df.to_numpy()
    
    print("Let us suppose that the value of k is 2")
    for i in range(0,5):        
        x1,y1,x2,y2,label=cal_centroid(data,df)
        print("Values of first centroid is")
        print(x1)
        print(y1)
        print(x2)
        print(y2)
        plot_classify(data,label,x1,y1,x2,y2,root)
        df=new_centroid(data,label)
    
    def counter_loop():
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("\nWe will be using faithful data having eruptions and waiting time as features")
        print("\nAfter the visualization of dataset\nas shown in diagram we decided to take k=2")
        print("\nThe new centroids in form (x1,y1) and (x2,y2) for two clusters are ")
        print(df)
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
    app = App(title="K Means Clustering Algorithm", width=1000, height=500,)
    counter = Text(app, text="K Means Clustering Model",size = 20, font = "Times New Roman", color="green")
    button = PushButton(app, command=counter_loop, text ="Accuracy")
    app.display()
    root.mainloop()
    '''image = PIL.Image.open("kcluster1.png")
    BTC_img = PIL.ImageTk.PhotoImage(image)
    BTC_img_label = tk.Label(image=BTC_img)
    BTC_img_label.image = BTC_img
    BTC_img_label.grid(row=2, column=0)'''
    #mm=Picture(app,image="kcluster_rawdata.ppm")
    #mm=Picture(app,image="kcluster1.png")
    #mm=Picture(app,image="kcluster2.png")
    #mm=Picture(app,image="kcluster3.png")
    #mm=Picture(app,image="kcluster4.png")
    #mm=Picture(app,image="kcluster5.png")
    #app.display() 
                     
    '''def main():
        data=pd.read_csv("D:/Machine Learning/Assignments/faithful.csv")
        data=data.iloc[:,1:3]
        print(data)
        plot(data)
        label=[]
        df=data.sample(n=2)
        print(df)
        data=data.to_numpy()
        df=df.to_numpy()
        print("Let us suppose that the value of k is 2")
        for i in range(0,5):        
            x1,y1,x2,y2,label=cal_centroid(data,df)
            print("Values of first centroid is")
            print(x1)
            print(y1)
            print(x2)
            print(y2)
            plot_classify(data,label,x1,y1,x2,y2)
            df=new_centroid(data,label)
    
    if __name__=="__main__":
        main()'''
