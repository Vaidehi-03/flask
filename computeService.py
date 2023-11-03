import numpy as np
from flask import request

def get_Mean_Max():
    data=request.get_json()

    newdata=np.array(data['data'])
    return  ({'mean':int(np.mean(newdata)),'max':int(np.max(newdata))})