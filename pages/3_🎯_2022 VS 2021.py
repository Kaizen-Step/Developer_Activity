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


st.write(""" According to the CNBC All-America Economic Survey. Overall, the crypto market has lost a little over $2 trillion in 2022 and popular digital coins such as bitcoin have fallen far below their 2021 highs. Despite this huge fall developers activity in makret rise considerably as the new developer ever wrote open-source crypto code rose by 25% in this year.  """)

st.text(" \n")
st.write(' ## The Highest Number of New Developers')

st.write(""" 2022 saw the highest number of new crypto developers in history with 61,127 and it is almost 3 times as high as 2020 figure (21,615) which exprienced fall after 2018.  """)

st.write(""" """)

st.image(Image.open('Images/2022 VS 2021/5.png'))

st.write(""" NEAR’s 2022 was one of huge growth and innovation. New partnerships like Sweatcoin and SailGP were major stepping stones toward bringing Web3 to the masses. Projects in areas such as gaming, music, and NFTs showcased that the NEAR ecosystem is thriving and poised for new heights in 2023. """)

st.image(Image.open('Images/2022 VS 2021/2.png'))

st.text(" \n")
st.text(" \n")
st.text(" \n")


st.write(""" ## Near Two Years Scatter Graphs   """)

st.write(""" You can see 2020-2021 Near full-time developers scatter graph, NEAR was among ecosystems with more than 100 full-time developers and gained 4x developers compare to 2020 figure. """)

st.image(Image.open('Images/2022 VS 2021/2021_2.jpg'))

st.text(" \n")

st.write(""" In 2022 full time developers grow 22% but compare to 4x raise in 2021 it is not that significant. """)
st.image(Image.open('Images/2022 VS 2021/4.png'))

st.text(" \n")
st.text(" \n")
st.text(" \n")

st.write(""" ### Near Is One of The Fastest Growing Ecosystems  """)
st.write(""" Near ranked 4th with 307% on total monthly developers in 2021 but this trend is become slower in 2022 with only 33% growth . """)
st.text(" \n")

st.image(Image.open('Images/2022 VS 2021/1.png'))
st.text(" \n")
st.image(Image.open('Images/EC Report 2022/9.Full_Time_Dev_Zoom_in.jpg'))
