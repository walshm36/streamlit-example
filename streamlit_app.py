from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.title('Maeves Covid Dashboard')
                       

df = pd.read_csv(".Desktop/Project/melted.csv")  

st.title("Hello world!")  # add a title
st.write(df)
