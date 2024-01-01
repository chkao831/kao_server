from src.py_libs.objects.basic_strategy import BasicStrategy


class SimpleStrategy(BasicStrategy):
    def __init__(self):
        super().__init__()
        self.biases = {}

    def select_action(self, historical_data):
        pass
