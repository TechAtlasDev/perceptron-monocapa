import numpy as np
import matplotlib.pyplot as plt

def plot_decision_boundary(perceptron, x, y):    
    x_min, x_max = min(xi[0] for xi in x) - 1, max(xi[0] for xi in x) + 1
    y_min, y_max = min(xi[1] for xi in x) - 1, max(xi[1] for xi in x) + 1

    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                        np.linspace(y_min, y_max, 100))
    zz = np.array([perceptron.predecir([x1, x2]) for x1, x2 in zip(xx.ravel(), yy.ravel())])
    zz = zz.reshape(xx.shape)

    plt.contourf(xx, yy, zz, alpha=0.3)
    plt.scatter([xi[0] for xi in x], [xi[1] for xi in x], c=y, edgecolor="k")
    plt.grid()
    plt.show()
