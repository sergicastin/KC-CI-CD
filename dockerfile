# Usar la imagen oficial de nginx
FROM nginx

# Instalar Python, venv, libpq-dev y gcc
RUN apt-get update && apt-get install -y python3.11-venv libpq-dev gcc python3-dev

# Crear un entorno virtual e instalar pip
RUN python3 -m venv /app/venv && /app/venv/bin/python -m ensurepip

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias en el entorno virtual
RUN /app/venv/bin/python -m pip install -r requirements.txt

# Copiar todos los archivos de la carpeta app al contenedor
COPY . .

# Copiar el archivo de configuración de nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 8080
EXPOSE 8080

# Ejecutar app.py al iniciar el contenedor usando el intérprete de Python del entorno virtual
CMD ["/app/venv/bin/python", "app/app.py"]
