# Usar la imagen oficial de nginx
FROM nginx

# Instalar Python y pip
RUN apt-get update && apt-get install -y python3-pip

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip3 install -r requirements.txt

# Copiar todos los archivos de la carpeta app al contenedor
COPY app/ .

# Copiar el archivo de configuración de nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80
EXPOSE 80

# Ejecutar app.py al iniciar el contenedor
CMD ["python3", "app/app.py"]
