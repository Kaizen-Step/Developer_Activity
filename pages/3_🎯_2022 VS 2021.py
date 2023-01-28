# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Near VS Peers - Developer Activity',
                   page_icon=':bar_chart:', layout='wide')
st.title('🎯2022 VS 2021')


# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources

@st.cache()
def get_data(query):
    if query == 'Overview_Total_Contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d02e98af-3135-42ab-9944-595940ba8dba/data/latest')
    elif query == 'Overview_NearTX':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1d7988f8-5b04-4e61-87fb-fde67fa81633/data/latest')
    elif query == 'Overview_Contract_Deployed':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/aecb2cbd-9f9c-4a69-97eb-5a0a13cf04c6/data/latest')

    return None


Overview_Total_Contracts = get_data('Overview_Total_Contracts')
Overview_NearTX = get_data('Overview_NearTX')
Overview_Contract_Deployed = get_data('Overview_Contract_Deployed')

df = Overview_Total_Contracts
df2 = Overview_NearTX
df3 = Overview_Contract_Deployed


st.write(""" In this Dashboard term Full-Time Developers are developers who have 10+ days of contributions (Commit code in Guithub) in a month, Part-Time Developer are those who have 2 to 9 days of contributions and finaly One-Time Developers are contribute only once. """)

st.text(" \n")
st.write(' ## The Highest Number of New Developers')


st.write(""" """)

st.image(Image.open('Images/2022 VS 2021/5.png'))

st.write(""" In this Dashboard term Full-Time Developers are developers who have 10+ days of contributions (Commit code in Guithub) in a month, Part-Time Developer are those who have 2 to 9 days of contributions and finaly One-Time Developers are contribute only once. """)

st.image(Image.open('Images/2022 VS 2021/2.png'))


st.write(""" ### Near  """)
st.image(Image.open('Images/2022 VS 2021/3.png'))
st.image(Image.open('Images/2022 VS 2021/4.png'))

st.write(""" ### Near  """)
st.image(Image.open('Images/2022 VS 2021/1.png'))
