FROM nginx:alpine

# Instalar Python
RUN apk add --no-cache python3

# Copiar los archivos estáticos desde la etapa de construcción
COPY --from=builder /app/. /usr/share/nginx/html/

# Copiar la configuración de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80
EXPOSE 80

# Comando para iniciar la aplicación Python
CMD ["python3", "app.py"]
