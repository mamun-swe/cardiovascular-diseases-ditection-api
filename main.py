from typing import Union

from fastapi import FastAPI

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/test-result")
def analysisData():
    df = pd.read_csv("./dataset.csv")
    x = df.iloc[:, :-1]
    y = df.iloc[:, 13]
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=1)

    # Random forest classifier
    Rclf = RandomForestClassifier()
    Rclf.fit(xtrain, ytrain)

    # Decission tree classifier
    Dclf = DecisionTreeClassifier()
    Dclf.fit(xtrain, ytrain)

    # Support vector machine classifier
    svm = SVC()
    svm.fit(xtrain, ytrain)

    rfcl_score = Rclf.score(xtest, ytest)
    dclf_score = Dclf.score(xtest, ytest)
    svm_score = svm.score(xtest, ytest)

    return {
        "randon_forest_classifier_result": rfcl_score,
        "decission_tree_classifier_result": dclf_score,
        "support_vector_machine_result": svm_score,
    }
