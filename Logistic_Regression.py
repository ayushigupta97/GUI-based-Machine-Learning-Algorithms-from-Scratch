# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:21:56 2020

@author: AYUSHI GUPTA
"""
def progC():
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from io import StringIO
    from sklearn.metrics import recall_score,precision_score
    #import math
    import seaborn as sn
    
    def sigmoid(z):
        return 1 / (1 + np.e**(-z))
    
    def fit(xtrain,ytrain):
        epoch=20
        b=0
        lr=0.1
        weights=np.zeros(4)
        N = len(xtrain)
                     
        for _ in range(epoch):        
                # Gradient Descent
            y_hat=np.zeros([67,1])
            for i in range(N):
                y_hat[i][0]=np.sum(sigmoid(np.dot(xtrain[i], weights)+b))
            t=np.dot(xtrain.T,  y_hat - ytrain)
            t=t.reshape(4,)
            weights =weights- lr * t / N  
            b=b-lr*np.sum(y_hat-ytrain)/N   
        return weights,b
    
    def predict(X,weights,b):        
            # Predicting with sigmoid function
            z = np.dot(X, weights)+b
            # Returning binary result
            return [1 if i > 0.5 else 0 for i in sigmoid(z)]
        
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
    df=data.iloc[0:100,:]
    x=df[['SL','SW','PL','PW']]
    y=df[['SPECIES']]
    y['SPECIES']=y['SPECIES'].map({'Iris-setosa':0,'Iris-versicolor':1})
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    X_train=X_train.to_numpy()
    X_test=X_test.to_numpy()
    y_train=y_train.to_numpy()
    y_test=y_test.to_numpy()
    weights,b=fit(X_train,y_train)
    
    ypred=predict(X_test,weights,b)
    print(ypred)
    
    acc=accuracy(ypred,y_test)
    recall = recall_score(y_test, ypred, average='weighted')
    precision = precision_score(y_test, ypred, average='weighted')
    
    plot_confusion(ypred,y_test)
    def counter_loop():
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("\nHere we will use Iris dataset, its first 100 samples")
        print("\nEpoch=20 and learning rate=0.1")
        print("\nThe weight matrix we obtained is ",weights)
        print("\nThe bias value we obtained is ",b)
        print("\nThe accuracy of model we obtained is",acc)
        print("\nThe recall value obtained is ",recall)
        print("\nThe recall value obtained is ",precision)
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
    app = App(title="Logistic Regression Algorithm", width=1000, height=500,)
    counter = Text(app, text="Logistic Regression Algorithm",size = 20, font = "Times New Roman", color="blue")
    button = PushButton(app, command=counter_loop, text ="Accuracy")
    app.display() 
    
    '''def main():
        data=pd.read_csv("D:/Machine Learning/Assignments/iris.csv")
        df=data.iloc[0:100,:]
        x=df[['SL','SW','PL','PW']]
        y=df[['SPECIES']]
        y['SPECIES']=y['SPECIES'].map({'Iris-setosa':0,'Iris-versicolor':1})
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)
        print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
        X_train=X_train.to_numpy()
        X_test=X_test.to_numpy()
        y_train=y_train.to_numpy()
        y_test=y_test.to_numpy()
        weights,b=fit(X_train,y_train)
        print("The weight matrix we obtained is")
        print(weights)
        print("The bias value we obtained is")
        print(b)
        ypred=predict(X_test,weights,b)
        print(ypred)
        print("The accuracy of model we obtained is")
        acc=accuracy(ypred,y_test)
        print(acc)
        plot_confusion(ypred,y_test)
        
    
    
    if __name__=='__main__':
        main()'''