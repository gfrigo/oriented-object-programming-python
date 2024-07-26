#pylint: disable-all

#Single responsability
class SistemaCadastral:

  def __init__(self, nome:str, idade:int) -> None:
    self.__nome = nome
    self.__idade = idade

  def cadastrar(self) -> None:
    if self.verificacao():
      self.armazenar()
    else:
      self.erro()

  def verificacao(self) -> bool:
    if isinstance(self.__nome, str) and isinstance(self.__idade, int):
      return True
    else:
      return False

  def armazenar(self) -> None:
    print("Acessando banco de dados...")
    print(f"Cadastro de {self.__nome} realizado!")

  def erro(self) -> None:
    print("Dados inválidos.")

sistemma_cadastral = SistemaCadastral("Gabriel", 19)
 