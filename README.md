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

## Data Transformation
   
   - Sales Data Transformation
   
   - Calendar Data Integration

   - Checked Dataset

   - Checked Missing Values

   - Handling Missing Values

   - Create Features

   - Revenue

   - Weekly Sales

   - Monthly Sales

## Time Series Forecasting

   - Imported Important Libraries

   - Creadted Daily Sales Dataset

 1. Rename Columns for Prophet

 Prophet requires the input dataset to have two specific column names:

 ds – Date column
 y – Target variable (Sales)

 The existing dataset was modified by renaming:

 date → ds
 sales → y

 This ensures compatibility with the Prophet forecasting model.

 2. Create and Train the Prophet Model

 A Prophet model was initialized using the default configuration and trained on the prepared dataset. During training, the model learns historical sales            patterns, trends, and seasonality, which will be used to generate future sales forecasts in the subsequent steps.
     
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

## Feature Engineering

Date-Based Feature Engineering

To improve the predictive performance of the demand forecasting model, additional time-based features were extracted from the date column. These features enable the model to capture seasonal, monthly, weekly, and daily demand patterns.

Features Created:

Year: Extracted the year from the transaction date.

Month: Extracted the month (1–12).

Day: Extracted the day of the month.

Week: Extracted the ISO week number of the year.

Weekday: Extracted the day name (Monday–Sunday).

Outcome

Successfully generated temporal features from the date column.
Enhanced the dataset with time-aware attributes for demand forecasting.
Prepared the data for subsequent preprocessing, exploratory data analysis, and machine learning model development. 

### Monthly Sales Aggregation

To analyze sales trends over time, the dataset was grouped by **Year** and **Month** to calculate the total monthly sales.

This aggregated dataset helps identify monthly sales patterns and serves as a foundation for further exploratory data analysis and forecasting.



### Export Processed Dataset

After preprocessing and feature engineering, the final dataset was exported for use in subsequent analysis and machine learning tasks.

This saves the cleaned dataset as **`processed_data.csv`** while excluding the DataFrame index.

