from flask import Flask,request,jsonify
from constraints_1 import DATA_FILE_PATH
import logging
import Services.Load_service as DataLoader
import utils
logger = utils.get_module_logger



app=Flask(__name__)

@app.route("/getDataBetween", methods=["GET","POST"])
def get_data_between():
    logger.info("API request is  initiated with the endpoint :-",str(request.endpoint()))
    client_request=request.get_json
    logger.info(str(client_request))

    result=DataLoader.data_processing(client_request["startDt"],client_request["endDt"])
    return jsonify(result)


if __name__=="__main__":
    app.run(port=8080,debug=True)