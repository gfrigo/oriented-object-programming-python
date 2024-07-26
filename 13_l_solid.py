#pylint: disable=all

from typing import Type

# Princípio da substituição de Liskov:
# Permite usar qualquer subtido da classe herdada para utilizar métodos requeridps
# Não permitido fazer "overwriting" de métodos semelhantes

class Animal:

  def comer(self) -> None:
    print("Animal está comendo...")

  def andar(self) -> None:
    print("Animal está andando...")

  def dormir(self) -> None:
    print("Animal está dormindo...")

class Ave(Animal):

  def __init__(self) -> None:
    super().__init__()

  def cantar(self) -> None:
    print("Ave cantando...")

class Pinguim(Ave):

  def __init__(self) -> None:
    super().__init__()

  def escorregar(self) -> None:
    print("Pinguim escorregando...")

class Pessoa():

  # Type[Animal] pode ser substitúida por Type[Ave] ou Type[Pinguim]
  # Qualquer subtipo de Animal pode ser substituído para o mesmo resultado.
  # Ave, Pingum e Animal -> São do tipo Animal()
  def observar(self, animal : Type[Animal]) -> None:
    animal.dormir()

# O método observar pode receber qualquer subtido de Animal
pessoa = Pessoa()
pinguim = Pinguim()
pessoa.observar(pinguim)

pinguim_2 = Animal()
pessoa.observar(pinguim_2)

pinguim_3 = Ave()
pessoa.observar(pinguim_3)