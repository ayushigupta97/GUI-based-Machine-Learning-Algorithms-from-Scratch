# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:06:13 2021

@author: AYUSHI GUPTA
"""

def progC():
    import pandas as pd
    import numpy as np
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from io import StringIO
    from sklearn.metrics import recall_score,precision_score
    df = pd.read_csv("D:/Machine Learning/Assignments/energy_data.csv")
    
    
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    #print( df, '\n\n\n')
    tt = sc.fit_transform(df[{'Ambient Temperature','Vacuum','Ambient Pressure','Relative Humidity'}])
    print( tt, '\n\n\n' )
    
    X = tt
    Xtrain = tt
    Ytrain = df['Power Energy']
    Y = df['Power Energy']
    
    
    def mean_square_error( Y, y_predicted) :
      return np.mean( (Y - y_predicted)**2 )
    
    def fit(X, y, lr, n_iters, weights, bias):
        n_samples, n_features = X.shape
    
        # init parameters
        weights = np.zeros(n_features)
        bias = 0
    
        # gradient descent
        for _ in range( n_iters):
            y_predicted = np.dot(X, weights) + bias
            # compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
    
            #print( 'Weight : ', weights, ' bias : ', bias, '\n\n')
            # update parameters
            weights -= lr * dw
            bias -= lr * db
    
        return weights, bias
    
    
    def predict(X, weights, bias):
        y_approximated = np.dot(X, weights) + bias
        return y_approximated
    
    
    def multi_variate_linear_regression( Xtest, Ytest ) :
        learning_rate = 0.005
        no_of_iterations = 1000
    
        weights = None
        bias = None
        #print( 'Xtrain : \n', Xtrain)
        weights , bias = fit(Xtrain, Ytrain, learning_rate, no_of_iterations, weights, bias )
    
        print( 'Weight : ', weights , '\nBias : ', bias)
        predictions = predict(Xtest, weights, bias)
    
    
        print( '\nPredictions : ' ,predictions,'\n', '\nYtest : \n' , Ytest )
    
        mse = mean_square_error( Ytest, predictions)
    
        print( '\nThe Mean Square Error : ', mse)
        return mse
    
    mse=multi_variate_linear_regression( X, Y )
    
    def counter_loop():
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("\nWe have used the energy dataset having five attributes")
        print( '\nThe Mean Square Error : ', mse)
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
        
    app = App(title="Multivariate Linear Rehression", width=700, height=400,)
    counter = Text(app, text="Multivariate Linear Regression",size = 20, font = "Times New Roman", color="red")
    button = PushButton(app, command=counter_loop, text ="Accuracy")
    app.display() 