# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:02:52 2021

@author: AYUSHI GUPTA
"""

def progC():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from io import StringIO
    
    
    def plot(X,Y,b1,b0):
        #plotting values 
        x_max = np.max(X) + 100
        x_min = np.min(X) - 100
        
        x = np.linspace(x_min, x_max, 1000)
        y = b0 + b1 * x
        
        plt.plot(x, y, color='#00ff00', label='Linear Regression')
        
        plt.scatter(X, Y, color='#ff0000', label='Data Point')
        
        plt.xlabel('Years Experience(year)')
        
        plt.ylabel('Salary(Rs)')
        plt.legend()
        plt.show()
    
    def rmse(x,y,m,c):
        error=0
        for i in range(len(y)):
            ypred=m*x[i]-c
            error+=(y[i]-ypred)**2
        error=np.sqrt(error/len(x))
        return error
    
    def r_square(x,y,m,c):
        ssr = 0
        sst = 0
        y_mean=np.mean(y)
        for i in range(len(x)) :
            y_pred = c + m * x[i]
            ssr += (y[i] - y_mean) ** 2
            sst += (y[i] - y_pred) **2
    
        value  = 1 - (sst/ssr)
        return value
    
    def linear_regression(x,y):
        x_mean=np.mean(x)
        y_mean=np.mean(y)
    
        num=0
        den=0
        for i in range(len(x)):
            num=num+(x[i]-x_mean)*(y[i]-y_mean)
            den=den+(x[i]-x_mean)**2
        m=num/den
        c=y_mean-m*x_mean
        print("m=",m)
        print("c=",c)
        plot(x,y,m,c)
        rr=rmse(x,y,m,c)
        #print('The root mean square error obtained is ',rmse(x,y,m,c))
        #print('Now we check accuracy of model using R^2 method')
        r=r_square(x,y,m,c)
        #print(r)
        return rr,r,m,c
    
    data=pd.read_csv('D:/Machine Learning/Assignments/Salary_Data.csv')
    print(data.shape)
    print(data)
    x=data["YearsExperience"]
    y=data["Salary"]
    print(x)
    print(y)
    xd=x.to_numpy()
    yd=y.to_numpy()
    sq_error,r2,m,c=linear_regression(xd,yd)
    def counter_loop():
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("\nFor this model we will use salary dataset\n with two attributes one for salary and other having years of experience")
        print('\nThe root mean square error obtained is ',sq_error)
        print('\nNow we check accuracy of model using R^2 method',r2)
        print("\nFor the required line we obtain the values of m and c as",m,c)
        print("\nIn the graph we have obtained the line shown in green colour")
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
    app = App(title="Linear Regression Model", width=1000, height=500,)
    counter = Text(app, text="Linear Regression",size = 20, font = "Times New Roman", color="green")
    button = PushButton(app, command=counter_loop, text ="Accuracy")
    app.display()
    
    '''def main():
        data=pd.read_csv('D:/Machine Learning/Assignments/Salary_Data.csv')
        print(data.shape)
        print(data)
        x=data["YearsExperience"]
        y=data["Salary"]
        print(x)
        print(y)
        xd=x.to_numpy()
        yd=y.to_numpy()
        linear_regression(xd,yd)
    
    if __name__=="__main__":
        main()'''