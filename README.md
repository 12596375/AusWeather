# AusWeather

## Overview of the Project

The main objective of this project is to predict/forecast with past and current day weather data on whether or not if it will rain the next day. RainTomorrow will be the binary dependent variable which translates 0 as no rain and 1 as rain. This means that this task will require a  classification predictive model to predict the dependent variable. Independent variables such as date, location, temperatures, clouds, rainfall and humidity will be used to help the model predict the dependent variable. 

It is to be noted that this is a time-series dataset as for example, if it is winter then the nights will be the coldest and the afternoon will be the warmest and vice versa for summer. Essentially certain patterns will be derived from the certain time of the year, however it is possible for this to not be the case due to Australian Weather. It is possible that there could be a lack of rain due to global warming which could through off the patterns. 

The data cleaning section of the project will consist of dealing with the missing data and outliers. As there are many outliers, outlier handling technique will be considered to ensure a more even distribution if a classifier used can not handle outlier detection well. There is also many different units measured such as temperature, wind speed and rainfall mm. A standard scalar will be used to ensure that all the metrics are similiar. Normalisation will also be considered and compared to see if either does improve the predictive model.

Feature selection through recursive feature elimination(RFE) will help eliminate redundant features. However, this will be cross-checked against the models without using RFE. Typical advanced models such as Logistic Regression and XGBoost will be able forecast the following day rain accuartely. However to predict more than the day and forecast a week could be difficult or extremely less accurate. We will also attempt to forecast a week ahead.

10 fold Cross validation will be used to ensure that our models are not overfitting and we will also be judging metrics such as computation time to compare the models. 

## Packages to Install

Aside from the standard packages of Pandas, Numpy, SKlearn and Matplotlib, external packages such as missingno and xgboost will need to be installed if you are attempting to run this on your own machine or AWS Sagemaker. If you are using AWS Sagemaker, changed the python3 to whatever notebook style you are using. 

Using conda terminal:
* AWS: conda install -n python3 -c conda-forge missingno
* Jupyter: conda install -c conda-forge missingno
* AWS: conda install -n python3 -c conda-forge xgboost
* Jupyter: conda install -c conda-forge xgboost
  
## Whats in the Repo?
  
There will be a data folder which will contain the base dataset (AusWeather) without any changes and my attempt to fill and complete the dataset(AusWeaterReady). There will be two notebooks, Ausweather and AusWeather-modelling which corresponding to my initial data exploration and cleaning and the other will be my attempt to create a predictive model to predict the classifiers.

## Todo list:

Todo:
- [x] Understand the data
- [x] Impute missing values
- [x] One hot encode the location
- [x] Feature Engineer from date for Seasons
- [x] Use a Standard scalar
- [x] Choose two baseline models
- [x] RFE with those baseline models
- [x] Create baseline models
- [x] Determine the Accuracy through Recall and Precision report
- [x] 10-fold cross validation to ensure no overfitting
- [x] Fine tune the models for better results
- [ ] Visualise the results with a dashboard made with Dash
- [ ] Host the results on Github pages
- [ ] Finalise a report detailing the process and findings
- [x] Code Refactoring
