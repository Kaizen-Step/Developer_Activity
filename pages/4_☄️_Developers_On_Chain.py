# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Bridge - Near Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('☄️Developers')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Near_Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7a334f6d-78ac-412b-b3a2-a5d964317d0a/data/latest')
    elif query == 'Near_Overview2':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/684c459d-baf8-4f40-9e02-7a9b203c05c1/data/latest')
    elif query == 'Near_Overview3':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c35c6142-3216-4973-9aed-2b6c1a255e55/data/latest')
    elif query == 'Near_Merge_Close_Open':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/94d7fae6-5b46-4d3b-91dd-925cedb3d9e1/data/latest')
    elif query == 'NewRepo_Cumulative':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b1a6b6f2-e502-4b37-b40a-ee3a60a436fc/data/latest')
    elif query == 'Pull_requested':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ed66c235-2df4-452d-81a2-fecbcfc41d08/data/latest')
    elif query == 'Daily_PR_Number':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1195dba7-1104-484e-84e3-6d9e5d70ba9a/data/latest')
    elif query == 'Top10_Repo_PR':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/381491f5-fd68-49b5-81a9-922a62f2bec1/data/latest')
    elif query == 'top10_Author':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/597ad03e-7c4d-4a91-8820-813b3d3601c6/data/latest')
    elif query == 'Longest_Period':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d03ef29a-6b58-4ba8-b8f3-aaf342a026c5/data/latest')
    return None


Near_Overview = get_data('Near_Overview')
Near_Overview2 = get_data('Near_Overview2')
Near_Overview3 = get_data('Near_Overview3')
Near_Merge_Close_Open = get_data('Near_Merge_Close_Open')
NewRepo_Cumulative = get_data('NewRepo_Cumulative')
Pull_requested = get_data('Pull_requested')
Daily_PR_Number = get_data('Daily_PR_Number')
Top10_Repo_PR = get_data('Top10_Repo_PR')
top10_Author = get_data('top10_Author')
Longest_Period = get_data('Longest_Period')

st.text(" \n")
st.subheader('Overview')


df = Near_Overview
df2 = Near_Overview2
df3 = Near_Overview3
df4 = Near_Merge_Close_Open
df5 = NewRepo_Cumulative
df6 = Pull_requested
df7 = Daily_PR_Number
df8 = Top10_Repo_PR
df9 = top10_Author
df10 = Longest_Period

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(label='**Total Action**',
              value=str(df["TOTAL_ACTION"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Developer**',
              value=df["TOTAL_DEVELOPER"].map('{:,.0f}'.format).values[0])


with c2:
    st.metric(label='**Number of Repositories**',
              value=str(df["REPOSITORIES"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**GitHub Pages**',
              value=df["GITHUB_PAGES"].map('{:,.0f}'.format).values[0])

with c3:
    st.metric(label='**Average Time to Close Repo[Day]**',
              value=str(df2["Average time to close repo(Day)"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Max Time To Close Repo [Day]**',
              value=df2["max time to close repo(Day)"].map('{:,.0f}'.format).values[0])


# Number of PR in each State
fig = px.pie(df4, values="PR_STATE",
             names="STATE", title='Number of PR in each State', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# New Repositary with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df5["DATE"], y=df5["NEW_REPO"],
                     name='New Repo'), secondary_y=False)
fig.add_trace(go.Line(x=df5["DATE"], y=df5["CUM_NEW_REPO"],
                      name='CUMULATIVE Repo'), secondary_y=True)
fig.update_layout(
    title_text='New Repositary with Cumulative Value')
fig.update_yaxes(
    title_text='New Repo', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Repo', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly PR  by Author Association Category
fig = px.bar(df6.sort_values(["Create Date", "DAILY_PR"], ascending=[
    True, False]), x="Create Date", y="DAILY_PR", color="AUTHORASSOCIATION", title='Weekly PR  by Author Association Category ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly PR')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Repo by State Category
fig = px.bar(df6.sort_values(["Create Date", "COUNT (DISTINCT REPO)"], ascending=[
    True, False]), x="Create Date", y="COUNT (DISTINCT REPO)", color="STATE", title='Weekly Repo by State Category ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Repo')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Developer by Author Association Category
fig = px.bar(df6.sort_values(["Create Date", "COUNT (DISTINCT AUTHOR)"], ascending=[
    True, False]), x="Create Date", y="COUNT (DISTINCT AUTHOR)", color="AUTHORASSOCIATION", title='Weekly Developer by Author Association Category  ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Developer')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Developers By State  Category
fig = px.bar(df6.sort_values(["Create Date", "COUNT (DISTINCT AUTHOR)"], ascending=[
    True, False]), x="Create Date", y="COUNT (DISTINCT AUTHOR)", color="STATE", title='Weekly Developers By State  Category ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Developer')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Repo by Author Association Category
fig = px.bar(df6.sort_values(["Create Date", "COUNT (DISTINCT REPO)"], ascending=[
    True, False]), x="Create Date", y="COUNT (DISTINCT REPO)", color="AUTHORASSOCIATION", title='Weekly Repo by Author Association Category  ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly Repo')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly PR by State Category
fig = px.bar(df6.sort_values(["Create Date", "DAILY_PR"], ascending=[
    True, False]), x="Create Date", y="COUNT (DISTINCT REPO)", color="STATE", title='Weekly PR by State Category  ')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Weekly PR')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#  10 PR Title with Longest Period to Close(Day)
fig = px.bar(df7, x="TITLE", y="days left to close PR", color="TITLE",
             title=' 10 PR Title with Longest Period to Close(Day)')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='days left to close PR')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#  Top ten repo based on PR
fig = px.bar(df8, x="REPO", y="PR_AUTHOR", color="REPO",
             title=' Top ten repo based on PR')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Pr Author')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#  Top ten Author based on PR
fig = px.bar(df9, x="AUTHOR", y="PR_AUTHOR", color="AUTHOR",
             title=' Top ten Author based on PR')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Pr Author')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#   10 PR Title with Longest Period to Close(Day)
fig = px.bar(df10, x="TITLE", y="days left to close PR", color="TITLE",
             title='  10 PR Title with Longest Period to Close(Day)')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='days left to Close PR')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#################################################
