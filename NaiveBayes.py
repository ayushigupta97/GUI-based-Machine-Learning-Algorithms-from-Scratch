# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:52:02 2020

@author: AYUSHI GUPTA
"""

def progC():
    import numpy as np
    import pandas as pd
    from guizero import App, Combo,Text,CheckBox, ButtonGroup,PushButton,info,TextBox, Picture
    import os
    import time
    import sys    
    from io import StringIO

    
    data = pd.DataFrame()
    
    # Create our target variable
    data['Gender'] = ['male','male','male','male','female','female','female','female']
    
    # Create our feature variables
    data['Height'] = [6,5.92,5.58,5.92,5,5.5,5.42,5.75]
    data['Weight'] = [180,190,170,165,100,150,130,150]
    data['Foot_Size'] = [12,11,12,10,6,8,7,9]
    
    # View the data
    print(data)
    
    person = pd.DataFrame()
    
    # Create some feature values for this single row
    person['Height'] = [6]
    person['Weight'] = [130]
    person['Foot_Size'] = [8]
    
    # View the data 
    print(person)
    
    # Number of males
    n_male = data['Gender'][data['Gender'] == 'male'].count()
    
    # Number of males
    n_female = data['Gender'][data['Gender'] == 'female'].count()
    
    # Total rows
    total_ppl = data['Gender'].count()
    # Number of males divided by the total rows
    P_male = n_male/total_ppl
    
    # Number of females divided by the total rows
    P_female = n_female/total_ppl
    # Group the data by gender and calculate the means of each feature
    data_means = data.groupby('Gender').mean()
    
    # View the values
    data_means
    # Group the data by gender and calculate the variance of each feature
    data_variance = data.groupby('Gender').var()
    
    # View the values
    data_variance
    # Means for male
    male_height_mean = data_means['Height'][data_variance.index == 'male'].values[0]
    male_weight_mean = data_means['Weight'][data_variance.index == 'male'].values[0]
    male_footsize_mean = data_means['Foot_Size'][data_variance.index == 'male'].values[0]
    
    # Variance for male
    male_height_variance = data_variance['Height'][data_variance.index == 'male'].values[0]
    male_weight_variance = data_variance['Weight'][data_variance.index == 'male'].values[0]
    male_footsize_variance = data_variance['Foot_Size'][data_variance.index == 'male'].values[0]
    
    # Means for female
    female_height_mean = data_means['Height'][data_variance.index == 'female'].values[0]
    female_weight_mean = data_means['Weight'][data_variance.index == 'female'].values[0]
    female_footsize_mean = data_means['Foot_Size'][data_variance.index == 'female'].values[0]
    
    # Variance for female
    female_height_variance = data_variance['Height'][data_variance.index == 'female'].values[0]
    female_weight_variance = data_variance['Weight'][data_variance.index == 'female'].values[0]
    female_footsize_variance = data_variance['Foot_Size'][data_variance.index == 'female'].values[0]
    # Create a function that calculates p(x | y):
    def p_x_given_y(x, mean_y, variance_y):
    
        # Input the arguments into a probability density function
        p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))
        
        # return p
        return p
    # Numerator of the posterior if the unclassified observation is a male
    P_male 
    x=p_x_given_y(person['Height'][0], male_height_mean, male_height_variance) 
    y=p_x_given_y(person['Weight'][0], male_weight_mean, male_weight_variance) 
    z=p_x_given_y(person['Foot_Size'][0], male_footsize_mean, male_footsize_variance)
    result1=P_male*x*y*z
    print(result1)
    # Numerator of the posterior if the unclassified observation is a female
    P_female 
    x=p_x_given_y(person['Height'][0], female_height_mean, female_height_variance) 
    y=p_x_given_y(person['Weight'][0], female_weight_mean, female_weight_variance) 
    z=p_x_given_y(person['Foot_Size'][0], female_footsize_mean, female_footsize_variance)
    result2=P_female*x*y*z
    print(result2)
    
    def counter_loop():
        old_stdout = sys.stdout
        result = StringIO()        
        sys.stdout = result
        print("\nHere we have created our own dataset of person with\n attributes height, weight and Foot Size with a class label of Gender")
        print("\nNow we use our model to predict for the person having\n height=6, weight=130 and foot size=8 is whether male or female")
        print("\nPosterior probability of person being male is ",result1)
        print("Posterior probablity of person being female is ",result2)
        if(result1>=result2):
            print("\nValue of result1 is greater, thus person is male")
        else:
            print("\nValue of result2 is greater, thus person is female")
        result_string = result.getvalue()
        counter.value = result_string # read output        
        button.disable()
    
    #To build the GUI
    app = App(title="Naive Bayes Algorithm", width=1000, height=500,)
    counter = Text(app, text="Naive Bayes",size = 20, font = "Times New Roman", color="green")
    button = PushButton(app, command=counter_loop, text ="Accuracy")
    app.display() 