#pylint: disable-all

class Alarme:

  def __init__(self, estado:bool=None) -> None:
    self.__estado = estado

  def set_estado(self, valor:bool) -> None:
    if isinstance(valor, bool):
      self.__estado = valor

  def get_estado(self) -> bool:
    return self.__estado
  
alarme = Alarme()
alarme.set_estado(False)
resultado = alarme.get_estado()
print(resultado)