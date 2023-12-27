# running our trained model as API using html
# run "python app.py" in the terminal to run the model 

from flask import Flask,request,url_for,render_template
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_features=[np.array(data)]
    output=model.predict(final_features)[0]
    print(output)

    return render_template('home.html',prediction_text="The Profit is {}".format(round(output,2)))


if __name__=="__main__":
    app.run(debug=True)