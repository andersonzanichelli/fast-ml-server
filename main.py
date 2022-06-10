import logging
from fastapi import FastAPI

from src.iris import Iris
from src.service import Service

app = FastAPI()

logging.config.fileConfig('src/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

species = { 0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica" }

@app.post("/predict/")
def predict(iris: Iris):
    logger.info(f'Receive the iris request {iris}')

    model = "src/iris.knn.model"
    result = Service(model).execute(iris)

    resp = {
            "model": model,
            "prediction": str(result),
            "name": species[result[0]]
            }

    return resp