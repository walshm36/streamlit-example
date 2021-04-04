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
              color="Country/Region",
              title ="Covid-19 Cases"
             )

st.subheader('Graph: First Iteration')
st.write(fig)

st.subheader('Graph: Second Iteration')

c = alt.Chart(df).mark_area().encode(
    x="Date", y="1000 Cases",
    color="Country/Region"
).properties(
    width='container',
    height=400
)

st.altair_chart(c, use_container_width=True)

st.subheader('Graph: Third Iteration')

values = st.sidebar.slider("Date", [datetime.Date(2020, 3, 1), datetime.Date(2021, 2, 1)])
f = px.area(f.query(f”price.between{values}”), 
              x=”Date”,
              x=”1000 Cases”,
              color_discrete_sequence=px.colors.qualitative.Dark24,
              color="Country/Region",
              title ="Covid-19 Cases"
             )
st.plotly_chart(f)
