from termpyx import Console

class Perceptron:
  def __init__(self, f_activation):
    self.f_activation = f_activation
    self.w1 = 0
    self.w2 = 0
    self.bias = 0

    self.console = Console()

  def entrenar(self, x, y, alpha=0.1, epochs=1, verbose=True):
    self.console.in_debug = verbose

    for epoch in range(epochs):
      if verbose:
        self.console.separator(f"Epoch {epoch}")

      self.console.debug(f"w1: {self.w1} | w2: {self.w2}")
      ssr = []
      ssr_data = []
      for (x1, x2), y1 in zip(x, y):
        y2 = self.predecir([x1, x2])
        delta = y1-y2

        # Update weights
        self.w1 += alpha*delta*x1
        self.w2 += alpha*delta*x2
        self.bias += delta

        ssr.append(delta**2)
        ssr_data.append([y1, y2])

      self.console.debug(f"MSE: {(sum(ssr)/len(ssr))} | SSR: {ssr} | SSR_DATA: {ssr_data}\n")

  def psv(self, x):
    return x[0] * self.w1 + x[1] * self.w2
      
  def predecir(self, x):
    psv = self.psv(x)
    return self.f_activation(psv+self.bias)
