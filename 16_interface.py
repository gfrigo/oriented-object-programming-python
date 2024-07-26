# pylint: disable-all

from abc import ABC, abstractmethod
from typing import Type

# Interfaces são extendidas para seus métodos serem implementados
# Não é necessário atributos
class FormasInterface():

  @abstractmethod
  def get_perimetro(self) -> int:
    pass

  @abstractmethod
  def get_area(self) -> int:
    pass

# Quadrado implementa FormasInterface != Herança
class Quadrado(FormasInterface):

  # Os atributos da Interface também são obrigatórios a quem implementa
  def __init__(self, lado : int, tipo : str) -> None:
    self.__lado = lado
    self.tipo = tipo

  def get_perimetro(self) -> int:
    perimetro = (self.__lado * 4)
    return perimetro

  def get_area(self) -> int:
    area = (self.__lado * self.__lado)
    return area
  
class Retangulo(FormasInterface):

  def __init__(self, lado : int, altura : int, tipo : str) -> None:
    self.__comprimento = lado
    self.__altura = altura
    self.tipo = tipo

  def get_perimetro(self) -> int:
    perimetro = (self.__comprimento * 2) + (self.__altura * 2)
    return perimetro

  def get_area(self) -> int:
    area = (self.__comprimento * self.__altura)
    return area
  
class Engenheiro:

  def __init__(self, nome : str) -> None:
    self.__nome = nome

  # Qualquer classe que implemente a interface é válida
  def calcular_perimetro(self, terreno : Type[FormasInterface]) -> None:
    perimetro = terreno.get_perimetro()
    print(f"{self.__nome} construiu um terreno {terreno.tipo} de perímetro {perimetro}")
  
  def calcular_area(self, terreno: Type[FormasInterface]) -> None:
    area = terreno.get_area()
    print(f"{self.__nome} construiu um terreno {terreno.tipo} de área {area}")

retangulo = Retangulo(2, 2, "Retangular")
quadrado = Quadrado(4, "Quadrado")

engenheiro = Engenheiro("Gabriel Frigo")
engenheiro.calcular_perimetro(retangulo)
engenheiro.calcular_area(retangulo)

engenheiro.calcular_perimetro(quadrado)
engenheiro.calcular_area(quadrado)
  