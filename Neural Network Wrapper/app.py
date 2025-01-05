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
from flask_mysqldb import MySQL
import datetime
import warnings
warnings.filterwarnings('ignore')
from wrapper import *
# from flask_talisman import Talisman

 
app = Flask(__name__)
 


import pymysql
conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "",
        db='diseases_data_base',
        )
      
#cur = conn.cursor()

#conn.commit()

import csv

# open the file in the write mode
data_base = open('database.csv', 'a')
# create the csv writer
writer = csv.writer(data_base)

# open the file in the write mode
data_base_pet = open('database_pet.csv', 'a')
# create the csv writer
writer_pet = csv.writer(data_base_pet)



data = pd.read_csv('Advance_data_set_mera_maweshi_refined.csv')
# data=pd.read_excel('/content/ALL_CASE_BASE_WITH_REPITATIVE_CASE.xlsx')
data = data.drop("Unnamed: 0", axis=1)
data1 = data.iloc[:, :122]
data1 = data1.fillna(0)
# data[data!=0]

disease = data.iloc[:, 121:]

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

disease_name = data1.iloc[:, 121:].values.tolist()
disease_name = list(chain.from_iterable(disease_name))
disease_name = list(dict.fromkeys(disease_name))
(disease_name).sort()
# Initialize the flask App
print(disease_name)

model = keras.models.load_model('model123 (1).h5')
#model = pickle.load(open('model.pkl', 'rb'))


###### Here is Pet data
data_pet = pd.read_csv('MeraPet-22-07-2022.csv')

data1_pet = data_pet.iloc[:, :79]
data1_pet = data1_pet.fillna(0)
# data[data!=0]

disease_pet = data_pet.iloc[:, 78:]

for ind in data1_pet.index:
    for col in data1_pet.columns:
        if (col == 'Name' or col == 'Sex' or col == 'DiseaseName'):
            continue
        if data1_pet[col][ind] != 0:
            data1_pet[col][ind] = 1

list_symptoms_pet = []
for col in data1_pet.columns:
    if (col == 'Name' or col == 'Sex' or col == 'DiseaseName'):
        continue
    else:
        list_symptoms_pet.append(col)

disease_name_pet = data1_pet.iloc[:, 78:].values.tolist()
disease_name_pet = list(chain.from_iterable(disease_name_pet))
disease_name_pet = list(dict.fromkeys(disease_name_pet))
(disease_name_pet).sort()
# Initialize the flask App
print(disease_name_pet)

model_pet = keras.models.load_model('model_pet (1).h5')


# default page of our web-app

########################## Poultry part for model loading start ###############################
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import os
def get_poultry_model():
    global poultry_model
    poultry_model = load_model('poultry_model.h5')
    print("poultry_model_loaded")


def poultry_load_image(img_path):
    my_image = load_img(img_path, target_size=(512, 512))
    my_image = img_to_array(my_image)

    my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))
   
   
    my_image /= 255.                                     

    return my_image

def poultry_prediction(img_path):
    new_image = poultry_load_image(img_path)
    
    pred = poultry_model.predict(new_image)
    disease_list=["cocci","healthy","ncd","salmo"]
    disease= disease_list[np.argmax(pred)]

    
    return disease
get_poultry_model()
########################## End Poultry part for model loading start ###############################



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Main')
def Main():
    return render_template('index.html')


@app.route('/Home')
def Home():
    return render_template('Home.html')


@app.route('/Merapet')
def Merapet():
    return render_template('BasicInfoPet.html')






# To use the predict button in our web-app


@app.route('/BasicInfo')
def BasicInfo():
    return render_template('BasicInfo.html')

# To use the predict button in our web-app
@app.route('/RepeatbasicInfo',methods=['GET', 'POST'])
def RepeatbasicInfo():
    data_base = open('database.csv', 'a')
#create the csv writer
    writer = csv.writer(data_base)
    symptoms_selected = []
    symptoms_selected.append("suggested_disease")
    for x in request.form.getlist('symptomsCheckboxGroup'):
        symptoms_selected.append(x)
    writer.writerow(symptoms_selected)
    return render_template('BasicInfo.html')

# To use the predict button in our web-app
@app.route('/RepeatbasicInfopet',methods=['GET', 'POST'])
def RepeatbasicInfopet():
    data_base_pet = open('database_pet.csv', 'a')
#create the csv writer
    writerpet = csv.writer(data_base_pet)
    symptoms_selected = []
    symptoms_selected.append("suggested_disease")
    for x in request.form.getlist('symptomsCheckboxGroup'):
        symptoms_selected.append(x)
    writerpet.writerow(symptoms_selected)
    return render_template('BasicInfo.html')

@app.route('/MainSymptoms', methods=['POST'])
def MainSymptoms():
    # using datetime module

    data_base = open('database.csv', 'a')
    # ct stores current time
    writer = csv.writer(data_base)
    ct = datetime.datetime.now()
    print(type(ct))
    ct = ct.strftime("%m/%d/%Y, %H:%M:%S")
    date=[]
    print(ct)
    date.append(ct)
    writer.writerow(date)
    
    

    cattle_type = request.form['type']
    sex = request.form['sex']
    basic=[]
    basic.append(cattle_type)
    basic.append(sex)
    writer.writerow(basic)
    

    return render_template('MainSymptoms.html')
# @app.route('/meramaweshi', methods=['POST'])
# def meramaweshi():
#     return render_template('meramaweshi.html')

@app.route('/MainSymptomspet', methods=['POST'])
def MainSymptomspet():
    # using datetime module

    data_base_pet = open('database_pet.csv', 'a')
    # ct stores current time
    writer_pet = csv.writer(data_base_pet)
    ct = datetime.datetime.now()
    print(type(ct))
    ct = ct.strftime("%m/%d/%Y, %H:%M:%S")
    date=[]
    print(ct)
    date.append(ct)
    writer_pet.writerow(date)
    
    

    pet_type = request.form['type']
    sex = request.form['sex']
    basic=[]
    basic.append(pet_type)
    basic.append(sex)
    writer_pet.writerow(basic)
    data_base_pet.close()
    

    return render_template('MainSymptomspet.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    data_base = open('database.csv', 'a')
    # ct stores current time
    writer = csv.writer(data_base)
    print(request.form.getlist('symptomsCheckboxGroup'))

    symptoms_selected = []
    for x in request.form.getlist('symptomsCheckboxGroup'):
        symptoms_selected.append(x)
    print("symptoms_selected")
    print(symptoms_selected)

    listofzeros = [0] * 119
    for j in symptoms_selected:
        listofzeros[list_symptoms.index(j)] = 1
    is_all_zero = np.all((listofzeros == 0))
    if is_all_zero:
        return "Please select symptoms"

    listofzeros_np = np.array(listofzeros)
    print(listofzeros_np)
    reshaped = listofzeros_np.reshape((1, 119))
    print("reshape")
    print(reshaped)
    print("wrapper & checker")
    disease_wrapper,checker=wrapper(reshaped)
    print(disease_wrapper,checker)
    if(checker > 2):  
        y_pred = model.predict(reshaped)
        print("y_pred")
        print(y_pred)
        # Converting predictions to label

        # pred = list()
        # for i in range(len(y_pred)):
        #     pred.append(np.argmax(y_pred[i]))
        # print(pred)

        max_disease=np.argmax(y_pred[0])
        disease = disease_name[max_disease]
    
        disease1="'"+disease+"'"
    else:
        disease1 = "'"+disease_wrapper+"'"
        disease =  disease_wrapper
    print(disease1)
    if request.method == 'POST':
      result = request.form.to_dict(flat=False)
    cur = conn.cursor()
    result1=result['symptomsCheckboxGroup']
    #return render_template('DiagnosedDisease.html', prediction_text='Predicted disease is :{}'.format(disease))
    s="SELECT Description FROM diseases_data_base.diseaseinfo Where DiseaseName="+disease1+";"
    print(s)
    print(s)
    # conn.connnection.ping()  # reconnecting mysql
    
    cur.execute(s)
    Description = cur.fetchall()
    Description=Description[0][0]
    print(Description)
    cur.execute("SELECT DiseaseId FROM diseases_data_base.diseaseinfo Where DiseaseName="+disease1+";")
    DiseaseId = cur.fetchall()
    DiseaseId=DiseaseId[0][0]
    DiseaseId=str(DiseaseId)
    print(DiseaseId)
    DiseaseId1="'"+DiseaseId+"'"
    cur.execute("SELECT TreatmentDetails FROM diseases_data_base.treatment Where DiseaseId="+DiseaseId1+";")
    TreatmentDetails = cur.fetchall()
    TreatmentDetails=TreatmentDetails[0][0]
    cur.execute("SELECT TreatmentDetails FROM diseases_data_base.treatment Where DiseaseId="+DiseaseId1+";")
   
    # cur.execute(
    #  """INSERT INTO 
    #      diseases_data_base.new_table (
    #        symptoms, disease)
    # VALUES (%s,%s)""", (result1, disease))

    conn.commit()
    writer.writerow(symptoms_selected)
    disease_list=[]
   
    disease_list.append(disease)
    writer.writerow(disease_list)
    data_base.close()
    return render_template('DiagnosedDisease.html', prediction_text='{}'.format(disease),result = result1,Description=Description,TreatmentDetails=TreatmentDetails)

@app.route('/predictpet', methods=['POST'])
def predictpet():
    '''
    For rendering results on HTML GUI
    '''
    data_base_pet  = open('database_pet.csv', 'a')
    # ct stores current time
    writer_pet = csv.writer(data_base)
    print(request.form.getlist('symptomsCheckboxGroup'))

    symptoms_selected = []
    for x in request.form.getlist('symptomsCheckboxGroup'):
        symptoms_selected.append(x)
    print(symptoms_selected)

    listofzeros = [0] * 76
    for j in symptoms_selected:
        listofzeros[list_symptoms_pet.index(j)] = 1
    is_all_zero = np.all((listofzeros == 0))
    if is_all_zero:
        return "Please select symptoms"

    listofzeros_np = np.array(listofzeros)
    print(listofzeros_np)
    reshaped = listofzeros_np.reshape((1, 76))
    y_pred = model_pet.predict(reshaped)
    print(y_pred)
    # Converting predictions to label

    # pred = list()
    # for i in range(len(y_pred)):
    #     pred.append(np.argmax(y_pred[i]))
    # print(pred)

    max_disease=np.argmax(y_pred[0])
    disease = disease_name_pet[max_disease]
    cur = conn.cursor()
    disease1="'"+disease+"'"
    print(disease1)
    if request.method == 'POST':
      result = request.form.to_dict(flat=False)
   
    result1=result['symptomsCheckboxGroup']
    #return render_template('DiagnosedDisease.html', prediction_text='Predicted disease is :{}'.format(disease))
    s="SELECT Description FROM diseases_data_base.diseaseinfo Where DiseaseName="+disease1+";"
    print(s)
    print(s)
    cur.execute(s)
    Description = cur.fetchall()
    Description=Description[0][0]
    print(Description)
    cur.execute("SELECT DiseaseId FROM diseases_data_base.diseaseinfo Where DiseaseName="+disease1+";")
    DiseaseId = cur.fetchall()
    DiseaseId=DiseaseId[0][0]
    DiseaseId=str(DiseaseId)
    print(DiseaseId)
    DiseaseId1="'"+DiseaseId+"'"
    cur.execute("SELECT TreatmentDetails FROM diseases_data_base.treatment Where DiseaseId="+DiseaseId1+";")
    TreatmentDetails = cur.fetchall()
    TreatmentDetails=TreatmentDetails[0][0]
    cur.execute("SELECT TreatmentDetails FROM diseases_data_base.treatment Where DiseaseId="+DiseaseId1+";")
   
    # cur.execute(
    #  """INSERT INTO 
    #      diseases_data_base.new_table (
    #        symptoms, disease)
    # VALUES (%s,%s)""", (result1, disease))

    conn.commit()
    writer_pet.writerow(symptoms_selected)
    disease_list=[]
   
    disease_list.append(disease)
    writer_pet.writerow(disease_list)
    data_base_pet.close()
    return render_template('DiagnosedDisease.html', prediction_text='{}'.format(disease),result = result1,Description=Description,TreatmentDetails=TreatmentDetails)














####### Poultry Part ######################
@app.route('/Merimurghi')
def Merimurghi():
    return render_template('Merimurghi.html')

@app.route("/predict_poultry", methods = ['GET','POST'])
def predict_poultry():
    
    if request.method == 'POST':
        
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(r"D:/Poultry_data_set_from_server/", filename)                       #slashes should be handeled properly
        file.save(file_path)
        print(filename)
        product = poultry_prediction(file_path)
        print(product)
        file_path="health.jpg"
        
    return render_template('predict_poultry.html', product = product, user_image = file_path)  



####### end Poultry Part #################





# Wrap Flask app with Talisman
# Talisman(app, content_security_policy=None)
if __name__ == "__main__": 
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
