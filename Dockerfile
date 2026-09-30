# Usamos una imagen ligera de Python optimizada para ciencia de datos
FROM python:3.11-slim

# Instalar dependencias del sistema requeridas para herramientas científicas
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    git \
    && rm -rf /var/lib/apt/lists/*

# Instalar el ecosistema oficial de física de partículas (Scikit-HEP) estable
RUN pip install --no-cache-dir \
    uproot \
    awkward \
    vector \
    particle \
    numpy \
    matplotlib

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /home/physics_user

# Comando por defecto al iniciar el contenedor (abrir terminal interactiva de Python)
CMD ["python3"]
