from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.title('Maeves Covid Dashboard')
"""
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
"""
DATA_URL = ('https://github.com/walshm36/streamlit-example/blob/762bfb00f06a5561781344d1136efd0edb8a221f/melted_cases.csv')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

