# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:33:35 2022

@author: ACER
"""

import pandas as pd 

import pickle
from sklearn.model_selection import train_test_split

df=pd.read_csv("C:/Users/ACER/Desktop/ty/clean_data.csv")
x=df.iloc[:,1:5]
y=df['energy_production']
from sklearn import preprocessing
normalized_X = preprocessing.normalize(x)

x_train, x_test, y_train, y_test = train_test_split(normalized_X, y, test_size=0.30, random_state=31)
from sklearn.ensemble import RandomForestRegressor
r_f= RandomForestRegressor(n_estimators=102,
    min_samples_split=20,
    min_samples_leaf=28,
    max_features='auto')
r_f.fit(x_train, y_train)


pickle.dump(r_f,open('model355.pkl','wb'))

model = pickle.load(open('model355.pkl','rb'))