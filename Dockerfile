# Usar una imagen ligera oficial de Python 3.10 para reducir el tamaño del contenedor
FROM python:3.10-slim

# Instalar las dependencias del sistema necesarias para la interfaz gráfica (Tkinter) y la compatibilidad con OpenCV
RUN apt-get update && \
    apt-get install -y \
    python3-tk \
    libglib2.0-0 \
    libgtk-3-0 \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender1 && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor donde se ejecutará la aplicación
WORKDIR /app

# Copiar todos los archivos del proyecto actual al directorio de trabajo en el contenedor
COPY . /app

# Instalar las dependencias de Python especificadas en requirements.txt sin almacenar caché
RUN pip install --no-cache-dir -r requirements.txt

# Establecer el comando predeterminado para iniciar la aplicación al ejecutar el contenedor
CMD ["python", "main.py"]