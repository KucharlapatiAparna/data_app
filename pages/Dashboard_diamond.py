import streamlit as st
from matplotlib import image
import plotly.express as px
import pandas as pd
import os
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "diamond.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data1", "diamonds.csv")

st.title("Dashboard Diamond Dataset")
img=image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.header('Data frame')
st.dataframe(df)

cut = st.selectbox("Select the type of cut:", df['cut'].unique())
col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['cut'] == cut], x="price")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['cut'] == cut], y="price")
col2.plotly_chart(fig_2, use_container_width=True)

color = st.selectbox("Select the color:", df['color'].unique())
col3, col4 = st.columns(2)

fig_1 = px.histogram(df[df['color'] == color], x="price")
col3.plotly_chart(fig_1, use_container_width=True)


fig_2 = px.box(df[df['color'] == color], y="price")
col4.plotly_chart(fig_2, use_container_width=True)

clarity = st.selectbox("Select the clarity:", df['clarity'].unique())
col5, col6 = st.columns(2)

fig_1 = px.histogram(df[df['clarity'] == clarity], x="price")
col5.plotly_chart(fig_1, use_container_width=True)


fig_2 = px.box(df[df['clarity'] == clarity], y="price")
col6.plotly_chart(fig_2, use_container_width=True)


