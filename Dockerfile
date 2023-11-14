# Usa una imagen Python más liviana
FROM python:3-slim

# Instala la dependencia necesaria
RUN pip install pandas Flask

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY app.py /app/
COPY movies.csv /app/
COPY ratings.csv /app/

# Asigna permisos de ejecución al script
RUN chmod +x app.py

# Establece el punto de entrada
ENTRYPOINT ["python", "app.py"]
