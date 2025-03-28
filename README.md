# Project 1

# Machine Learning Analysis of Musical Patterns: Classification and Regression on Spotify Dataset

Description: This project analyzes Spotify music features using machine learning models. It implements two main functions: (1) classifying song danceability as high/low and (2) predicting song valence (positiveness)

## Usage

### Training.ipynb

Run `training.ipynb` to train models:

* Loads and preprocesses Spotify dataset
* Trains classification models (Logistic Regression, Random Forest)
* Trains regression models (Linear Regression, Ridge, Decision Tree)
* Saves models to .pkl files

### Testing.ipynb

Run `test.ipynb` to load trained models and make predictions.


### Custom Utility Functions

The project includes a custom `DataCleaner` transformer in `utility.py` that can be used in scikit-learn pipelines:


### Task

* **Classification Task** : Predicts high/low danceability
* **Regression Task** : Predicts song valence (positiveness)

## Data Features

* `danceability`: How suitable the track is for dancing
* `energy`: Energy level of the track
* `loudness`: Overall loudness in decibels
* `speechiness`: Presence of spoken words
* `acousticness`: Acoustic elements in the track
* `instrumentalness`: Instrumental content
* `valence`: Musical positiveness

## Author

Tzu-Chieh Chao
