from logger import log
from Conexion import Conexion

class CursorPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('inicio metodo with __enter__')
        self._conexion = Conexion.obtenerconexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, tipo_exception, valor_exception, detalle_expetion):
        log.debug('Se ejecuta metodo __exit__')
        if valor_exception:
            self._conexion.rollback()
            log.error(f'ocurrio un error {valor_exception}, {tipo_exception, {detalle_expetion}}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
    
if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('dentro del bloque with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())