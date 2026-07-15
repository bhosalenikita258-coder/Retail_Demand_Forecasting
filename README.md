# Retail Demand Forecasting

##  Project Overview
Retail Demand Forecasting is an end-to-end data analysis and time-series forecasting project that predicts future retail product demand using historical sales data. The project integrates data preprocessing, exploratory data analysis (EDA), feature engineering, forecasting with Facebook Prophet, and an interactive Streamlit dashboard to support inventory planning and business decision-making.

---

##  Objectives
- Load, clean, and preprocess historical retail datasets.
- Perform Exploratory Data Analysis (EDA) to identify sales patterns and trends.
- Engineer time-based features for forecasting.
- Build a Facebook Prophet model to forecast future sales.
- Develop an interactive Streamlit dashboard to visualize forecasts and insights.
- Support inventory planning through forecast-based recommendations.

---

##  Dataset Information

This project uses the **M5 Forecasting Accuracy** dataset from Kaggle, which consists of:

1. **calendar.csv** – Calendar information, holidays, and special events.
2. **sales_train_validation.csv** – Historical daily sales for products across stores.
3. **sell_prices.csv** – Weekly selling prices for each product.

https://www.kaggle.com/competitions/m5-forecasting-accuracy/data
---

##  Tech Stack

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Visualization:** Matplotlib
- **Forecasting Model:** Facebook Prophet
- **Dashboard:** Streamlit
- **Development Environment:** Jupyter Notebook

---

##  Project Workflow

### 1. Data Collection
- Load retail sales, calendar, and selling price datasets.

### 2. Data Preprocessing
- Handle missing values.
- Merge datasets.
- Convert date columns.
- Prepare data for forecasting.

### 3. Exploratory Data Analysis (EDA)
- Dataset overview
- Missing value analysis
- Month distribution
- Weekday distribution
- Event type distribution
- Selling price distribution
- Products by category
- Products by state
- Average selling price by store
- Average selling price by state
- Daily sales trend
- Top-selling products

### 4. Feature Engineering
- Create Year, Month, Day, Week, and Weekday features.
- Prepare data in Prophet format (`ds` and `y`).

### 5. Time Series Forecasting
- Train the Facebook Prophet model.
- Generate a 30-day sales forecast.
- Visualize forecast results.
- Analyze trend, weekly, and yearly seasonality.

### 6. Interactive Application (`app.py`)

A user-friendly Streamlit dashboard providing:

- Forecast data in tabular format.
- Interactive 30-day sales forecast visualization.
- Forecast confidence intervals (`yhat`, `yhat_lower`, `yhat_upper`).
- **Sales Summary** displaying:
  - Total Forecasted Sales
  - Average Predicted Sales
  - Maximum Predicted Sales
  - Minimum Predicted Sales
- Information box explaining the overall demand trend.
- **Inventory Recommendation** section providing inventory planning suggestions based on forecast results.
- Success or warning messages to support inventory management decisions.
- **Dataset Information** displaying:
  - Dataset Name
  - Forecast Records
  - Forecast Horizon
  - Domain
- **Model Information** displaying:
  - Model Name (Facebook Prophet)
  - Algorithm Type
  - Model Input
  - Model Output
  - Model Purpose
- Dashboard footer showing project information.

---

##  Repository Structure

```text
Retail_Demand_Forecasting/
├── Retail_Demand_Forecasting.ipynb
├── app.py
├── README.md
├── sales_forecast.csv
├── calendar.csv
├── sales_train_validation.csv
└── sell_prices.csv
```

---

##  Project Output

The project provides:

- Cleaned retail dataset
- Exploratory Data Analysis (EDA)
- 30-day sales forecast
- Forecast trend visualization
- Forecast component analysis
- Interactive Streamlit dashboard
- Sales summary statistics
- Inventory recommendations
- Dataset information
- Model information

---

##  How to Run

### Install Required Libraries

```bash
pip install pandas numpy matplotlib prophet streamlit
```

### Run the Streamlit Dashboard

```bash
streamlit run app.py
```

---
