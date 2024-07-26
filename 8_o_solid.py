# pylint: disable-all

# Open close principle -> Entradas diferentes geram ações diferentes
# Molde -> Melhor entendimento com interfaces

class Circo:
  def apresentacao(self, apresentador : any) -> None:
    apresentador.__apresentar_show()

class Palhaco:
  def apresentar_show(self) -> None:
    print("Palhaço apresentou seu show!")

class Malabarista:
  def apresentar_show(self) -> None:
    print("Malabarista apresentou seu show!")

circo = Circo()
palhaco = Palhaco()
malabarista = Malabarista()

circo.apresentacao(palhaco)