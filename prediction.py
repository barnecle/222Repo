import os
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import numpy as np
import json
import pandas as pd
from joblib import load

UPLOAD_FOLDER='.'

#load the model
my_model = load('mush_model.pkl')
class_names = {'p', 'e'}

def predict(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    data = pd.read_csv(file_path)

    le = LabelEncoder()

    for i in data.columns:
                data[i] = le.fit_transform(data[i])
    x = data.drop(["gill-attachment","bruises"], axis = 1)
    xv =  x.values
    prediction = my_model.predict(xv)
    new_predict = []

    for i in range(0, len(prediction)):
        if(prediction[i] == 1):
            new_predict.append("p")
        else:
            new_predict.append("e")
    
    arr = np.array(new_predict)
    data['prediction'] = arr
    print(data)
    data.to_csv(file_path)
    name = arr
    name = name.tolist()
    name_str = json.dumps(name)
    return name_str

def predict_input(array):
    if(len(array)!=22):
        print("Error: wrong amount of input")
    else:
        le = LabelEncoder()
        for i in array:
            array[i] = le.fit_transform(array[i])
        prediction = my_model.predict(array)
        if(prediction[i] == 1):
                new_predict = "p"
            else:
                new_predict = "e"
        name_str = json.dumps(new_predict)
        return name_st
