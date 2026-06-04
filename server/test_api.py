import requests

# The URL of your local Flask server
url = 'http://127.0.0.1:5000/predict_insurance_charges'

# The data you want to test (matches the request.form in server.py)
data = {
    'age': 28,
    'sex': 'male',
    'bmi': 31.5,
    'children': 2,
    'smoker': 'yes',
    'region': 'southeast'
}

# Sending the POST request
try:
    response = requests.post(url, data=data)
    
    # Print the result
    if response.status_code == 200:
        print("Success!")
        print("Estimated Charges:", response.json()['estimated_charges'])
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Error details:", response.text)

except Exception as e:
    print(f"Could not connect to the server: {e}")