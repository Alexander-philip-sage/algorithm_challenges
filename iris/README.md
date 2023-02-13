# Interview Challenge for Iris Data Set

ML Engineer assessment instructions:

1. Using the Iris dataset, train models to solve the following: KNN, Random Forest Classifier, SVM classifier, and a logistic regression classifier
2. Using FastApi, create an endpoint for each model that will allow you to pass in a target to each endpoint and execute the model
3. Push the code to GitHub

# Overview

**Pickle Files**: are models trained with sklearn package and saved for serving

**PNG Files**: are part of data exploration and checking out the features and classes

**Notebook File**: was created to find the best hyperparameter and do data exploration

**endpoint.py**: the file that serves the api

**train.py**: a lot of the code from the notebook re-written to run on command line

# Usage

1. Create a virtual environment and install the packages from the requirements file.
2. Activate the venv
3. launch the app `uvicorn endpoint:app --reload`
4. Open a browser and go to http://127.0.0.1:8000/docs
5. Each of the four models are deployed as seperate endpoints to hit. Data is passed in as a list in the body. All four models are loaded when the app starts and are waiting in memory ready for use. 
