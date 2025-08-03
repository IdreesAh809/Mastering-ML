import requests

url = 'http://127.0.0.1:5000/predict'

data = {
    "experience": 2,
    "test_score": 7,
    "interview_score": 9
}

response = requests.post(url, json=data)
print("Response:", response.json())
