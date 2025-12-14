import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Weather vs Food Orders Dashboard")

weather = pd.read_csv("data/weather.csv")
orders = pd.read_csv("data/orders.csv")

data = pd.merge(weather, orders, on="date")

st.subheader("Merged Data")
st.dataframe(data)

st.subheader("Orders on Rainy vs Non-Rainy Days")
rain_orders = data.groupby("rain")["orders"].mean()

fig, ax = plt.subplots()
rain_orders.plot(kind="bar", ax=ax)
st.pyplot(fig)
