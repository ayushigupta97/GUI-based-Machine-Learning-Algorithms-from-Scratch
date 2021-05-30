# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:50:30 2021

@author: AYUSHI GUPTA
"""

def progC():
    import csv
    import math
    import numpy
    import pandas as pd
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from sklearn.metrics import recall_score,precision_score
    from io import StringIO
    with open('D:/Machine Learning/Assignments/iris.csv','r') as file:
        x=[]
        y=[]
        reader=csv.reader(file)
        print(len(list(reader)))
        for row in reader:
            z=[]
            for i in range(0,len(row)-1):
                z.append(row[i])
            x.append(z)
            #print(row[i])
            #y.append(row[len(row)])
        print(x)
        
    
    
    def euclidDist(xTrain,test,k,yTrain):
        dist=[]
        for i in range(len(xTrain)):
            distance=0
            for j in range(len(test)):
                distance+=pow(xTrain[i][j]-test[j],2)
            #print(distance)
            dist.append(math.sqrt(distance))
        d=numpy.argsort(dist)
        firstkdist=[]
        for i in range(0,k):
            firstkdist.append(yTrain[d[i]])
        a=0
        b=0
        c=0
        #print(d)
        for i in range(len(firstkdist)):
            if firstkdist[i]=="Iris-setosa":
                a=a+1
            elif firstkdist[i]=="Iris-versicolor":
                b=b+1
            else:
                c=c+1
        if a>b and a>c:
            return "Iris-setosa"
        elif b>a and b>c:
            return "Iris-versicolor"
        else:
            return "Iris-verginica"
        
    def getNearestK(xTrain,xTest,k,yTrain):
        yPredict=[]
        l=[]
        print(len(xTest))
        #print(xTest)
        for i in range(len(xTest)):
            l=euclidDist(xTrain,xTest[i],k,yTrain)
            yPredict.append(l)
        return yPredict
        
    #5print(xTrain)
    
    
    def accuracy(yPredict,ytest):
        count=0
        for i in range(len(ytest)):
            if yPredict[i]==ytest[i]:
                count=count+1
        #print (float(count)/len(ytest))
        return (float(count)/len(ytest))*100
    
    data=pd.read_csv('D:/Machine Learning/Assignments/iris.csv')
    print(data.shape)
    x=data[["SL","SW","PL","PW"]]
    y=data["SPECIES"]
    from sklearn.model_selection import train_test_split
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)
    print(xTrain)
    print(xTest)
    print(yTrain)
    print(yTest)
    xtrain=xTrain.to_numpy()
    xtest=xTest.to_numpy()
    ytrain=yTrain.to_numpy()
    ytest=yTest.to_numpy()
    #k=int(input("Enter any odd value of k "))
    k=7
    yPredict=getNearestK(xtrain,xtest,k,ytrain)
    t=accuracy(yPredict,ytest)
    recall = recall_score(ytest, yPredict, average='weighted')
    precision = precision_score(ytest, yPredict, average='weighted')
    
    def counter_loop(): 
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("For knn we have used the iris dataset\n")
        print("Here we have taken the value of k is 7\n")        
        print("The accuracy of the model obtained is ")
        print(t)
        print("\nThe recall value obtained is ",recall)
        print("\nThe recall value obtained is ",precision)
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
    app = App(title="K Nearest Neighbour Algorithm", width=500, height=500,)
    counter = Text(app,text="K Nearest Neighbour Algorithm", size = 20, font = "Times New Roman", color="blue")
    button = PushButton(app, text ="Accuracy", command=counter_loop)
    app.display() 
        
    '''def main():
        data=pd.read_csv('D:/Machine Learning/Assignments/iris.csv')
        print(data.shape)
        x=data[["SL","SW","PL","PW"]]
        y=data["SPECIES"]
        from sklearn.model_selection import train_test_split
        xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)
        print(xTrain)
        print(xTest)
        print(yTrain)
        print(yTest)
        k=int(input("Enter any odd value of k "))
        xtrain=xTrain.to_numpy()
        xtest=xTest.to_numpy()
        ytrain=yTrain.to_numpy()
        ytest=yTest.to_numpy()
        yPredict=getNearestK(xtrain,xtest,k,ytrain)
        t=accuracy(yPredict,ytest)
        print("The accuracy of the model obtained is ")
        print(t)
    
    if __name__ == "__main__":
        main()'''
