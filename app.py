from flask import Flask, render_template, request
import sklearn
import pandas as pd
import pickle
import numpy as np
import math


app = Flask(__name__)


@app.route('/')

def index():

    return render_template('index.html',locations=locations,area_type=area_type)

@app.route('/predict', methods=['GET','POST'])




  


if __name__ == '__main__':
    app.run(debug=True, port= 5500)
