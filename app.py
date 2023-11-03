from flask import Flask,request,jsonify
from Services import *
from utils import get_module_logger
from predictionServices import *

app=Flask(__name__)

@app.route("/predict",methods=['GET','POST'])
def predictquantity():
    clireq=request.get_json()
    return jsonify (list(predictions(clireq['date'])))

if(__name__)=="__main__":
    app.run(port=8080,debug=True)