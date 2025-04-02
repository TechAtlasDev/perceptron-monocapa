from abc import ABC, abstractmethod
from .perceptron import Perceptron

class Analyzer(ABC):
  def __init__(self, perceptron:Perceptron):
    pass
  
  @abstractmethod
  def mse(self):
    pass

  @abstractmethod
  def mae(self):
    pass

  @abstractmethod
  def r2(self):
    pass