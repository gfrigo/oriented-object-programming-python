#pylint: disable-all

class Calculadora:

  def __init__(self, n1:int, n2:int) -> None:
    self.__n1 = n1
    self.__n2 = n2

  def calcular(self, op:str) -> int:
    if(op == "+"):
      return self.__adicionar()
    elif op == "-":
      return self.__subtrair()
    else:
      return "Operação inválida"

  # Encapsulamento privado = "__" + (nome_do_metodo/atributo)
  def __adicionar(self) -> int:
    return self.__n1 + self.__n2
    
  def __subtrair(self) -> int:
    return self.__n1 - self.__n2
    
calculadora = Calculadora(5, 3)
resultado1 = calculadora.calcular(op="+")
resultado2 = calculadora.calcular(op="-")

print(f"{resultado1} e {resultado2}")

