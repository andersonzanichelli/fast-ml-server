from pydantic import BaseModel
import numpy as np

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    def get_np_attr(self):
        return np.array([[
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width]])

    def __str__(self):
        return '{ "sepal.length": ' + str(self.sepal_length) + ', "sepal.width": ' + str(self.sepal_width) + ', "petal.length": ' + str(self.petal_length) + ', "petal.width": ' + str(self.petal_width) + ' }'