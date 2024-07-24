# pylint: disable-all

from typing import Type

class Interruptor:

  def __init__(self, comodo: str) -> None:
    self.__comodo = comodo

  def acender(self) -> None:
    print(f"Acendendo {self.__comodo}")

  def apagar(self) -> None:
    print(f"Apagando {self.__comodo}")

class Pessoa:

  def acender_luz(self, interruptor: Type[Interruptor]) -> None:
    interruptor.acender()

  def apagar_luz(self, interruptor: Type[Interruptor]) -> None:
    interruptor.apagar()

pessoa = Pessoa()
interruptor_sala = Interruptor("Sala")

pessoa.acender_luz(interruptor_sala)
pessoa.apagar_luz(interruptor_sala)