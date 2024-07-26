# pylint: disable-all

# Encapsulamento (acesso) de atributos
# Acesso protegido é passado apenas na herança
class DatabaseConn:

  def __init__(self) -> None:
    self.user =  "Gabriel" # Public access
    self._conn = "//connection_string" # Protected access
    self.__database = "Postgres" # Private access

  def get_database(self) -> str:
    print(self.__database)
  
  def _test_conn(self) -> str: # Protected access method
    print("Connection [200]")
  
class Repository(DatabaseConn):

  def __init__(self) -> None:
    super().__init__()

  def select(self) -> None:
    self._test_conn()
    print(f"connection to {self._conn}")
    print("SELECT * FROM dbo.table;" + f"\nUser: {self.user}")

repository = Repository()
repository.select()
