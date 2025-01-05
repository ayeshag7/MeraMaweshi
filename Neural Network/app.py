#import libraries
from tensorflow import keras
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from itertools import chain
import pandas as pd
#import tensorflow.keras
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow
data = pd.read_csv('cbr_P_A (1).csv')
# data=pd.read_excel('/content/ALL_CASE_BASE_WITH_REPITATIVE_CASE.xlsx')
data = data.drop("Unnamed: 0", axis=1)
data1 = data.iloc[:, :84]
data1 = data1.fillna(0)
# data[data!=0]

disease = data.iloc[:, 83:]

for ind in data1.index:
    for col in data1.columns:
        if (col == 'Name' or col == 'Sex' or col == 'DiseaseName.1'):
            continue
        if data1[col][ind] != 0:
            data1[col][ind] = 1

list_symptoms = []
for col in data1.columns:
    if (col == 'Name' or col == 'Sex' or col == 'DiseaseName.1'):
        continue
    else:
        list_symptoms.append(col)

disease_name = data1.iloc[:, 82:].values.tolist()
disease_name = list(chain.from_iterable(disease_name))
disease_name = list(dict.fromkeys(disease_name))
(disease_name).sort()
# Initialize the flask App
app = Flask(__name__)
model = keras.models.load_model('123.h5')
#model = pickle.load(open('model.pkl', 'rb'))

# default page of our web-app


@app.route('/')
def home():
    return render_template('index_1.html')

# To use the predict button in our web-app


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print(request.form.getlist('symptomsCheckboxGroup'))

    symptoms_selected = []
    for x in request.form.getlist('symptomsCheckboxGroup'):
        symptoms_selected.append(x)
    print(symptoms_selected)

    listofzeros = [0] * 80
    for j in symptoms_selected:
        listofzeros[list_symptoms.index(j)] = 1
    is_all_zero = np.all((listofzeros == 0))
    if is_all_zero:
        return "Please select symptoms"

    listofzeros_np = np.array(listofzeros)
    print(listofzeros_np)
    reshaped = listofzeros_np.reshape((1, 80))
    y_pred = model.predict(reshaped)
    print(y_pred)
    # Converting predictions to label

    pred = list()
    for i in range(len(y_pred)):
        pred.append(np.argmax(y_pred[i]))
    disease = disease_name[pred[0]]
    print(disease)
    return render_template('index.html', prediction_text='Predicted disease is :{}'.format(disease))


if __name__ == "__main__":
    app.run(debug=True)
