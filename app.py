#!/usr/bin/env python

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar datos desde los archivos CSV
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Realizar alguna manipulación de datos si es necesario

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/movies"

@app.route("/api/movies")
def get_movies():
    # Convertir los datos de películas a formato JSON y devolverlos
    return jsonify(movies.to_dict(orient='records'))

@app.route("/api/ratings")
def get_ratings():
    # Convertir los datos de calificaciones a formato JSON y devolverlos
    return jsonify(ratings.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
