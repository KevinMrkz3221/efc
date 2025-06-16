# Dockerfile para backend Django
FROM python:3.11-slim

# Variables de entorno para evitar prompts de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia los archivos de requerimientos
COPY requirements.txt ./

# Instala dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código del backend
COPY . .

# Expone el puerto por defecto de Django
EXPOSE 8000

# Comando por defecto para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
