# Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Título de la app centrado
st.title('US Vehicle Advertisement Listings')

# Leer la data del archivo CSV 'vehicles_us_cleaned.csv' con manejo de errores
try:
    df = pd.read_csv('vehicles_us_cleaned.csv')
except FileNotFoundError:
    st.error("El archivo 'vehicles_us_cleaned.csv' no se encuentra en el directorio.")
    st.stop()  # Detiene la ejecución del script si no se encuentra el archivo

# Verificar si hay valores faltantes
if df.isnull().any().any():
    st.warning('Hay valores faltantes en el dataset.')

# Filtrar los datos para asegurarnos de que no hay valores nulos en las columnas clave
df = df.dropna(subset=['manufacturer', 'price'])

# Mostrar la data en la app
st.write(df)

# Histograma de los tipos de vehículos por fabricante
st.subheader('Histogram of the types of vehicles by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
# Mostrar el gráfico del histograma
st.plotly_chart(fig)

# Histograma de distribución de precios entre fabricantes
st.subheader('Histogram of price distribution between manufacturers')

# Menú desplegable para seleccionar el fabricante 1 y 2
manufacturer1 = st.selectbox('Manufacturer 1', df['manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['manufacturer'].unique(), index=2)

# Casilla de verificación de histograma normalizado
normalized = st.checkbox('Normalized')

# Filtrar los datos por los fabricantes seleccionados
df_manufacturer1 = df[df['manufacturer'] == manufacturer1]
df_manufacturer2 = df[df['manufacturer'] == manufacturer2]

# Crear el histograma para los fabricantes seleccionados
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df_manufacturer1['price'], 
    name=manufacturer1, 
    opacity=0.75, 
    histnorm='percent'
))

fig.add_trace(go.Histogram(
    x=df_manufacturer2['price'], 
    name=manufacturer2, 
    opacity=0.75, 
    histnorm='percent'
))

# Normalizar el histograma si la casilla de verificación está marcada
if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

# Títulos de los ejes
fig.update_xaxes(title_text='Price')
fig.update_yaxes(title_text='Percentage')

# Mostrar el gráfico
st.plotly_chart(fig)

# Scatter plot matrix
st.subheader('Scatter plot matrix')

# Menú desplegable para seleccionar las dimensiones para el scatter plot
x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)

# Menú desplegable para el color
color = st.selectbox('Color', df.columns, index=3)

# Subtítulo dinámico para el scatter plot matrix
st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')

# Crear el scatter plot matrix
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)

# Mostrar el gráfico
st.plotly_chart(fig)
