import os
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from joblib import load
import numpy as np
import json
import pandas as pd

#load the model

my_model = load('mush_model.pkl')


file_path = "~/E222/222Repo/mushrooms.csv"
data = pd.read_csv(file_path)

le = LabelEncoder()

for i in data.columns:
        data[i] = le.fit_transform(data[i])

y = data["class"]

def my_prediction(id):
    dummy = np.array(id)
    dummyT = dummy.reshape(1,-1)
    r = dummy.shape
    t = dummyT.shape
    r_str = json.dumps(r)
    t_str = json.dumps(t)
    prediction = my_model.predict(dummyT)
    name = class_names[prediction]
    name = name.tolist()
    name_str = json.dumps(name)
    str = [t_str, r_str, name_str]
    return str
