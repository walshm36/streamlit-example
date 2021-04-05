from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly as py
import plotly.express as px
import plotly.io as pio
import matplotlib as plt
import datetime as dt

st.title('Maeves Covid Dashboard :sunglasses:')        

DATA_URL = ('melted_cases.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

st.subheader('Raw data')
st.write(df)

st.header("Cases Growth") 

fig = px.area(df, x="Date", y="1000 Cases", 
              color_discrete_sequence=px.colors.qualitative.Dark24,
              color="Country_Region",
              title ="Covid-19 Cases"
             )

st.subheader('Graph: First Iteration')
st.write(fig)

st.subheader('Graph: Second Iteration')

c = alt.Chart(df).mark_area().encode(
    x="Date", y="1000 Cases",
    color="Country_Region"
).properties(
    width='container',
    height=400
)

st.altair_chart(c, use_container_width=True)

fig2 = px.choropleth(data_frame = df, 
                    locations= "iso_alpha",
                    color= "1000 Cases", 
                    hover_name= "Country_Region",
                    color_continuous_scale= 'balance', 
                    animation_frame= "Date")

st.subheader('Graph: Third Iteration')
st.write(fig2)



