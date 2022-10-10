import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


@app.route('/api',methods=['POST'])
def predict():

    # Get the data from the POST request
    data = request.json 

    # Convert dict to list and array
    dataL = list(data.values())
    dataArr = np.array(dataL).reshape(1, -1)
    
    # Predict the result
    output = model.predict(dataArr)
    
    if(output[0] == 1):
        return jsonify("Canceled")
    else:
        return jsonify("Not Canceled")
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)

