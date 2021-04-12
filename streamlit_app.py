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

#st.beta_set_page_config(layout="wide")
st.title('Maeves Covid Dashboard :sunglasses:')        

DATA_URL = ('melted_cases.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()

st.header("Cases Growth") 

fig = px.area(df, x="Date", y="1000 Cases", 
              color_discrete_sequence=px.colors.qualitative.Dark24,
              color="Country_Region",
              title ="Covid-19 Cases"
             )



fig2 = px.choropleth(data_frame = df, 
                    locations= "iso_alpha",
                    color= "1000 Cases", 
                    hover_name= "Country_Region",
                    color_continuous_scale= 'YlOrRd', 
                    animation_frame= "Date")



#col1, col2 = st.beta_columns(2)

#col1.
st.subheader("Daily Cases :mask:")
#col1
st.write(fig, use_column_width=True)
st.date_input('Date input')
st.multiselect('Multiselect', df["Country_Region"])


#col2
st.subheader("Global Cases :earth_africa:")
#col2
st.write(fig2, use_column_width=True)
#with st.beta_expander("See explanation"):
 #    st.write("""
  #       Cases emerging each day
   #  """)


#st.subheader('Raw data')
#st.write(df)


