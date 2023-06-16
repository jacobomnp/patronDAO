from Cursor import CursorPool
from Usuario import Usuario
from logger import log

class UsuarioDAO():
    '''DAO (data access objetc)
    CRUD(Create, Read, Update, Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    _DELETE = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona a insertar: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
           
    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {usuario}')
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._DELETE, valores)
            log.debug(f'persona eliminada: {persona}')
            return cursor.rowcount

    # @classmethod
    # def eliminar(cls, persona):
    #     with Conexion.obtenerconexion():
    #         with Conexion.obtenerCursor() as  cursor:
    #             valores = (persona.id_persona,)
    #             cursor.execute(cls._DELETE, valores)
    #             log.debug(f'persona eliminada: {persona}')
    #             return cursor.rowcount
            
if __name__ == '__main__':
    personas = UsuarioDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
    
    # usuario1 = Usuario(username='Perla', password='kispytos')
    # usuario_insertado = UsuarioDAO.insertar(usuario1)
    # log.debug(f'personas insertadas: {usuario_insertado}')
    
    usuario2 =  Usuario(username='mmartinez', password='tacodecnasta', id_usuario=6)
    usuario_actualizado = UsuarioDAO.actualizar(usuario2)
    log.debug(f'Usuario actualizado; {usuario_actualizado}')

    usuario3 = Usuario(id_usuario=7)
    usuario_eliminado = UsuarioDAO.eliminar(usuario3)
    log.debug(f'usuario eliminado: {usuario_eliminado}')


