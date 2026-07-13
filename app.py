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

st.subheader("Sales Summary")

##Calculate summary statistics 
total_sales = forecast['yhat'].sum()
average_sales = forecast['yhat'].mean()
max_sales = forecast['yhat'].max()
min_sales = forecast['yhat'].min()

##Display statistics 
st.write(f"**Total Forecasted Sales:** {total_sales:.2f}")
st.write(f"**Average Predicted Sales:** {average_sales:.2f}")
st.write(f"**Maximum Predicted Sales:** {max_sales:.2f}")
st.write(f"**Minimum Predicted Sales:** {min_sales:.2f}")

st.info(
    "The summary statistics provide a quick overview of the predicted "
    "sales over the next 30 days and help understand the overall demand trend."
)

st.subheader("Inventory Recommendation")

##Add Recommendation Logic
if average_sales > 0:
    st.success("Demand is expected to remain stable. Maintain sufficient inventory to avoid stock shortages.")
else:
    st.warning(
        "Demand is predicted to be low. Review inventory levels before placing new orders."
    )

##Add a note
if average_sales > 0:
    st.success(
        "Demand is expected to remain stable. Maintain sufficient inventory to avoid stock shortages."
    )
else:
    st.warning("Demand is predicted to be low. Review inventory levels before placing new orders.")

##Dataset information 
st.subheader("Dataset Information")

st.write("**Dataset:** M5 Forecasting Dataset")
st.write(f"**Forecast Records:** {len(forecast)}")
st.write("**Forecast Horizon:** 30 Days")
st.write("**Domain:** Retail Sales Forecasting")

st.subheader("Model Information")

st.write("**Model:** Facebook Prophet")
st.write("**Algorithm Type:** Time Series Forecasting")
st.write("**Input:** Historical Retail Sales Data")
st.write("**Output:** 30-Day Sales Forecast")
st.write("**Purpose:** Forecast future product demand to support inventory planning and business decision-making.") 

st.markdown("---")
st.caption("Retail Demand Forecasting Dashboard | Developed using Python, Streamlit, and Facebook Prophet")
    


