import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')

df = px.data.tips()

def page1(df):
    time = st.sidebar.radio('Select Time', df['time'].unique())
    df = df[df['time'] == time]

    st.header("Box Plot of Total Bill by Time")
    st.plotly_chart(px.box(df, x="total_bill", title="Total Bill Distribution"))

def page2(df):
    sex = st.sidebar.selectbox('Select Sex', df['sex'].unique())
    df = df[df['sex'] == sex]

    st.header("Histogram of Total Bill by Sex")
    st.plotly_chart(px.histogram(df, x="total_bill", title="Total Bill Distribution"))

def page3(df):
    smoker = st.sidebar.radio('Select Smoker', df['smoker'].unique())
    df = df[df['smoker'] == smoker]

    st.header("Violin Plot and Scatter Plot for Total Bill & Tip")
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Violin Plot", "Scatter Plot"))

    fig.add_trace(go.Violin(x=df['smoker'], y=df['total_bill'], name="Total Bill"), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['total_bill'], y=df['tip'], mode='markers', name="Total Bill vs. Tip"), row=1, col=2)

    st.plotly_chart(fig)

pgs = {
    'Time': page1,
    'Sex': page2,
    'Smoker': page3
}

pg = st.sidebar.radio('Navigate Pages', options=pgs.keys())
pgs[pg](df)
