from flask import Flask, render_template, request
import sklearn
import pandas as pd
import pickle
import numpy as np
import math


app = Flask(__name__)
data = pd.read_csv('Bengaluru_House_Cleaned_Data.csv')
pipe = pickle.load(open('RidgeModel.pkl','rb'))

@app.route('/')
def index():
    
   
    locations = sorted(data['location'].unique())
    area_type = sorted(data['area_type'].unique())

    return render_template('index_test.html',locations=locations,area_type=area_type)

