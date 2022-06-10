import pickle

class ModelRunner:

    def __init__(self, model_name):
        self.model_name = model_name

    def load_model(self):
        with open(self.model_name, 'rb') as file:
            return pickle.load(file)

    def run(self, iris):
        model = self.load_model()

        predicted = model.predict(iris.get_np_attr())

        return predicted
