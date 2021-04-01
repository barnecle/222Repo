from flask import Flask
from flask import jsonify
import connexion
from joblib import load

#load the model

#my_model = load('mush_model.pkl')

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("E222-SP21-Mushroom_ML.yaml-1.0-swagger.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Use routes to use machine :)"}
    return jsonify(msg)
@app.route("/test")
def test():
    msg = {"msg": "testing!"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
