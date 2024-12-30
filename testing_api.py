import requests

url = "https://wandering-ronnica-mohi-23841afe.koyeb.app/predict"

data = {
    "Age": 25,
    "Source of Income": "Self Employed",
    "No of Dependents": 3,
    "Annual Income": 10000,
    "Credit Score": 200,
    "DTI": 0.18,
    "Purpose": "Personal"
}

response = requests.post(url, json=data)
print(response.json())
