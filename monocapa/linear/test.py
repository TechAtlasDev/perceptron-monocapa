from ..core.activation import linear
from ..utils.generator import Celsius2FahrenheitGenerator
from ..core.objects.perceptron import PerceptronBase

from ..core.objects.analyzer import Analyzer

def main():
  generador = Celsius2FahrenheitGenerator()
  x, y = generador.generate(13, shuffle=True)
  #generador.graph()

  perceptron = PerceptronBase(
    f_activation=linear,
    input_units=1
  )
  perceptron.train(x, y, 0.01, 300)

  analyzer = Analyzer(
    perceptron=perceptron,
  )
  analyzer.debug()
  analyzer.error()
  analyzer.mse()
  analyzer.ssr()
  
  value = -753
  valor_predicho = perceptron.predict(value)
  valor_esperado = generador.test(value)

  analyzer.console.separator("Analizando el modelo")
  analyzer.console.log(
    f"Valor esperado: {valor_esperado} | Valor predicho: {valor_predicho}"
  )