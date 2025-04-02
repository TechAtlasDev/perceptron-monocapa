from ..abs.generator import Generator
import random

class DatasetGenerator(Generator):
  def __init__(self, function=lambda x: x):
    self.function = function
    self.x = []
    self.y = []

  def generate(self, quantity, r_start:int=None, r_end:int=None, shuffle=False):
    self.x = [x for x in range(quantity)]
    self.y = [self.function(x) for x in self.x]

    if shuffle:
      data = list(zip(self.x, self.y))
      random.shuffle(data)
      self.x, self.y = zip(*data)

    return self.x, self.y
  
  def graph(self):
    import matplotlib.pyplot as plt
    plt.plot(self.x, self.y)
    plt.title("Dataset")
    plt.show()

  def test(self, x):
    return self.function(x)