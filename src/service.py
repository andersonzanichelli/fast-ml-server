from src.model_runner import ModelRunner

class Service:

    def __init__(self, model_filename):
        self.model = model_filename

    def execute(self, iris):
        return ModelRunner(self.model).run(iris)