# pylint: disable-all

from abc import ABC, abstractmethod
from typing import Type

# Agregação -> Agregar uma classe com objetos de outra
class Item(ABC):

  @abstractmethod
  def informacoes_produto(self) -> None:
    raise 'Should implement informacoes_produto method'

class Produto(Item):

  def __init__(self, nome : str, valor : int) -> None:
    self.__nome = nome
    self.__valor = valor

  def informacoes_produto(self) -> None:
    print(f"Produto: {self.__nome}. Valor: R${self.__valor}")

class Servico(Item):

  def __init__(self, nome : str, valor : int) -> None:
    self.__nome = nome
    self.__valor = valor

  def informacoes_produto(self) -> None:
    print(f"Serviço: {self.__nome}. Valor: R${self.__valor}")

class CarrinhoDeCompras:

  def __init__(self) -> None:
    self.__itens = []

  def adicionar_produto(self, item : Type[Item]) -> None:
    self.__itens.append(item)
  
  def finalizar_compra(self) -> None:
    for item in self.__itens:
      item.informacoes_produto()
    self.__itens = []

monitor = Produto("Monitor", 1000)
manutencao = Servico("Manutenção", 300)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(monitor)
carrinho.adicionar_produto(manutencao)
carrinho.finalizar_compra()