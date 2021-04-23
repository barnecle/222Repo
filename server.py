from flask import Flask, render_template
from flask import jsonify
import connexion
from joblib import load
import os
#load the model

#my_model = load('mush_model.pkl')

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("Mushroom_ML.yaml")

UPLOAD_FOLDER = "."
# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Use routes to use machine :)"}
    return jsonify(msg)
@app.route("/test")
def test():
    msg = {"msg": "testing!"}
    return jsonify(msg)

@app.route("/model-tree")
def model_tree():
    filename = 'fig1.jpg'
    full_filename = os.path.join(UPLOAD_FOLDER, filename)
    return render_template("index.html", user_image = full_filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
