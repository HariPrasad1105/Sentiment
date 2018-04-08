from FirstProject1 import Sentiment
from TrainingAlgorithm import Algorithm

class Sentiment1:

    def __init__(self, keyword):
        self.key = keyword

    def function(self):
        senti = Sentiment(self.key, 100)
        # algo = Algorithm()
        # pos, neg, neu = algo.result()
        # print(pos, neg, neu)
        # return pos, neg, neu
