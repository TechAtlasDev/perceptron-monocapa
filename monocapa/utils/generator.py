from .objects.generator import DatasetGenerator

class Celsius2FahrenheitGenerator(DatasetGenerator):
  def __init__(self, function=lambda x : x * 9/5 + 32):
    self.function = function