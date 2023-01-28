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
st.title('🔥Near In Electric Capital 2022 Report')


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

st.write(""" In this section, we try to dive deep into Electric Capital developer's Report findings about the Near ecosystem and make comparisons where ever is relevant. In this section term, Full-Time Developers are developers with 10+ days of contributions (Commit code in Guithub) in a month, Part-Time Developers are those with 2 to 9 days of contributions, and finally, One-Time Developers contribute only once in a month. GitHub is an online software development platform; used for storing, tracking, and collaborating on software projects. A commit, or "revision," is an individual change to undergoing project file (or set of files). A repository contains all of your project's files and each file's revision history. You can discuss and manage your project's work within the repository.  """)

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
st.write(' ### Monthly Active Developers')

st.write("""  Monthly part-time developers hit a peak of 632 on May 20, 2022, and the one-time developer's figure reached its peak in the same month. Both experienced significant falls until the end of 2022, while Monthly full-time developers remained relatively unchanged for the whole of 2022, starting the year with 198 and finishing it with 205. """)

st.image(Image.open(
    'Images/Near Dashboard 2022/Near_Monthly_Active_Dev_Type.jpg'))

st.image(Image.open('Images/Near Dashboard 2022/Near_Dev_Data_table.jpg'))

st.text(" \n")
st.text(" \n")
st.write(' ### Monthly Commits')

st.write(""" Although the full-time developers were almost 1/3 of part-time Devs in number, they accounted for 78% of monthly commits in 2022 and reached the peak of 12,414 monthly commits on May 16. Unfortunately, for the second half of 2022, the number of commits fell significantly, regardless of the type of developers.   """)

st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_Type.jpg'))
st.text(" \n")
st.image(Image.open('Images/Near Dashboard 2022/Near_Monthly_Commit_All.jpg'))


st.text(" \n")
st.text(" \n")
st.text(" \n")
st.text(" \n")


st.write(' # Near Among Top 200 Ecosystems')
st.text(" \n")
st.write(""" In the Electrical Capital 2022 developer report, ecosystems are divided into three groups, Bitcoin and Ethereum as pioneers, the top 200 Ecosystems except for Bitcoin and Ethereum as top 200, and finally, all other lower-ranked ecosystems as others. Near is among the 200 top ecosystems. as you can see in the following Normalized chart, 50% of Total Developers worked on the top 200 ecosystems projects, and 30% worked on Bitcoin and Ethereum. 
""")
st.text(" \n")
st.image(Image.open('Images/EC Report 2022/1.Ecosystem_Type.jpg'))

st.text(" \n")
st.text(" \n")
st.write(' ### Full time Developers Gained or Lost ?')

st.write(""" Ethereum, with more than 1800 full-time developers, ranked first among all Ecosystems. In the following chart, you can find the full-scale comparison between ecosystems: for a better understanding of the top 200, which Near is among them, we focused on a certain part of the graph to observe Near figures better.  """)

st.image(Image.open('Images/EC Report 2022/2.Full_Scale.jpg'))
st.text(" \n")
st.write(""" With a 22% rise in full-time developers compared to last year's figure, Near is one of the successful Eco to attract full-time developers despite a significant drop in the whole market.  """)

st.image(Image.open('Images/EC Report 2022/3.Near_Full_Time_Devs.jpg'))

st.text(" \n")
st.text(" \n")
st.write(' ### Near Total Developers Growth Since 2018')


st.write(' In 2018, less than 50 developers worked on the  Near ecosystem, but with more than 800 developers in 2022, Near is one of the most successful ecosystems among top200; as you can see in the below graph total Number of developers rose by more than 15 times, and it is a record for Near.')

st.image(Image.open('Images/EC Report 2022/5.Near_Growth_Total_Devs.jpg'))
st.text(" \n")

st.write(' Near full-time developers grew more than 20 times during the last four years and ranked 2nd after Polygan enormous growth.')


st.image(Image.open('Images/EC Report 2022/4.Near_Growth_Since2018.jpg'))

st.text(" \n")
st.text(" \n")
st.text(" \n")

st.write(' ## Ecosystems since Lauched Time Comparison')
st.write('Near full-time developers grew more than 20 times during the last four years and ranked 2nd after Polygan enormous growth. Except for Bitcoin and Ethereum, all top 200 ecosystems launched less than seven years: NEAR launched its genesis (Phase 0) on April 22, 2020, and became community-operated (Phase I) on September 24, as you can see in below charts Near ranked 6th after Polkadot, Cosmos, Solanas, Polygan and Kusama in the number of full-time developers with 205 in 2022.     ')

st.image(Image.open('Images/EC Report 2022/6.Launched_time_Comparison.jpg'))

st.text(" \n")

st.image(Image.open('Images/EC Report 2022/4.Near_Growth_Since2018.jpg'))

st.write('As you can see in the above chart focused on Near that contian the Near 205 full-time developers and more than 20x growth compared to 2021. ')

st.text(" \n")
st.text(" \n")

st.write(' ## Fastest Emerging Ecosystems')
st.text(" \n")

st.write(' Near is among the fastest ecosystems, which has grown to more than 150 developers in less than four years. Solana, Polygan, Kusama, BNB and Near took fewer than four years to develop to more than 150 developers but Near, with less than two years since launched, did a promising job. ')

st.image(Image.open('Images/EC Report 2022/9.Full_Time_Dev_Zoom_in.jpg'))

st.image(Image.open('Images/EC Report 2022/11.Total_Devs_Full_Scale.jpg'))
st.text(" \n")
st.write(' Near with 800 total developers, ranked 3rd among top Ecosystems excel Bitcoin and Ethereum.')
st.image(Image.open('Images/EC Report 2022/12.Most_Total_Devs.jpg'))
st.text(" \n")

st.text(" \n")
st.text(" \n")


st.write(' ### How Long Does It Takel For Near to Grow to +1000 Developers ?')
st.text(" \n")
st.write(" Near is among fast upcoming ecosystems, but how long do we have to wait to see Near among a few ecosystems with more than 1000 developers, I believe it's not that much, and the future will be brighter and full of good opportunities for Near.     ")
st.image(Image.open('Images/EC Report 2022/10.1000Devs_Path.jpg'))
st.text(" \n")
