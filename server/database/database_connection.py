from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from rich.console import Console

console = Console()


class DatabaseConnection:
    def __init__(self, str_conn: str):
        self.str_conn: str = str_conn
        self.__engine: Engine = None
        self.__session: Session = None

    @property
    def session(self):
        if self.__session is None:
            Session = sessionmaker(bind=self.engine)
            self.__session = Session()
        return self.__session

    @property
    def engine(self):
        if self.__engine is None:
            self.__engine = create_engine(self.str_conn)
        return self.__engine

    def connect(self) -> bool:
        try:
            self.session.connection()
            console.print('Conexion a la base de datos exitosa', style='bold green')
            return True
        except Exception as ex:
            console.print('Falló la conexion con la base de datos', style='bold red')
            print(str(ex))
            return False

    def disconnect(self) -> None:
        if self.session:
            self.session.close()
        console.print('Base de datos desconectada', style='yellow')
