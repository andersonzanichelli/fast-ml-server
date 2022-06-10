import numpy as np

class Iris:

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width 
        self.petal_length = petal_length
        self.petal_width = petal_width 

    def get_np_attr(self):
        return np.array([[
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width]])

    def __str__(self):
        return '{ "sepal.length": ' + str(self.sepal_length) + ', "sepal.width": ' + str(self.sepal_width) + ', "petal.length": ' + str(self.petal_length) + ', "petal.width": ' + str(self.petal_width) + ' }'