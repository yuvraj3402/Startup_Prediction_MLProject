# running our trained model as API using streamlit
# run "streamlit run app2.py" in the terminal to run the model 

import streamlit as st
import pickle
import numpy as np


st.title("Startup Profit Prediction")
def predict(data):
    model=pickle.load(open('model.pkl','rb'))
    return model.predict(data)


col1,col2,col3,col4,col5=st.columns(5)
with col1:
    RaD_speed = st.number_input('R&D Spend')
with col2:
    int_admnistration = st.number_input('intAdministration')
with col3:
    Marketing_spend= st.number_input('Marketing Spend')
with col4:
    florida= st.number_input('Florida',0,1)
with col5:
    new_york= st.number_input('New-York',0,1)


if st.button("Predict Your Profit"):
    result =predict(np.array([[RaD_speed,int_admnistration,Marketing_spend,florida,new_york]]))
    st.text(result[0])
