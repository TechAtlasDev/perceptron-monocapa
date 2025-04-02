from abc import ABC, abstractmethod

class FActivation(ABC):
  def __init__(self, f_core:callable):
    self.f_core = f_core

  @abstractmethod
  def __call__(self, x):
    pass

  @abstractmethod
  def deriv(self, x):
    pass