# pylint: disable-all

from typing import Type

# Classe Mãe -> Classe Filha -> Classe Neta
class Animal:
  def __init__(self, idade : int, genero : str) -> None:
    self.idade = idade
    self.genero = genero

  def nasce(self) -> None:
    print("Nascendo...")

  def reproduzir(self) -> None:
    print("Reproduzindo...")

  def morrer(self) -> None:
    print("Morrendo...")

class Mamifero(Animal):
  def __init__(self, idade : int, genero : str, tipo:str, patas:int) -> None:
    super().__init__(idade, genero)
    self.tipo = tipo
    self.patas = patas

  def apresentar_mamifero(self) -> None:
    print(f"Olá, sou {self.tipo} de {self.patas} patas")
  
  def ciclo(self) -> None:
    super().nasce()
    super().reproduzir()
    super().morrer()
  
class Cachorro(Mamifero):
  def __init__(self, mamifero : Type[Mamifero], raca : str, porte : str, nome : str) -> None:
    super().__init__(mamifero.idade, mamifero.genero, mamifero.tipo, mamifero.patas)
    self.raca = raca
    self.porte = porte
    self.nome = nome

  def apresentar_cachorro(self) -> None:
    print(f"Olá, me chamo {self.nome}. Sou um cachorro da raça {self.raca} de porte {self.porte}")

mamifero = Mamifero(7, "F", "Doméstico", 4)  
cachorro = Cachorro(mamifero, "Salsicha", "Médio", "Mel")
cachorro.apresentar_mamifero()
cachorro.ciclo()
cachorro.apresentar_cachorro()



