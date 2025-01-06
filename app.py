#Importar librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


#Titulo de la app centrado
st.title('US Vehicle Advertisement Listings')


#Leer la data de csv file vehicled_us_clean.csv
df = pd.read_csv('vehicles_us_cleaned.csv')

#Mostrar la data en la app
st.write(df)

#Histogram de los tipos de vehículos por fabricante
st.subheader('Histogram of the types of vehicles by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
# plot del histogram
st.plotly_chart(fig)

#Histogram de distribución de precios entre fabricantes
st.subheader('Histogram of price distribution between manufacturers')
#Menú desplegable para seleccionar el fabricante 1 y 2.
#Los índices 1 y 2 se utilizan para establecer valores predeterminados para el menú desplegable.
manufacturer1 = st.selectbox('Manufacturer 1', df['manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['manufacturer'].unique(), index=2)
#Crear una casilla de verificación de histogram normalizado
normalized = st.checkbox('Normalized')
#Crear un histogram con la entrada fabricante1 y fabricante2
fig = px.histogram()
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer1]['price'], name=manufacturer1, opacity=0.75, histnorm='percent'))
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer2]['price'], name=manufacturer2, opacity=0.75, histnorm='percent'))
#Normalizar el histogram si la casilla de verificación está marcada
if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
#x-axis title
fig.update_xaxes(title_text='Price')
#y-axis title
fig.update_yaxes(title_text='Percentage')
#Plot de histogram
st.plotly_chart(fig)



#Scatter plot matrix 
st.subheader('Scatter plot matrix')
#Menú desplegable para cada dimensión
#Los índices 1, 2 y 3 se utilizan para establecer valores predeterminados para el menú desplegable.
x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)
#Desplegable para el color
color = st.selectbox('Color', df.columns, index=3)
#Subtítulo de la matriz del diagrama de dispersión que se actualiza automáticamente
st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')
#Crear scatter plot matrix
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)
#Plot de scatter plot matrix
st.plotly_chart(fig)
