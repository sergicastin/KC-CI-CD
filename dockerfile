# Etapa de construcción
FROM python:3.8 AS builder

# Configura el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos estáticos desde la etapa de construcción
COPY . /app

# Etapa final
FROM nginx:alpine

# Configura el directorio de trabajo en /usr/share/nginx/html
WORKDIR /usr/share/nginx/html

# Copia los archivos estáticos desde la etapa de construcción
COPY --from=builder /app/templates .

# Copia la configuración de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80
EXPOSE 80

# Comando para iniciar el servidor Nginx
CMD ["nginx", "-g", "daemon off;"]
