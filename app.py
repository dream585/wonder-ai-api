from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
#model = joblib.load('model.pkl')

CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    profile = data['profile']

    # This is a mock prediction for demonstration purposes
    if "software engineer" in profile and "AI and machine learning" in profile:
        prediction = "Based on your profile, you are best suited for a role as a Full Stack Developer specializing in AI and machine learning projects."
    else:
        prediction = "Based on your profile, we recommend exploring opportunities in web development."

    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run(debug=True)