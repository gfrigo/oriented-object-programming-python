#pylint: disable-all

from typing import Dict, Type

# Polimorfismo -> Assinatura de métodos da super classe podem ser alteradas
class Repositorio:

  def select(self, nome : str) -> Dict:
    return {"nome" : nome, "idade" : 19}
  
  def insert(self, nome : str, idade : int) -> Dict:
    print(f"Inserindo dados: {nome}, {idade}")
    return {"nome" : nome, "idade": idade}
  
class Insersor:

  # Injeção de dependência
  def __init__(self, repositorio: Type[Repositorio]) -> None:
    self.__repositorio = repositorio
  
  def inserir_dados(self, nome : str, idade : int) -> Dict:
    registro = self.__repositorio.select(nome)
    if registro:
      raise Exception("O registro já existe.")

    novo_registro = self.__repositorio.insert(nome, idade)
    return novo_registro
  
class RepositorioFaker(Repositorio):
  def __init__(self) -> None:
    super().__init__()

  # Quero evitar que seja lançada a exceção
  # Para reescrever o método é necessário os mesmos argumentos
  def select(self, nome : str) -> None:
    return None
  
# repositorio = Repositorio()
repositorio = RepositorioFaker()
insersor = Insersor(repositorio)

dados = insersor.inserir_dados("Gabriel", 19)
print(dados)


