from irismodel import functions

class ModelRunner:

    def run(self, iris):
        return functions.run(iris.get_np_attr())

    def square(self, value):
        return functions.square(value)