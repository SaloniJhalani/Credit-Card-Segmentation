# Credit Card Segmentation

## Table of Contents
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Website Link](#website-link)
- [Implementation Details](#implementation-details)
    - [Methods Used](#methods-used)
    - [Technologies](#technologies)
    - [Python Packages Used](#python-packages-used)
- [Steps Followed](#steps-followed)
- [Results and Evaluation Criterion](#results-and-evaluation-criterion)
- [Future Improvements](#future-improvements)

## Project Overview
This project aims to develop a machine learning model to predict bank customer churn. Customer churn, also known as customer attrition, refers to the phenomenon where customers stop doing business with a company or switch to a competitor. By identifying potential churners in advance, banks can take proactive measures to retain valuable customers and minimize revenue loss. This repository provides a comprehensive solution for predicting customer churn using various machine learning algorithms.

## Data Source
The dataset used for this project can be obtained from [here](https://www.kaggle.com/datasets/adammaus/predicting-churn-for-bank-customers).

The dataset summarizes the usage behavior of about 9000 active credit card holders for 6 months. 

## Website Link

A web-based demonstration of this project can be accessed [here](https://bank-customer-churn-prediction.streamlit.app).

## Implementation Details

### Methods Used
* Machine Learning - Unsupervised
* Data Visualization
* Customer Segmentation

### Technologies
* Python
* Jupyter
* streamlit

### Python Packages Used
* Data Manipulation: Pandas, numpy
* Data Visualization: seaborn, matplotlib
* Machine Learning: scikit
  
## Steps Followed

1. **Data collection**: Obtained the customer credit card dataset from Source Dataset Link.
2. **Data Preprocessing**: Cleansed the data, handled skweness in the data and performed the dimenstioalty reduction.
4. **Model Development**: Traied the model using KMeans with different number of clusters. 
5. **Model Evaluation**: Find the best number of cluster is 4 using elbown technique. 
6. **Deployment**: The Credit Card Segmentation model is deployed as a standalone application. This enables users to interact with the model and visualize the data based on the identified clusters. The deployed app provides an intuitive interface with features such as column distribution analysis, scatter plots showcasing relationships between variables, and dropdown fields for selecting specific values.

## Results and Evaluation Criterion

Based on the evaluation results, the best-performing model was **XGBoost** which achieved an accuracy of 91% and F1-score of 91%. 

<img width="436" alt="Screenshot 2023-06-27 at 4 15 32 PM" src="https://github.com/SaloniJhalani/Bank-Customer-Churn-Prediction/assets/33859675/4d273530-aa25-443c-93d6-33d6d3904de4">

## Future Improvements

Here are some potential areas for future improvements in the project:

* Feature engineering: Explore additional features that may capture customer behavior more accurately.
* Model optimization: Fine-tune the model parameters to potentially improve performance.
* Real-time monitoring: Implement a system to monitor and retrain the model periodically to adapt to changing customer dynamics.
* User interface enhancement: Improve the user interface of the deployed application for better user experience.






