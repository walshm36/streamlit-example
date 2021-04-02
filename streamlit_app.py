from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.title('Maeves Covid Dashboard')

DATA_URL = ('https://github.com/walshm36/streamlit-example/blob/762bfb00f06a5561781344d1136efd0edb8a221f/melted_cases.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

st.subheader('Raw data')
st.write(data)
