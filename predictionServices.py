import joblib,pandas as pd ,numpy as np
#from utils import get_module_logger
from tensorflow import keras

# logger=get_module_logger(__name__)

lstmmodel=joblib.load(r"C:\Flask\Third_Project\model_data.joblib")
scalermodel=joblib.load(r"C:\Flask\Third_Project\scaler.joblib")

df=pd.read_csv("C:\Flask\Order_Quantity.csv")



def predictions(date):
    # print(lstmmodel)
    df['Date']=pd.to_datetime(df['Date'])
    date=pd.to_datetime(date)
    ind=int(df[df["Date"]==date].index[0])
    print("Index working",ind)
    #df2=df[ind-2:ind-1]
    df2=df[ind-1:ind]
    prediction=lstmmodel.predict(np.array(df2['Order_Quantity']).reshape(-1,1))
    print(prediction)
    result=scalermodel.inverse_transform(prediction)
    return result
    

    

# if(__name__)=="__main__":
#     predictions("2011-01-02")
