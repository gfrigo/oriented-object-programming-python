# pylint: disable-all

# Variáveis globais no contexto da classe
# self: contexto do objeto / cls: contexto da classe
class Loja:

  tarifa = 2

  @classmethod
  def vender(cls, valor:float) -> float:
    return valor * cls.tarifa

  @classmethod
  def alterar_taxa(cls, nova_tarifa:int) -> None:
    cls.tarifa = nova_tarifa

loja1 = Loja()
loja2 = Loja()

print(loja1.vender(10))
print(loja2.vender(10))

loja1.alterar_taxa(5)

print(loja1.vender(10))
print(loja2.vender(10))