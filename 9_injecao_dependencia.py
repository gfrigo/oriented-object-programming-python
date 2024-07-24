# pylint: disable-all

from typing import Type

# Classe 'Pessoa' depende de 'Casa' como dependencia
class Casa:

  def __init__(self) -> None:
    self.__endereco = 'Rua dos alfineiros'

  def acender_luzes(self) -> None:
    print("Acendendo luzes...")

  def get_endereco(self) -> str:
    return self.__endereco

class Pessoa:

  def __init__(self, nome : str, local : Type[Casa]) -> None:
    self.__nome = nome
    self.__local = local
    
  def entrar_local(self) -> None:
    self.__local.acender_luzes()

  def apresentar_local(self) -> None:
    endereco = self.__local.get_endereco()
    print(endereco)

casa_amigo = Casa()
pessoa = Pessoa("Gabriel", casa_amigo)

pessoa.apresentar_local()