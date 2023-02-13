from fastapi import FastAPI
import pickle
from pydantic import BaseModel, conlist
from typing import List


svm_clf = None
linear_regression_clf = None
random_forest_clf = None
knn_clf = None
app = FastAPI(title="Iris SKLearn API", description="API for iris dataset sklearn models", version="1.0")
CLASSES = ['setosa', 'versicolor', 'virginica']

@app.on_event('startup')
async def load_model():
    with open("svm_clf.pickle", 'rb') as fileobj:
        global svm_clf
        svm_clf = pickle.load(fileobj)
    with open("knn.pickle", 'rb') as fileobj:
        global knn_clf
        knn_clf = pickle.load(fileobj)
    with open("random_forest_clf.pickle", 'rb') as fileobj:
        global random_forest_clf
        random_forest_clf = pickle.load(fileobj)
    with open("linear_regression_clf.pickle", 'rb') as fileobj:
        global linear_regression_clf
        linear_regression_clf = pickle.load(fileobj)

class Iris(BaseModel):
    data: List[conlist(float, min_items=4, max_items=4)]

@app.get("/")
def read_root():
    return {"help": """see docs page at http://127.0.0.1:8000/docs """}

@app.post('/KNN', tags=["prediction"])
async def get_KNN_prediction(iris: Iris):
    global knn_clf
    data = dict(iris)['data']
    class_i = knn_clf.predict(data)[0]
    return {"prediction": CLASSES[class_i]}

@app.post('/SVM', tags=["prediction"])
async def get_SVM_prediction(iris: Iris):
    global svm_clf
    data = dict(iris)['data']
    class_i = svm_clf.predict(data)[0]
    return {"prediction": CLASSES[class_i]}

@app.post('/RandomForest', tags=["prediction"])
async def get_RandomForest_prediction(iris: Iris):
    global random_forest_clf
    data = dict(iris)['data']
    class_i = random_forest_clf.predict(data)[0]
    return {"prediction": CLASSES[class_i]}

@app.post('/LinearRegression', tags=["prediction"])
async def get_LinearRegression_prediction(iris: Iris):
    global linear_regression_clf
    data = dict(iris)['data']
    class_i = linear_regression_clf.predict(data)[0]
    return {"prediction": CLASSES[class_i]}
