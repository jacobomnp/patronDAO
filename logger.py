import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s, [%(filename)s:%(lineno)s] %(message)s',
                datefmt = '%I:%M:%S %p',
                handlers = [
                        log.FileHandler('capa_datos.log'),
                        log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mnesaje a nivel de info')
    log.warning('mensaje a warning')
    log.error('Mensaje a nivel de error')
    log.critical('mensaje a nivel de critical')