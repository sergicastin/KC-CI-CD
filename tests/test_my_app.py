import os
import logging

# Definir la ruta del archivo de registro
log_file_path = '/app/logs/app.json'

# Crear el manejador de logs
log_handler = logging.FileHandler(log_file_path)

# Configurar el formato del log
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

# Configurar el nivel de registro
log_handler.setLevel(logging.DEBUG)

# Crear un objeto logger
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

# Ejemplo de registro
logger.info('Este es un mensaje de ejemplo')
