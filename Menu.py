from UsuarioDAO import UsuarioDAO
from logger import log
from Usuario import Usuario

opcion = None

while opcion != 5:
    print(f'''
          Opciones para los usuarios:
            1. C (insertar usuario)
            2. R (listar usuarios)
            3. U (actualizar usuario)
            4. D (eliminar usuario)
            5. Salir   
          ''')
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion > 5:
            print('seleccione una opcion de la lista del 1 al 5')
    except:
        print('seleccione una opcion correcta')

    if opcion == 1:
        username = input('Nombre de usuario: ')
        password = input('Contraseña: ')
        datos_usuario = Usuario(username=username, password=password)
        usuario_insertado = UsuarioDAO.insertar(datos_usuario)
        log.debug(f'usuario insertado con exito {usuario_insertado}')

    if opcion == 2:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.debug(usuario)

    if opcion == 3:
        id_usuario = input('id del usuario a actualizar: ')
        username = input('Nuevo nombre de usuario: ')
        password = input('Nueva contraseña: ')
        datos_usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
        try:
            usuario_actualizado = UsuarioDAO.actualizar(datos_usuario)
            if usuario_actualizado == 0:
                log.debug(f'el usuario con id {datos_usuario.id_usuario} no se ha encontrado')
            else:
                log.debug(f'usuario actualizado con exito {usuario_actualizado}')
        except:
            log.debug(f'Ocurrio un error al actualizar usuario con id: {datos_usuario.id_usuario}')
    
    if opcion == 4:
        id_usuario = input('id del usuario a eliminar: ')
        datos_usuario = Usuario(id_usuario=id_usuario,)
        try:
            usuario_eliminado = UsuarioDAO.eliminar(datos_usuario)
            log.debug(f'El usuario con id {datos_usuario.id_usuario} ha sido eliminado con exito')
        except:
            log.debug(f'El usuario con id {datos_usuario.id_usuario} no se ha podido eliminar')


