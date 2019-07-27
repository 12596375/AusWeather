# AusWeather

## Overview of the Project

The main objective of this project is to predict with past and current day weather data on whether or not if it will rain the next day. RainTomorrow will be the binary dependent variable which translates 0 as no rain and 1 as rain. This means that this task will require a  classification predictive model to predict the dependent variable. Independent variables such as date, location, temperatures, clouds, rainfall and humidity will be used to help the model predict the dependent variable. Feature engineering and selection will be used to ensure that all appropriate data is used for the predictive model. Also as there is many outliers, outlier handling technique will be considered to ensure a more even distribution if a classifier used can not handle outlier detection well. There is also many different units measured such as temperature and rainfall mm. A standard scalar will be considered to ensure that everything will be in a similar metric to ensure no confusion to the predictive model.

## Packages to Install

Aside from the standard packages of Pandas, Numpy, SKlearn and Matplotlib, external packages such as missingno and xgboost will need to be installed if you are attempting to run this on your own machine or AWS Sagemaker. If you are using AWS Sagemaker, changed the python3 to whatever notebook style you are using. 

Using conda terminal:
* AWS: conda install -n python3 -c conda-forge missingno
* jupyter: conda install -c conda-forge missingno
* AWS: conda install -n python3 -c conda-forge xgboost
* jupyter: conda install -c conda-forge xgboost
  
## Whats in the Repo?
  
There will be a data folder which will contain the base dataset (AusWeather) without any changes and my attempt to fill and complete the dataset(AusWeaterReady). There will be two notebooks, Ausweather and AusWeather-modelling which corresponding to my initial data exploration and cleaning and the other will be my attempt to create a predictive model to predict the classifiers.

## Todo list:

Todo:
- [x] Understand the data
- [x] Impute missing values
- [x] One hot encode the location
- [x] Feature Engineer from date for Seasons
- [ ] Use a Standard scalar
- [x] Choose two baseline models
- [x] RFE with those baseline models
- [x] Create baseline models
- [x] Determine the Accuracy through Recall and Precision report
- [ ] 10-fold cross validation to ensure no overfitting
- [ ] Fine tune the models for better results
- [ ] Visualise the results with D3JS 
- [ ] Host the results on Github pages
- [ ] Finalise a report detailing the process and findings
- [ ] Code Refactoring
