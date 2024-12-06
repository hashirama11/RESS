# Utilizar la última versión de Python 3.13
FROM python:3.13

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar requirements.txt y luego instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio actual en el contenedor
COPY . .

# Ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
