from flask import Flask,jsonify,request
import util
app=Flask(__name__)
@app.route('/get_dropdown_values', methods=['GET'])
def get_dropdown_values():
    response = jsonify({
        'gender': util.get_gender(),
        'smoker': util.get_smoker(),
        'location': util.get_loc()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_insurance_charges', methods=['POST'])
def predict_charges():
    # Extracting data from the request form
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']

    # Call the utility function
    estimated_charges = util.predict_insurance_charges(age, sex, bmi, children, smoker, region)

    response = jsonify({
        'estimated_charges': estimated_charges
    })
    
    # Adding CORS header so your frontend can talk to the server
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response
if(__name__=="__main__"):
    print("Server Started Medical Insurance Prediction")
    util.load_artifacts()
    app.run()