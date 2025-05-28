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

@app.route('/predict', methods=['GET','POST'])
def predict():

    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    area_type = request.form.get('area_type')
    balcony = request.form.get('balcony')

#    print(location,bhk,bath,sqft,area_type,balcony)

    input = pd.DataFrame([[location,sqft,bath,bhk,area_type,balcony]],columns=['location','total_sqft','bath','bhk','area_type', 'balcony'])
    prediction = pipe.predict(input)[0] * 1e5
  
    return str(prediction)



  


if __name__ == '__main__':
    app.run(debug=True, port= 5500)
