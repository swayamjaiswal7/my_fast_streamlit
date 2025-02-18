import streamlit as st
import pandas as pd

st.write("Here's a overview of the Automobile datasets")
df=pd.read_csv('Automobile.csv')
st.table(df)
st.write("Here is a scatter plot showing linear relationship between length of the car vs car mileage")
st.scatter_chart(df,x='length',y='mileage',color='company')
st.write("Here we can see a positive correlation between mileage and length of car and it is colored in different car companies")
