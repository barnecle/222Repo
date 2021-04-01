import os
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from joblib import load
import numpy as np
import json
import pandas as pd
from flask import jsonify, render_template, request, redirect, url_for
from flask import send_file
from sklearn.metrics import confusion_matrix

UPLOAD_FOLDER='.'

#load the model

my_model = load('mush_model.pkl')


file_path = "~/E222/222Repo/mushrooms.csv"
data = pd.read_csv(file_path)

le = LabelEncoder()

for i in data.columns:
        data[i] = le.fit_transform(data[i])

y = data["class"]

def prediction(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    data = pd.read_csv(file_path)

    le = LabelEncoder()

    for i in data.columns:
                data[i] = le.fit_transform(data[i])
    x = data.drop(["class","gill-attachment","bruises"], axis = 1)

    prediction = my_model.predict(x.values)
    name = class_names[prediction]
    name = name.tolist()
    name_str = json.dumps(name)
    return name_str

