from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
pip install plotly_express


st.title('Maeves Covid Dashboard')                    

DATA_URL = ('melted_cases.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

st.write(df)
