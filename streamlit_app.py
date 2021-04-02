from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
pip freeze   # optional: this is to check current installed package
pip install plotly --upgrade   # this to update plotly to latest version, at the time of this post: 4.5.4
pip install plotly   # might be unnecessary, but I did this
import plotly.express as xp   # now it works


st.title('Maeves Covid Dashboard')                    

DATA_URL = ('melted_cases.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

st.write(df)

fig = px.area(df, x="Date", y="1000 Cases", color="Country/Region")

st.write(fig)
