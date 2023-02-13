
# Importing dataset from scikit-learn and other useful packages:
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from typing import Tuple
# We will fix a random SEED for reproducibility:
SEED = 11
np.random.seed(SEED)

"""# Explore the Data Set"""


def print_ds_details():
  print("Featues for each flower")
  print(iris_ds['feature_names'])
  print("Targets/labels of each flower")
  print(iris_ds['target_names'])
  print("\nRandom example Data")
  range_ints = np.arange(len(iris_ds['data']))
  np.random.shuffle(range_ints)
  for i in range_ints[:3]:
    print('features:',iris_ds['data'][i])
    print('target: ', iris_ds['target'][i])

  print(iris_ds['DESCR'])

def build_df(iris_ds) -> pd.core.frame.DataFrame:
  data_for_df = np.concatenate((np.array(iris_ds['data']),np.expand_dims(np.array(iris_ds['target'], dtype=int), axis=1)), axis=1)
  columns = iris_ds['feature_names'].copy()
  columns.append('target')
  iris_df = pd.DataFrame(data_for_df, columns =columns  )
  iris_df=iris_df.sample(frac=1).reset_index(drop=True)
  iris_df.head()

  iris_df['target_name'] = iris_df['target'].apply(lambda x: iris_ds['target_names'][int(x)])
  iris_df.head()
  return iris_df
"""The below plot confirms the correlation values presented in the DESC field of the data set. It shows us that based on petal length and width alone, there is a relatively linearly seperable relationship between the classes. """

def plot_classes(iris_df: pd.core.frame.DataFrame, xlabel:str, ylabel:str, fig_name:str):
  for classid in iris_df['target'].unique():
    xys = iris_df[iris_df['target']==classid]
    x = xys[xlabel].to_numpy()
    y = xys[ylabel].to_numpy()
    plt.scatter(x,y,label=iris_ds['target_names'][int(classid)] )
    plt.legend()
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.savefig(fig_name)

def plot_features_classes(iris_df: pd.core.frame.DataFrame):
  '''plots the relationship between how the features impact 
  the classes for two combinations'''
  ylabel= 'petal width (cm)'
  xlabel = 'petal length (cm)'
  plot_classes(iris_df, xlabel, ylabel, (xlabel+" vs "+ylabel).replace("(",''))

  """the sepal width and length alone aren't good at seperating the versicolor and virginica. These two classes are also the most mixed with the petal width and length. They likely will result in the most errors in prediction. """

  ylabel= 'sepal width (cm)'
  xlabel = 'sepal length (cm)'
  plot_classes(iris_df, xlabel, ylabel, (xlabel+" vs "+ylabel).replace("(",''))

"""# Predictive Models
KNN, Random Forest Classifier, SVM classifier, and a logistic regression classifier
"""

def split_dataset(iris_df: pd.core.frame.DataFrame) -> Tuple[: np.ndarray]:
  """ I prefer to split into three categories. A technique that tries to avoid the bias introduced by choosing the right hyperparameters (like model architecture or parameters) based on the accuracy of the test set."""

  test_split = 0.4
  x_data = iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
        'petal width (cm)']].to_numpy()
  y_data = [int(x) for x in iris_df.target.to_list()]
  X_train, X_t, y_train, y_t = train_test_split(x_data, y_data, test_size=test_split, random_state=SEED)
  X_test, X_dev, y_test, y_dev = train_test_split(X_t, y_t, test_size=0.5, random_state=SEED)
  return X_train, y_train, X_test, X_dev, y_test, y_dev 


"""## KNN"""

def grid_search_all(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, X_dev: np.ndarray):
  '''performs a grid search on three of the algorithms to look for the 
  parameters that fit the dataset the best. comments illistrate the analysis'''
  knn_scores = []
  for k in [1,3,5,7,8,40]:
    for w in ['uniform', 'distance']:
      neigh = KNeighborsClassifier(n_neighbors=k, weights=w)
      neigh.fit(X_train, y_train)
      score =neigh.score(X_dev, y_dev)
      knn_scores.append({"n_neighbors":k, "weights":w, "score":score, "ct_train":len(X_train), "ct_dev":len(X_dev)})
  knn_scores_df = pd.DataFrame(knn_scores)
  knn_scores_df.sort_values(by='score', ascending=False)
  knn_scores_df.to_csv("knn_scores_df.csv")
  """Thats really weird. I've never seen the same score with such 
  different parameters in real data. I like the idea of the 'distance' 
  weight in the classifier logically based on the graphs I made in data exploration. 
  Valuing too many points too far out equally is not logical, and it does fail on the 
  extreme when we go to 40 data points. I'll stick with k=3 and weights=distance, 
  as a relatively random choice"""

  """## Random Forest Classifier"""

  rfc_data = []
  for n_estimators in [4, 50,100]:
    for criterion in ['gini', 'entropy']:
      for max_depth in [2,4,10]:
        for min_samples_split in [2,4,10]:
          for min_samples_leaf in [1,2,4,8]:
            params = {"n_estimators":n_estimators, "criterion":criterion, "max_depth":max_depth, "min_samples_leaf":min_samples_leaf, "min_samples_split":min_samples_split}
            clf = RandomForestClassifier(**params, random_state=SEED)
            clf.fit(X_train, y_train)
            score=clf.score(X_dev, y_dev)
            params.update({"score":score, "ct_train":len(X_train), "ct_dev":len(X_dev)})
            rfc_data.append(params)
  rfc_df= pd.DataFrame(rfc_data)
  rfc_df= rfc_df.sort_values(by='score', ascending=False)

  rfc_df.to_csv("random_forest_classifier_df.csv")

  """again a lot of the params are tied for first. So I'll take some of the 
  smaller numbers to keep the model simpler."""

  """## SVM"""
  svm_data = []
  for kernel in ['rbf', 'poly','sigmoid','linear']:
    if kernel in ('rbf', 'poly','sigmoid'):
      for gamma in ['scale', 'auto']:
        clf = make_pipeline(StandardScaler(), SVC(kernel=kernel,gamma=gamma, random_state=SEED))
        svm_data.append({"kernel":kernel, "gamma":gamma,"score":score, "ct_train":len(X_train), "ct_dev":len(X_dev) })
    else:
        clf = make_pipeline(StandardScaler(), SVC(kernel=kernel,random_state=SEED))
        svm_data.append({"kernel":kernel, "gamma":gamma,"score":score, "ct_train":len(X_train), "ct_dev":len(X_dev) })
  svm_df= pd.DataFrame(svm_data)
  svm_df= svm_df.sort_values(by='score', ascending=False)
  svm_df.to_csv("svm_classifier_df.csv")
  '''all the options in the svm produce the same result so I'll choose the simpler kernel, the linear kernel'''
  
  """## Logistic Regression

  this architecture is pretty simple so I'm just going to skip the processing 
  of grid searching through hyperparameters
  """

def train_final_models(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, X_dev: np.ndarray, y_test: np.ndarray, y_dev: np.ndarray ):
  '''parameters for each model are fixed based on 
  results from grid search for each algorithm'''
  neigh = KNeighborsClassifier(n_neighbors=3, weights='distance')
  neigh.fit(X_train, y_train)
  score_train =neigh.score(X_train, y_train)
  score_dev =neigh.score(X_dev, y_dev)
  score_test =neigh.score(X_test, y_test)
  print("train score", score_train)
  print("dev score", score_dev)
  print("test score", score_test)

  rfc_clf = RandomForestClassifier(n_estimators=50,criterion='entropy', max_depth=4, min_samples_leaf=1, min_samples_split=2, random_state=SEED)
  rfc_clf.fit(X_train, y_train)
  score_train=rfc_clf.score(X_train, y_train)
  score_dev=rfc_clf.score(X_dev, y_dev)
  score_test=rfc_clf.score(X_test, y_test)
  print("train score", score_train)
  print("dev score", score_dev)
  print("test score", score_test)

  svm_clf = make_pipeline(StandardScaler(), SVC(kernel='linear', gamma='auto'))
  svm_clf.fit(X_train, y_train)
  score_dev=svm_clf.score(X_dev, y_dev)
  score_test=svm_clf.score(X_test, y_test)
  print("train score", score_train)
  print("dev score", score_dev)
  print("test score", score_test)

  lr_clf = LogisticRegression(random_state=SEED)
  lr_clf.fit(X_train, y_train)
  score_dev=lr_clf.score(X_dev, y_dev)
  score_test=lr_clf.score(X_test, y_test)
  print("train score", score_train)
  print("dev score", score_dev)
  print("test score", score_test)

  return neigh, rfc_clf, svm_clf, lr_clf

if __name__=='__main__':
  iris_ds = load_iris()
  iris_df=build_df(iris_ds)
  plot_features_classes(iris_df)
  X_train, y_train, X_test, X_dev, y_test, y_dev =split_dataset(iris_df)

  neigh, rfc_clf, svm_clf, lr_clf = train_final_models()