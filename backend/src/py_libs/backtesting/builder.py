from src.py_libs.backtesting.env import BackTestingEnv
from src.py_libs.backtesting.evaluator import BackTestingEvaluator
from src.py_libs.backtesting.loop import BackTestingLoop
from src.py_libs.objects.basic_strategy import BasicStrategy


class BackTestingBuilder:
    def __init__(self, config):
        self.config = config

    def get_backtesting_loop(self, strategy: BasicStrategy):
        BackTestingLoop(env=BackTestingEnv(), strategy=strategy, evaluator=BackTestingEvaluator())
