from logger import log
from psycopg2 import pool as bd
import sys

class Conexion():
    _DATABASE = 'usuario'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = bd.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                    host = cls._HOST,
                                                    user = cls._USERNAME,
                                                    password = cls._PASSWORD,
                                                    port =cls._DB_PORT,
                                                    database = cls._DATABASE)
                log.debug(f'creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'ocurrio un error en la conexon: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerconexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'conexion obtenida del pool {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'se regresa la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall
    
if __name__ == '__main__':
    conexion1 = Conexion.obtenerconexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerconexion()
    conexion3 = Conexion.obtenerconexion()
    conexion4 = Conexion.obtenerconexion()
    conexion5 = Conexion.obtenerconexion()
