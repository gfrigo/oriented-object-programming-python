#pylint: disable-all

from abc import ABC, abstractmethod

# Princípio da Segregação de Interfaces -> Evitar implementações desnecessárias

class AveVoa(ABC):

  @abstractmethod
  def comer(self) -> None:
    raise 'Should implement comer method'

  @abstractmethod
  def voar(self) -> None:
    raise 'Should implement voar method'

  @abstractmethod
  def gritar(self) -> None:
    raise 'Should implement gritar method'

class AveNaoVoa(ABC):

  @abstractmethod
  def comer(self) -> None:
    raise 'Should implement comer method'

  @abstractmethod
  def gritar(self) -> None:
    raise 'Should implement comer method'

class Pinguim(AveNaoVoa):

  def __init__(self) -> None:
    self.ave = "Pinguim"

  def comer(self) -> None:
    print(f"Ave do tipo {self.ave} está comendo...")

  def gritar(self) -> None:
    print(f"Ave do tipo {self.ave} está gritando...")

class Canario(AveVoa):

  def __init__(self) -> None:
    self.ave = "Canário"

  def comer(self) -> None:
    print(f"Ave do tipo {self.ave} está comendo...")

  def voar(self) -> None:
    print(f"Ave do tipo {self.ave} está voando...")
  
  def gritar(self) -> None:
    print(f"Ave do tipo {self.ave} está gritando...")

pinguim = Pinguim()
canario = Canario()

pinguim.comer()
canario.voar()