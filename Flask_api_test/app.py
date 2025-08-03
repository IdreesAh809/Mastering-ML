import joblib
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)
model = joblib.load('salary_prediction_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
            experience = float(data['experience'])
            test_score = float(data['test_score'])
            interview_score = float(data['interview_score'])
        else:
            # Fallback for form submission from web UI
            experience = float(request.form['experience'])
            test_score = float(request.form['test_score'])
            interview_score = float(request.form['interview_score'])

        prediction = model.predict(np.array([[experience, test_score, interview_score]]))
        return jsonify({'predicted_salary': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
