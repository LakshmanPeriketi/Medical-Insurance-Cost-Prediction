import json
import pickle
import joblib 
import numpy as np
import pandas as pd

__model=None
__Loc=None
__gender=None
__Smoker=None
sex_le=None
smoker_le=None
region_le=None


def predict_insurance_charges(age, sex, bmi, children, smoker, region):
    # 1. Transform categorical strings to labels using your trained encoders
    # Assuming le_sex, le_smoker, and le_region were saved from your training
    sex_encoded = sex_le.transform([sex.lower()])[0]
    smoker_encoded = smoker_le.transform([smoker.lower()])[0]
    region_encoded = region_le.transform([region.lower()])[0]
    
    # 2. Arrange features in the EXACT order used during model.fit()
    # Typical order: [age, sex, bmi, children, smoker, region]
    #features = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

    # 3. Predict
    #prediction = model.predict(features)
    #prediction = __model.predict(features)[0]    
    cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    features_df = pd.DataFrame([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]], columns=cols)

    prediction = __model.predict(features_df)[0]
    

    return round(float(prediction), 2)    

def get_loc():
    return __Loc
def get_gender():
    return __gender
def get_smoker():
    return __Smoker

def load_artifacts():
    print("Start Loading Artifacts...")
    global __gender, __Smoker, __Loc, __model,sex_le,region_le,smoker_le
    __gender=["male","female"]
    __Smoker=["yes","no"]
    __Loc=["southeast","southwest","northeast","northwest"]
    with open('./artifacts/insurance.pickle','rb') as f:
        __model=pickle.load(f)
    sex_le = joblib.load('./artifacts/sex_le.pkl')
    smoker_le = joblib.load('./artifacts/smoker_le.pkl')
    region_le = joblib.load('./artifacts/region_le.pkl')

    print("Successfully Loaded Artifacts")

if __name__=="__main__":
    load_artifacts()
    #print(get_loc())
    #print(get_gender())
    #print(get_smoker())
    #print(predict_insurance_charges(27,"male",30.66,3,"no","southeast"))
    #print(predict_insurance_charges(19,"male",78.24,2,"yes","northwest"))
    #print(predict_insurance_charges(31,"female",18.47,0,"yes","northeast"))
    #print(predict_insurance_charges(74,"male",27.5,1,"no","southwest"))
    #print(predict_insurance_charges(45,"female",10.83,0,"no","northeast"))




