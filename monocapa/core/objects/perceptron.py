from ..abs.perceptron import Perceptron
import numpy as np

class PerceptronBase(Perceptron):
  def __init__(self, f_activation, input_units):
    self.f_activation = f_activation
    self.units = input_units
    self.weights = np.zeros(input_units)
    self.bias = 0

    self.error_history:list[list[np.ndarray]] = []

  def train(self, x, y, alpha, epochs):
    for _ in range(epochs):
      ssr = list()
      for xi, yi in zip(x, y):
        y_pred = self.predict(xi)

        error = yi - y_pred
        self.weights += alpha * error * xi
        self.bias += alpha * error

        ssr.append(error)
      self.error_history.append(ssr)

  def predict(self, x):
    dot = np.dot(x, self.weights) + self.bias
    return self.f_activation(dot)
  
  def __repr__(self):
    return f"PerceptronBase(f_activation={self.f_activation}, input_units={self.units}, weights={self.weights}, bias={self.bias})"