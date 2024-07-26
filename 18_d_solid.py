# pylint: disable-all

from abc import ABC, abstractmethod
from typing import Type

# Princípio da inversão da dependência:
# A injeção de dependência (associação) deve ser feita de interfaces genéricas
class RepositorioInterface(ABC):

  @abstractmethod
  def inserir(self) -> None:
    raise 'Should implement inserir() method'
  
  @abstractmethod
  def deletar(self) -> None:
    raise 'Should implement deletar() method'
  
class MySqlRepositorio(RepositorioInterface):

  def __init__(self, dado):
    self.__dado = dado

  def inserir(self) -> None:
    print(f"Inserindo {self.__dado} no MySQL...")

  def deletar(self) -> None:
    print(f"Deletando {self.__dado} no MySQL...")

class PostgresRepositorio(RepositorioInterface):

  def __init__(self, dado):
    self.__dado = dado

  def inserir(self) -> None:
    print(f"Inserindo {self.__dado} no PostgresSQL...")

  def deletar(self) -> None:
    print(f"Deletando {self.__dado} no PostgresSQL...")

class Usuario:

  # Todas as classes que implementarem RepositorioInterface serão válidas
  # Futuras modificações no projeto não afetam Usuario (MySQL -> Postgres)
  def __init__(self, repositorio : Type[RepositorioInterface]) -> None:
    self.__repositorio = repositorio

  def armazenar_dado(self) -> None:
    self.__repositorio.inserir()

  def remover_dado(self) -> None:
    self.__repositorio.deletar()

postgres = PostgresRepositorio("Objeto JSON")
usuario = Usuario(postgres)

usuario.armazenar_dado()
usuario.remover_dado()

