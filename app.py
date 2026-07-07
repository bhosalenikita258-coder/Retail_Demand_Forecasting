import streamlit as st

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