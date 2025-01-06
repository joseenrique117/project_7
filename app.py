# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Title of the app centered
st.title('US Vehicle Advertisement Listings')

# Read data from CSV file vehicles_us_cleaned.csv
df = pd.read_csv('vehicles_us_cleaned.csv')

# Check for missing values in relevant columns and drop them
missing_values = df[['manufacturer', 'type', 'price']].isnull().sum()
if missing_values.any():
    st.warning(f'Missing values detected in columns: {missing_values[missing_values > 0]}')
    # Drop rows with missing values in key columns (manufacturer, type, price)
    df = df.dropna(subset=['manufacturer', 'type', 'price'])

# Display the cleaned data in the app
st.write(df)

# Histogram of vehicle types by manufacturer
st.subheader('Histogram of the types of vehicles by manufacturer')

# Ensure there are no NaN values in the relevant columns
df_clean = df.dropna(subset=['manufacturer', 'type'])

# Now plot the histogram
fig = px.histogram(df_clean, x='manufacturer', color='type')
st.plotly_chart(fig)

# Histogram of price distribution between manufacturers
st.subheader('Histogram of price distribution between manufacturers')

# Ensure there are no NaN values for 'manufacturer' and 'price'
manufacturer1 = st.selectbox('Manufacturer 1', df['manufacturer'].dropna().unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['manufacturer'].dropna().unique(), index=2)
normalized = st.checkbox('Normalized')

# Filter out rows where 'price' or 'manufacturer' is NaN for the selected manufacturers
df_filtered = df[df['price'].notna() & df['manufacturer'].notna()]

# Create the histogram
fig = px.histogram()
fig.add_trace(go.Histogram(x=df_filtered[df_filtered['manufacturer'] == manufacturer1]['price'], 
                           name=manufacturer1, opacity=0.75, histnorm='percent'))
fig.add_trace(go.Histogram(x=df_filtered[df_filtered['manufacturer'] == manufacturer2]['price'], 
                           name=manufacturer2, opacity=0.75, histnorm='percent'))

# Normalize the histogram if the checkbox is checked
if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

# Set axis titles
fig.update_xaxes(title_text='Price')
fig.update_yaxes(title_text='Percentage')

# Display the histogram
st.plotly_chart(fig)

# Scatter plot matrix
st.subheader('Scatter plot matrix')
numeric_columns = df.select_dtypes(include=['number']).columns
x_axis = st.selectbox('X axis', numeric_columns, index=1)
y_axis = st.selectbox('Y axis', numeric_columns, index=2)
color = st.selectbox('Color', df.columns, index=3)

st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)
st.plotly_chart(fig)
