#pylint: disable-all

# O método abstrato é uma assinatura que deve obrigatoriamente ser implementada
from abc import ABC, abstractmethod

class AbstractClass(ABC):

  def __init__(self) -> None:
    self.atributo = "Olá mundo"

  @abstractmethod
  def metodo_abstrato(self) -> None:
    pass

class Filha(AbstractClass):

  def apresentar_atributo(self) -> None:
    print(self.atributo)

  # Polimorfismo
  def metodo_abstrato(self) -> None:
    print("Implementando método abstrato")

filha = Filha()
filha.apresentar_atributo()
filha.metodo_abstrato()
