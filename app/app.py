from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from datetime import datetime
import pandas as pd
from joblib import load
import plotly.express as px

app = Flask(__name__)
CORS(app)

def get_model(selection):
    if selection == 'RedNeuronal':
        return load('../models/ann.joblib')
    elif selection == 'BosqueAleatorio':
        return load('../models/rf_model.joblib')
    elif selection == 'KVecinosCercanos':
        return load('../models/knn.joblib')


@app.route("/csv", methods=["POST"])
def csv():
    file = request.files["file"]
    selection = request.form.get("selection")

    # Cargar el modelo y hacer las predicciones
    df = pd.read_csv(file)
    model = get_model(selection)
    df['weather'] = model.predict(df)

    # # Guardar csv
    formatted_date = datetime.now().strftime("%Y%m%d-%H%M%S")
    new_filename = f"../users_data/{formatted_date}@{selection}.csv"
    df.to_csv(new_filename, index=False)

    return 'Archivo procesado exitosamente.'


@app.route("/graficas", methods=["GET"])
def graficas():
    # El directorio donde se guardan los archivos
    data_dir = "../users_data"

    # Obtener la lista de archivos en el directorio
    filenames = os.listdir(data_dir)

    # Ordenar los archivos por fecha de modificación para obtener el más reciente
    filenames.sort(key=lambda x: os.path.getmtime(
        os.path.join(data_dir, x)), reverse=True)

    # Obtener el archivo más reciente
    latest_filename = filenames[0]
    filepath = os.path.join(data_dir, latest_filename)

    # Encontrar el archivo que contiene el timestamp
    # filenames = [f for f in os.listdir(data_dir) if formatted_date in f]
    # filename = filenames[0]
    # filepath = os.path.join(data_dir, filename)

    # Cargar el archivo en un DataFrame de pandas
    df = pd.read_csv(filepath)

    # Poner la primer letra en mayúscula en las predicciones
    df['weather'] = df['weather'].str.title()
    # Gráfica de predicciones
    graph = px.scatter(df, x=df.index, y='weather', title='Predicción de cada registro', labels={
                       'index': 'Número de registro', 'weather': 'Predicción'})

    # Convertir las gráficas a JSON para enviarlas
    graphs = [graph.to_json()]

    return jsonify({"graphs": graphs})


if __name__ == "__main__":
    app.run(debug=True)
