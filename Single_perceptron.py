# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:21:25 2020

@author: AYUSHI GUPTA
"""

def progC():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    import seaborn as sn
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from sklearn.metrics import recall_score,precision_score
    from io import StringIO
    
    def sigmoid(z):
        return 1 / (1 + np.e**(-z))
    
    
    def testres(weight,xtest):
        pred=[]
        for i in range(len(xtest)):
            x=sigmoid(np.dot(weight,xtest[i]))
            pred.append(x)
        return [1 if i > 0.5 else 0 for i in pred]
    
    
    def fit(xtrain,ytrain):
        epoch=10
        eta=0.1
        weight=np.zeros(5)
        for i in range(epoch):
            for j in range(len(xtrain)):
                ypred=sigmoid(np.dot(weight,xtrain[j]))
                weight=weight+eta*(ytrain[j]-ypred)*xtrain[j]
        return weight
        
    def accuracy(ypred,y_test):
        count=0
        for i in range(len(ypred)):
            if(ypred[i]==y_test[i]):
                count=count+1
        return (count/len(ypred))*100
    
    def plot_confusion(y_pred,y_test):
        data = confusion_matrix(y_test, y_pred)
        df_cm = pd.DataFrame(data, columns=np.unique(y_test), index = np.unique(y_test))
        df_cm.index.name = 'Actual'
        df_cm.columns.name = 'Predicted'
        plt.figure(figsize = (10,7))
        sn.set(font_scale=1.4)#for label size
        sn.heatmap(df_cm, cmap="Reds", annot=True,annot_kws={"size": 16})# font size
      
    data=pd.read_csv("D:/Machine Learning/Assignments/iris.csv")
    data=data.iloc[0:100,:]
    data['SPECIES']=data['SPECIES'].map({'Iris-setosa':0,'Iris-versicolor':1})
    x=data.iloc[:,0:4]
    y=data.iloc[:,4]    
    x=x.to_numpy()
    y=y.to_numpy()
    z=np.zeros(100)
    t=np.column_stack((z,x))
    #print(t)
    #print(t.shape,z.shape)
    X_train, X_test, y_train, y_test = train_test_split(t, y, test_size=0.2)
    #print(X_train.shape,X_test.shape)
    weight=fit(X_train,y_train)
    
    ypred=testres(weight,X_test)
    acc=accuracy(ypred,y_test)
    recall = recall_score(y_test, ypred, average='weighted')
    precision = precision_score(y_test, ypred, average='weighted')
    
    def counter_loop():
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("\nFor this model we have taken the Iris dataset\n in which first 100 samples are used")
        print("\nWe have taken epoch=10, learning rate=0.1 and sigmoid as activation function")
        print("\nThe weight matrix obtained is")
        print(weight)
        print("\nAccuracy of the model is found to be")
        print(acc)
        print("\nThe recall value obtained is ",recall)
        print("\nThe recall value obtained is ",precision)
        print("\nAlso there is a diagram for confusion mtrix")
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
    plot_confusion(ypred,y_test)
    app = App(title="Single Perceptron Model", width=1000, height=500,)
    counter = Text(app, text="Single Perceptron Model",size = 20, font = "Times New Roman", color="red")
    button = PushButton(app, command=counter_loop, text ="Accuracy")
    app.display() 
    '''def main():
        data=pd.read_csv("D:/Machine Learning/Assignments/iris.csv")
        data=data.iloc[0:100,:]
        data['SPECIES']=data['SPECIES'].map({'Iris-setosa':0,'Iris-versicolor':1})
        x=data.iloc[:,0:4]
        y=data.iloc[:,4]    
        x=x.to_numpy()
        y=y.to_numpy()
        z=np.zeros(100)
        t=np.column_stack((z,x))
        #print(t)
        #print(t.shape,z.shape)
        X_train, X_test, y_train, y_test = train_test_split(t, y, test_size=0.2)
        #print(X_train.shape,X_test.shape)
        weight=fit(X_train,y_train)
        print("The weight matrix obtained is")
        print(weight)
        ypred=testres(weight,X_test)
        acc=accuracy(ypred,y_test)
        print("Accuracy of the model is found to be")
        print(acc)
        plot_confusion(ypred,y_test)
        #print(ypred)
        
        
    if __name__=="__main__":
        main()'''
        
    
