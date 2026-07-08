import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Retail Demand Forecasting Dashboard")

import pandas as pd

## load the forecast file
forecast = pd.read_csv("sales_forecast.csv")

##Add subheading 
st.subheader("Sales Forecast Data")

## Display the forecast table 
st.dataframe(
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
)

##Plot Forecast
st.subheader("30-Day Sales Forecast")

##Create The forecast chart
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(pd.to_datetime(forecast['ds']),forecast['yhat'])

ax.set_title("30-Day Sales Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Predicted Sales (Units Sold)")

st.pyplot(fig)

##Add chart caption
st.caption(
    "Figure 1: 30-Day sales forecast generated using the Prophet model. "
    "X-axis: Date | Y-axis: Predicted Sales (Units Sold)"
)




