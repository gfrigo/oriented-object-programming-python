# pylint: disable-all

class ControleRemoto:

  # Construtor e contexto
  def __init__(self, televisao:str, comodo: str) -> None:
    self.televisao = televisao
    self.comodo = comodo

  def avancar_canal(self) -> None:
    print("Avançando canal...")

  def voltar_canal(self) -> None:
    print("Voltando canal...")

  def escolher_canal(self, canal:int) -> None:
    print(f"Canal selecionado: {canal}")


controle_remoto = ControleRemoto("LG", "Quarto")
controle_remoto.avancar_canal()
controle_remoto.voltar_canal()
controle_remoto.escolher_canal(500)