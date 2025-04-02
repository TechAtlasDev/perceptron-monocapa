x = [
  [0, 1],
  [2, 2],
  [1, 1],
  [2, 0],
  [1, 4],
  [3, 4],
  [5, 2],
  [3, -1],
  [6, 1],
  [4, -2],
]

y = [
  0, 1, 0, 0, 1,
  1, 1, 0, 1, 0
]



import matplotlib.pyplot as plt
plt.scatter(x=[xi[0] for xi in x], y=[xi[1] for xi in x], c=y)
plt.grid()
plt.show()


def main():
  from .core.perceptron import Perceptron
  from .core.activation import escalon
  from .utils.utils import plot_decision_boundary

  perceptron = Perceptron( 
    f_activation=escalon
  )
  perceptron.entrenar(
    x=x,
    y=y,
    alpha=0.1,
    epochs=10
  )

  plot_decision_boundary(perceptron=perceptron, x=x, y=y)
