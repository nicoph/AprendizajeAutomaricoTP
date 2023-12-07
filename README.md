# AprendizajeAutomaricoTP
## Objetivo

- Familiarizarse con la librería scikit-learn y las herramientas que brinda para el pre-procesamiento de datos, la implementación de modelos y la evaluación de métricas, y con TensorFlow para el entrenamiento de redes neuronales.

## Dataset

- El dataset se llama weatherAUS.csv y contiene información climática de Australia de los últimos diez años, incluyendo si para el día siguiente llovió o no y la cantidad de lluvia en las columnas ‘RainTomorrow’ y ‘RainfallTomorrow’. El objetivo es la predicción de estas dos variables en función del resto de las características que se consideren adecuadas. Tiene una columna ‘Location’ que indica la ciudad y el objetivo es predecir la condición de lluvia en las ciudades de Sydney, SydneyAirport, Canberra, Melbourne y MelbourneAirport (costa sureste). Pueden considerarse como una única ubicación. Descartar el resto de los datos.

- Tiene una columna ‘Location’ que indica la ciudad y el objetivo es predecir la condición de lluvia en las ciudades de Sydney, SydneyAirport, Canberra, Melbourne y MelbourneAirport (costa sureste). Pueden considerarse como una única ubicación. Descartar el resto de los datos.

## Notas para su funcionamiento
- El trabajo fue realizado en Jupiter Notebook de Google Colab
Para correr de forma local solamente cabiar la variable file_path por su ruta de esta manera: 
file_path= './ruta-al-archivo/weatherAUS.csv'
- pip install requirements.txt
- Al utilizar plotly express para unos gráficos, la preview en git no visuliza esos mismos.
- Se recomienda usar entorno virtual debido a la cantidad de librerias y los posibles problemas de versionado
- *más info* https://docs.python.org/es/3/tutorial/venv.html
## Toda la información adicinal se encuentra en la notebook

Se agrego un deply con streamlit
Correr de forma local ejecutando el siguiente comando
```python
streamlit run app.py
```
O acceder a [Hugging Face](https://huggingface.co/spaces/rv3r/AA-PrecitipitationsAustraliaPredictions) para probarlo de forma online
