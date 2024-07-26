#pylint: disable-all

# Objetivo: Não há necessidade de instâncias para acessar o método estático
class Error:
  
  @staticmethod
  def error_500():
    print("Internal Server Error.")

  @staticmethod
  def error_404():
    print("Not Found.")

Error.error_500()
Error.error_404()