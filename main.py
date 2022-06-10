from fastapi import FastAPI

from iris import Iris
from service import Service

app = FastAPI()

species = { 0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica" }

@app.get("/predict/sepal_length/{sepal_length}/sepal_width/{sepal_width}/petal_length/{petal_length}/petal_width/{petal_width}")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    model = "iris.knn.model"
    iris = Iris(sepal_length, sepal_width, petal_length, petal_width)
    result = Service(model).execute(iris)

    resp = {
            "model": model,
            "prediction": str(result),
            "name": species[result[0]]
            }

    return resp