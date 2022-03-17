# NYC 311 Complaint Type Prediction - Hardik Nahata

## About/Overview

311 is a service that New York City residents can use to make non-emergency reports to the city for things like noise complaints, graffiti, potholes, etc. Each complaint that comes into the city is registered, along with additional information like the location, the neighborhood, the agency that responded to the request, etc.
The 311 dataset has about 40 columns and around 21 Million Rows.

## Objectives Accomplished
I have successfully attempted the following objectives of the problem statement provided by Ezoic:
- Challenge 1 : Question 1 : How many incidents were opened in each year (beginning with 2010)?
- Challenge 1 : Question 2 : Which borough has the most incidents?
- Challenge 2 : Complaint Type Prediction given the Complaint Description.
- Extra Challenge: Deployed the model on the Cloud with Streamlit. (Link Provided)

## Note
Please use Google Collab to open the Jupyter Notebooks (IPYNB files) for best experience and formatting.

## Description of the repository
This repository contains the following two folders:
- **Challenge 1** : contains Data Exploration and Analysis
- **Challenge 2** : contains notebooks for Data Wrangling, Data Cleaning and Model Training.
=- **Model Deployment** : contains files for model deployment


## Challenge 1 File Descriptions

1. **Challenge-One-Question-1**:
		This Notebook queries data from the RedShift Database and shows the code and visualization to find how many incidents were opened in each year (beginning with 2010)?

2. **Challenge-One-Question-2**:
		This Notebook queries data from the RedShift Database and shows the code and visualization to find which borough has the most incidents?

## Challenge 2 File Descriptions

1. **Challenge-Two-Data-Filtering**:
		This Notebook queries data from the RedShift Database and filters it to retrieve the data required to solve the problem of complaint type prediction.
		
2. **Challenge-Two-Data-Preprocessing-1**:
		This Notebook works on the dataframe created in the previous notebook and applies Data Preprocessing techniques to clean and transform the data for model training.	

3. **Challenge-Two-Data-Preprocessing-2**:
		This Notebook works on the dataframe created in the previous notebook and applies Data Preprocessing techniques to hande the class imbalance found in the data.

4. **Challenge-Two-Traditional-ML-Class-Imbalance**:
		This Notebook works on the dataframe which contains the data **with class imbalance**.  
		I have applied Traditional Machine Learning Algorithms for Complaint Prediction:
		- Random Forest
		- Logistic Regression
		- Multinomial Naive Bayes 
		- Linear SVC
	
5. **Challenge-Two-Traditional-ML-Class-Balanced**:
	    This Notebook works on the dataframe which contains the data **with class balance**. 
	    I have applied Traditional Machine Learning Algorithms for Complaint Prediction:
		- Random Forest
		- Logistic Regression
		- Multinomial Naive Bayes 
		- Linear SVC
		
		* The reason to train/test with class balanced & imbalanced data was to show the improve in performance.  

6. **Challenge-Two-Transformers**:
	    I have trained the RoBERTa Transformer Model on the dataset.

7. **Challenge-Two-AutoNLP-HuggingFace**:
	    I have explored AutoNLP by HuggingFace to train on the dataset.

## Model Deployment File Descriptions

- As per the problem statement, we had an option to create an interactive application.
- I had decided to **deploy** my best model for complaint prediction on the Cloud.
- I have also attached the code used to deploy in this folder. 
- I have used the Streamlit library for deployment.
- The **link** to the deployed model is below:
   https://share.streamlit.io/hardiknahata/nyc311-complaint-type-prediction/main/predict.py
	    
## Assumptions
- I have assumed that the complaint type relies on the description of the complaint only.
- I have assumed and merged similar complaint types. The reasoning is provided in the notebooks.

## Limitations
- The models have been trained to predict the top 100 type of complaints.

## Future Scope
- Model performance can be improved by hyperparameter tuning and experimentation.
- Hyperparameter tuning can be applied with libraries such as GridSearchCV and Optuna.
- Different Transformer architectures can be tried out on the dataset.
- More predictive models can be built on the data. The data is huge and a lot of interesting stuff can be done. 

## Citations
- Google
- Machine Learning Mastery
- Analytics Vidhya


# Deployed on Cloud:
https://share.streamlit.io/hardiknahata/nyc311-complaint-type-prediction/main/predict.py


# How to Run Locally
Install required libaries by running:  
`pip install -r requirements.txt`

Command to launch StreamLit App on local browser:  
`streamlit run predict.py`


