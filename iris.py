import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Aplicación para predecir iris!
""")


st.sidebar.header('Parámetros de prueba: ') #hasta que se cambie de atributo, estamos modelando la barra lateral!

largoSepalo=st.sidebar.slider('Largo sépalo',4.3, 7.9, 5.4)
anchoSepalo=st.sidebar.slider('Ancho sépalo',2.0, 4.4, 3.4)
largoPetalo=st.sidebar.slider('Largo pétalo',1.0, 6.9, 1.3)
anchoPetalo=st.sidebar.slider('Ancho pétalo',0.1, 2.5, 0.2)

dic={'largoSepalo':largoSepalo, 
      'anchoSepalo':anchoSepalo,
      'largoPetálo':largoPetalo,
      'anchoPétalo':anchoPetalo}

data=pd.DataFrame(dic,index=['Prueba'])

st.subheader("Párametros de prueba")
st.write(data) #Esto carga el dataframe modificable por sliders, tiene apenas una fila.

iris = datasets.load_iris() #Usamos el método iris de la clase estática datasets.
#Cargamos los datos. Todos van a ser de entrenamiento.
X = iris.data 
Y = iris.target

#AJUSTE
clf = RandomForestClassifier()
clf.fit(X, Y)

#PREDICCION
prediction = clf.predict(data) #Nos arroja el tipo de flor
prediction_proba = clf.predict_proba(data)

#Encabezado para los tipos de flor
st.subheader('Tipos de flor y su correspondiente índice')
st.write(iris.target_names)

#Encabezado para la prediction
st.subheader('Predición de la flor')
st.write(iris.target_names[prediction])

#Probabilidades: 
st.subheader('Probabilidades')
st.write(prediction_proba)
