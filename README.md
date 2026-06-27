# Retail Demand Forecasting

## Project Overview

Retail Demand Forecasting is a data analysis project that explores historical retail sales data to understand sales patterns, product demand, pricing trends, and calendar-based events. The project performs Exploratory Data Analysis (EDA) to identify insights that can support future demand forecasting.

## Objectives

Load and analyze retail sales datasets
Perform data cleaning and preprocessing
Explore dataset structure and statisics
Identify missing and duplicate values
Analyze demand patterns using visualizations
Prepare the dataset for future forecasting models


## Dataset

The project uses three datasets:

  - calendar.csv – Calendar dates and event information

  - sales_train_validation.csv – Historical sales data

  - sell_prices.csv – Product selling prices

https://www.kaggle.com/competitions/m5-forecasting-accuracy/data
---

## Technologies Used

   - Python
 
   - Pandas

   - NumPy

   - Matplotlib

## Exploratory Data Analysis

   - The following analyses were performed:

        - Dataset loading

        - Dataset shape and information

        - Missing value analysis
          
        -  Duplicate value checking
          
        -  Statistical summary
          
        -  Date conversion
        
        -  Monthly sales distribution
        
        -  Weekday distribution
          
        -  Event type distribution
          
        -  Product price distribution
          
        -  Highest and lowest selling prices
          
        -  Store-wise distribution
          
        -  Product category distribution

        - State-wise product distribution
    
        - Average selling price by store
    
        - Average selling price by state
    
        - Sample Daily Sales
    
        - Top Selling Products 

## Key Insights

   - Examined the structure and quality of retail datasets

   - Identified missing values and duplicates
  
   - Visualized monthly and weekday demand trends

   - Analyzed event-based sales distribution

   - Studied product pricing patterns

   - Compared store-wise and category-wise distributions

   - Examined product distribution by category and state

## Future Work
  
  - Feature Engineering

  - Time Series Forecasting

  - Machine Learning Models (XGBoost, Random Forest)

  - Deep Learning (LSTM)

  - Model Evaluation and Performance Comparison

## Project Structure

Retail_Demand_Forecasting/
│

├── Retail_Demand_Forecasting.ipynb

├── calendar.csv

├── sales_train_validation.csv

├── sell_prices.csv

└── README.md
# Week 2: Data Transformation

## Objective

The objective of Week 2 is to transform the raw M5 Forecasting dataset into clean, structured datasets suitable for demand forecasting models.

## Tasks Completed

### 1. Sales Data Transformation
- Converted the sales dataset from wide format to long format using the `melt()` function.
- Structured the data for easier analysis and forecasting.

### 2. Calendar Data Integration
- Merged the transformed sales dataset with the calendar dataset.
- Added date-related features such as:
  - Date
  - Weekday
  - Month
  - Year
  - Event information

### 3. Price Data Integration
- Merged sales data with the sell prices dataset.
- Linked product prices using `store_id`, `item_id`, and `wm_yr_wk`.

### 4. Data Cleaning
- Checked for missing values after merging.
- Filled missing selling prices using the median value.
- Verified data consistency for further analysis.

### 5. Data Aggregation
- Aggregated daily sales into:
  - Weekly sales
  - Monthly sales
- Prepared datasets for forecasting models.

### 6. Output Files
Generated:
- `clean_analytical_dataset.csv`
- `weekly_sales.csv`
- `monthly_sales.csv`

## Technologies Used

- Python
- Pandas
- Jupyter Notebook


