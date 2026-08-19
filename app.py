import streamlit as st
import pickle
import numpy as np
import plotly.express as px


model=pickle.load(open("health_risk_predictor.pkl","rb"))


encoders=pickle.load(open("label_encoders.pkl","rb"))

st.title("Health Risk Predictor")
age=st.slider("Age",18,80,22)
diet=st.selectbox("Diet Quality",['Poor','Average','Good'])
exercise=st.slider("Exercise day per week",0,7,3)
sleep=st.slider("sleep Hours",3,12,6)
stress=st.selectbox("stress level",['Low','Medium','High'])
bmi=st.number_input("BMI",10.0,40.0,22.0)
smoking=st.selectbox("smoking",["Yes","No"])
alcohol=st.selectbox("Alocohol consumption",['Low','Medium','High'])
family_history=st.selectbox("Family History of disease" ,["Yes","No"])


if st.button("predict Risk"):

    input_data=[age,
                encoders['diet'].transform([diet])[0],
                exercise,
                sleep,
                encoders['stress'].transform([stress])[0],
                bmi,
                encoders['smoking'].transform([smoking])[0],
                encoders['alcohol'].transform([alcohol])[0],
                encoders['family_history'].transform([family_history])[0],
                ]
    prediction=model.predict([input_data])
    probs=model.predict([input_data])

    risk_label=encoders['risk_level'].inverse_transform([prediction[0]])[0]

    st.success(risk_label)


    #barchart for lifestyle factors

    factors={
        "Diet":encoders['diet'].transform([diet])[0] + 1,
        "Exercise":exercise,
        "Sleep":sleep,
        "Stress":encoders['stress'].transform([stress])[0]+ 1,
        "BMI":bmi
           
    }

    bar_fig=px.bar(
        x=list(factors.keys()),
        y=list(factors.values()),
        labels={"x":"Factors","y":"value"},
        title="your Lifestyle Factors"
    )
    st.plotly_chart(bar_fig)

