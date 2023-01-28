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
st.title('🌌Near Vs Peers')


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


st.write(""" In this section we try to compare Near with 2 other ecosystems (Cosmos and Terra). First we review the total 2022 figures then we tried to compare the trends. Cosmos generally had higher figures with the  511 full-time developer which is more than 2times higher than Near figure, while Terra with devestating exprienced this year had a only 7 full-time developers. the Repositeries did not follow the developer number pattern and there is only 796 difference between Near and Cosmos. """)

st.text(" \n")
st.write(' ## Overview')


df = Overview_Total_Contracts
df2 = Overview_NearTX
df3 = Overview_Contract_Deployed

c1, c2, c3 = st.columns(3)
with c1:
    st.write(""" ### Near  """)
    st.image(Image.open('Images/Near Dashboard 2022/Near_Full_time_Devs.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Total_Repos.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Active_Devs.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Total_Commits.jpg'))
with c2:
    st.write(""" ### Terra  """)
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Full_time_Devs.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Total_Repos.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Monthly_Active_Devs.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Total_Commits.jpg'))
with c3:
    st.write(""" ### Cosmos  """)
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Full_Time_Devs.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Total_Repos.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Monthly_Active_Devs.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Total_Commits.jpg'))

st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Near Compared to Terra')
st.text(" \n")


st.write(""" It is obvious that Terra did not exprience good year and with loss of 70% in number of full-time developers in one year needs, while Near exprineced 16% growth with the same figure.  """)

c1, c2 = st.columns(2)


with c1:
    st.write(""" #### Near Charts """)
    st.image(Image.open(
        'Images/Near Dashboard 2022/Near_Monthly_Active_Dev_Type.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Active_Dev_All.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Dev_Data_table.jpg'))

with c2:
    st.write(""" #### Terra Charts """)
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Monthly_Active_Developres_Type.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Monthly_Active_Developres_All.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Developers_Data_Table.jpg'))


st.write(""" The flactuation in Terra line graph is continued until 2022, while there was obvious uprising trend in all Near charts despite the 2022 whole market drop. """)


c1, c2 = st.columns(2)

with c1:

    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_Type.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_All.jpg'))

with c2:

    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Monthly_Commits_Type.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Terra_Total_Commits_all.jpg'))


st.text(" \n")
st.text(" \n")
st.text(" \n")
st.subheader('Near Compared to Cosmos')
st.text(" \n")

st.write(""" For Cosmos it took almost 6 years to grow to more than 500 developers but Near took this path with only 2 years. Although, the total and full-time developers figures of Cosmos was higher than Near, Near uprising trend had more steep than Cosmos. """)

st.image(Image.open('Images/Compare to other dash 2022/7.Cosmos_Polkadot_Growth.jpg'))


c1, c2 = st.columns(2)


with c1:
    st.write(""" #### Near Charts """)
    st.image(Image.open(
        'Images/Near Dashboard 2022/Near_Monthly_Active_Dev_Type.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Active_Dev_All.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Dev_Data_table.jpg'))

with c2:
    st.write(""" #### Cosmos Charts """)
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Monthly_Active_Type.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Monthly_Active_All.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Developers_Data_Table.jpg'))


st.write(""" In the Commits also Cosmos figures showed the better performance and total Cosmos commits are more than 2 time higher than Near Commits (5,583,259 and 1,783,233, respectively).  """)


c1, c2 = st.columns(2)

with c1:

    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_Type.jpg'))
    st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_All.jpg'))

with c2:

    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Monthly_Commits_Type.jpg'))
    st.image(Image.open(
        'Images/Compare to other dash 2022/Cosmos_Monthly_Commits_All.jpg'))
