from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly as py
import plotly.express as px
import plotly.io as pio

st.title('Maeves Covid Dashboard :sunglasses:')                    

DATA_URL = ('melted_cases.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

st.subheader('Raw data')
st.write(df)

fig = px.area(df, x="Date", y="1000 Cases", 
              color_discrete_sequence=px.colors.qualitative.Dark24,
              color="Country/Region",
              title ="Covid-19 Cases",
             # template="plotly_white"
             )

st.selectbox('Select', ["Country/Region"])
st.subheader('Graph: First Iteration')
st.write(fig)
