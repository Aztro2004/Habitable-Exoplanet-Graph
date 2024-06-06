# Usar una imagen base oficial de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django

# Copiar el resto del código fuente de la aplicación
COPY . .

# Exponer el puerto donde se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]