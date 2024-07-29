# pylint: disable-all

# Composição -> Compor classe maior utilizando de outras
# Evitar Herança e Injeção de Dependencia
class Select:
  def select_many(self) -> None:
    print("Selecionando muitos itens")

  def select_one(self, id : int) -> None:
    print(f"Selecionando apenas id {id}")

class Insert:
  def insert_many(self) -> None:
    print("Inserindo muitos itens")

  def insert_one(self) -> None:
    print("Inserindo um item")

class Repository:

  def __init__(self) -> None:
    self.__insert = Insert()
    self.__select = Select()
  
  def select_by_id(self, id : int) -> None:
    self.__select.select_one(id)

repository = Repository()
repository.select_by_id(1)