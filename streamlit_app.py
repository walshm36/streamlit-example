from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px


st.title('Maeves Covid Dashboard')                    

DATA_URL = ('melted_cases.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

# show data on streamlit
st.write(df)

#graph
fig = px.area(df, x="Date", y="1000 Cases", color="Country/Region")
fig.show()
