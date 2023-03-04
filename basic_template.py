import streamlit as st 
import numpy as np
from matplotlib import pyplot as plt 
import pandas as pd 
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression



data = pd.read_csv("salary.csv")

x= np.array(data["YearsExperience"]).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data["Salary"]))



st.title("Salary Predictor")
nav = st.sidebar.radio("Navigator",["Home","Prediction","Contribute"])

if nav == "Home" :
    st.image("salary1.jpg",width=800)
    if st.checkbox("show table"):
        st.table(data)

    graph = st.selectbox("what kind of graph ? ",["Non-Interactive","Interative"])
    
    val = st.slider("filter data using ",0,20)
    data = data.loc[data["YearsExperience"]>=val]
    if graph == "Non-Interactive":
       plt.figure(figsize=(20,15))
       plt.scatter(data["YearsExperience"],data["Salary"])
       plt.ylim(0) 
       plt.xlabel("YearsExperience")
       plt.ylabel("Salary")
       plt.tight_layout()
       st.pyplot()
    if graph == "Interative":
        layout = go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range=[0,21000000])
        ) 
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode="markers"),layout = layout)
        st.plotly_chart(fig)


if nav == "Prediction":
    st.header("know your Salary ")
    val = st.number_input("Enter your exp",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]
    
    if st.button("predict"):
        st.success(f"your predicted Salary is {round(pred)}")
    


if nav == "Contribute":
    st.header("contribute to ou data set")
    ex = st.number_input("enter your experience",0.0,20.0)

    sal = st.number_input("Enter your Salary",0.00,10000000.00,step = 1000.0)
    if st.button("Submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("salary.csv",mode='a',header=False,index=False)
        st.success("submited")
