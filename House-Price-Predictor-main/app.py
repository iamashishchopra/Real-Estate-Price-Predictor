from flask import Flask, request, jsonify
import util as util
app=Flask(__name__)

@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    print("Starting Python Flask Server for House Price Prediction...")
    util.load_saved_artifacts()
    response=jsonify({
        "locations":util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    print("Starting Python Flask Server for House Price Prediction...")
    util.load_saved_artifacts()
    total_sqft=float(request.form['total_sqft'])
    location=request.form["location"]
    bhk=int(request.form["bhk"])
    bath=int(request.form["bath"])

    response=jsonify({
        "estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response



    
