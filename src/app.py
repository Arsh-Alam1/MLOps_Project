from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
import numpy as np

app = Flask(__name__)

# Dummy model
model = LogisticRegression()
X_train = np.array([[0], [1], [2], [3]])
y_train = np.array([0, 0, 1, 1])
model.fit(X_train, y_train)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    prediction = model.predict([data["features"]])
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
