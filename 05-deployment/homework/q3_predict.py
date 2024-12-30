import pickle
from flask import request
import warnings
warnings.filterwarnings("ignore")

def predict(dv, model, customer):
    # customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5
    
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    
    return result

if __name__ == '__main__':
    model_file = 'model1.bin'
    dv_file = 'dv.bin'

    customer = { "job": "management", 
                "duration": 400, 
                "poutcome": "success"
            }

    with open(model_file, 'rb') as f_in: 
        model = pickle.load(f_in)

    with open(dv_file, 'rb') as f_in: 
        dv = pickle.load(f_in)
    
    result = predict(dv, model, customer)
    print(result)