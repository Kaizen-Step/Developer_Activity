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
st.set_page_config(page_title='Near In EC 2022 Report - Developer Activity',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈Near In Electric Capital 2022 Report')


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


st.write(""" In this Dashboard term Full-Time Developers are developers who have 10+ days of contributions (Commit code in Guithub) in a month, Part-Time Developer are those who have 2 to 9 days of contributions and finaly One-Time Developers are contribute only once. """)

st.text(" \n")
st.write(' ## Overview')


df = Overview_Total_Contracts
df2 = Overview_NearTX
df3 = Overview_Contract_Deployed

c1, c2 = st.columns(2)
with c1:
    st.image(Image.open('Images/Near Dashboard 2022/Near_Full_time_Devs.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Total_Repos.jpg'))
with c2:
    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Active_Devs.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Total_Commits.jpg'))

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Monthly Active Developers')
st.text(" \n")

st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Active_Dev_Type.jpg'))
st.text(" \n")
st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Active_Dev_All.jpg'))
st.text(" \n")
st.image(Image.open('Images/Near Dashboard 2022/Near_Dev_Data_table.jpg'))


st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Monthly Commits')
st.text(" \n")

st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_Type.jpg'))
st.text(" \n")
st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_All.jpg'))


st.write(' ## Near Among Top 200 Ecosystems')

st.write(""" In this Dashboard (Ether_Bitcoin, top 200, others)
""")
st.text(" \n")
st.image(Image.open('Images/EC Report 2022/1.Ecosystem_Type.jpg'))


st.write(' ### Full time Developers in different Ecosystems')

st.image(Image.open('Images/EC Report 2022/2.Full_Scale.jpg'))
st.text(" \n")
st.image(Image.open('Images/EC Report 2022/3.Near_Full_Time_Devs.jpg'))

st.write(' ### Near Total Developers Growth Since 2018')
st.text(" \n")

st.image(Image.open('Images/EC Report 2022/5.Near_Growth_Total_Devs.jpg'))

st.write(' ### Near Full-Time Developers Growth Since 2018')
st.text(" \n")

st.image(Image.open('Images/EC Report 2022/4.Near_Growth_Since2018.jpg'))

st.write(' ### Ecosystems Lauch Time Comparison')
st.text(" \n")

st.image(Image.open('Images/EC Report 2022/6.Launched_time_Comparison.jpg'))


st.image(Image.open('Images/EC Report 2022/4.Near_Growth_Since2018.jpg'))

st.write(' ### Full-Time Developers Since Launched')
st.text(" \n")

st.image(Image.open('Images/EC Report 2022/8.Full_Time_Dev_Full_Scale.jpg'))
st.text(" \n")
st.image(Image.open('Images/EC Report 2022/9.Full_Time_Dev_Zoom_in.jpg'))

st.write(' ### Ecosystems with 1000 Full-Time Developers')
st.text(" \n")

st.image(Image.open('Images/EC Report 2022/10.1000Devs_Path.jpg'))
st.text(" \n")

st.write(' ### Total Developers Since Launched')
st.text(" \n")

st.image(Image.open('Images/EC Report 2022/11.Total_Devs_Full_Scale.jpg'))
st.text(" \n")
st.image(Image.open('Images/EC Report 2022/12.Most_Total_Devs.jpg'))
st.text(" \n")
