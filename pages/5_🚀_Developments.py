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
st.set_page_config(page_title='Development - Developer Activity',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Developments')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'NewContracts_Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5639fadf-49df-4a66-83b9-e94e3fec6c56/data/latest')
    elif query == 'NewContracts_Daily_Weekly_Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6b354e38-ee84-4c7a-a57c-5cc320688ee1/data/latest')
    elif query == 'WeeklyTopContracts_Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/830bbb73-4837-4302-bb3a-69a3ec13c1f5/data/latest')
    elif query == 'WeeklyTopContracts_Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b9360da6-852c-4caf-885e-f3c1639b18ed/data/latest')
    elif query == 'Overview_Total_Number_Contracts':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6cc96469-ed94-4d32-86de-b73d49565c5e/data/latest')
    elif query == 'Active_ContractsDaily_Weekly_Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c3fb1a80-6d3f-4f25-ac4e-912cd1557db2/data/latest')
    return None


NewContracts_Overview = get_data('NewContracts_Overview')
NewContracts_Daily_Weekly_Monthly = get_data(
    'NewContracts_Daily_Weekly_Monthly')
WeeklyTopContracts_Transactions = get_data('WeeklyTopContracts_Transactions')
WeeklyTopContracts_Users = get_data('WeeklyTopContracts_Users')
Overview_Total_Number_Contracts = get_data('Overview_Total_Number_Contracts')
Active_ContractsDaily_Weekly_Monthly = get_data(
    'Active_ContractsDaily_Weekly_Monthly')


st.text(" \n")
st.subheader('Overview')


df = NewContracts_Overview
df2 = NewContracts_Daily_Weekly_Monthly
df3 = WeeklyTopContracts_Transactions
df4 = WeeklyTopContracts_Users
df5 = Overview_Total_Number_Contracts
df6 = Active_ContractsDaily_Weekly_Monthly


c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Average New contracts per Quarter**',
              value=str(df["New contracts per Quarter"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**2022 new contracts**',
              value=str(df["NEW_CONTRACTS"].map('{:,.0f}'.format).values[0]))
with c2:
    st.metric(label='**Average New contracts per Month**',
              value=str(df["New contracts per Month"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Total Number of Contracts**',
              value=str(df5["total Number of contracts"].map('{:,.0f}'.format).values[0]))


st.text(" \n")
st.text(" \n")
st.text(" \n")


st.write(""" ## New Contracs Deployed Over time ### """)

st.write("""   """)

# Daily New Contract Deployed
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DAily"], y=df2["NEW_CONTRACTS"],
                     name="Daily New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DAily"], y=df2["CUM_NEW_CONTRACTS_DAILY"],
                      name="Cumulative New Contract"), secondary_y=True)
fig.update_layout(
    title_text='Daily New Contract Deployed')
fig.update_yaxes(
    title_text="Daily New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly New Contract Deployed
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["Weekly"], y=df2["NEW_CONTRACTS"],
                     name="Weekly New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df2["Weekly"], y=df2["CUM_NEW_CONTRACTS_WEEKLY"],
                      name="Cumulative New Contract"), secondary_y=True)
fig.update_layout(
    title_text='Weekly New Contract Deployed')
fig.update_yaxes(
    title_text="Weekly New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Monthly New Contract Deployed
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["Monthly"], y=df2["NEW_CONTRACTS"],
                     name="Monthly New Contract"), secondary_y=False)
fig.add_trace(go.Line(x=df2["Monthly"], y=df2["CUM_NEW_CONTRACTS_MONTHLY"],
                      name="Cumulative New Contract"), secondary_y=True)
fig.update_layout(
    title_text='Monthly New Contract Deployed')
fig.update_yaxes(
    title_text="Monthly New Contract", secondary_y=False)
fig.update_yaxes(title_text="Cum New Contract", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ### Most Popular Contracts ### """)


# Most popular Contracts Based on Transactions
fig = px.pie(df3, values="COUNT",
             names="CONTRACT", title='Most popular Contracts Based on Transactions', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Weekly Top Contracts Based on Transactions
fig = px.bar(df3.sort_values(["DATE", "COUNT"], ascending=[
    True, False]), x="DATE", y="COUNT", color="CONTRACT", title='Weekly Top Contracts Based on Transactions')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='TX Number')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Most popular Contract based on Users
fig = px.pie(df4, values="USERS",
             names="CONTRACT", title='Most popular Contract based on Users', hole=0.5)
fig.update_layout(legend_title=None, legend_y=0.5)
fig.update_traces(textinfo='percent+value', textposition='inside')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Top Contracts Based on Users
fig = px.bar(df4.sort_values(["DATE", "USERS"], ascending=[
    True, False]), x="DATE", y="USERS", color="CONTRACT", title='Weekly Top Contracts Based on Users')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Number of Users')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(""" ### Active Contracts ### """)

# Daily Active Contract
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df6["DAily"], y=df6["ACTIVE_CONTRACT"],
                     name="Daily Active Contract"), secondary_y=False)
fig.update_layout(
    title_text='Daily Active Contract')
fig.update_yaxes(
    title_text="Daily Active Contract", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Weekly Active Contract
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df6["Weekly"], y=df6["ACTIVE_CONTRACT"],
                     name="Weekly Active Contract"), secondary_y=False)
fig.update_layout(
    title_text='Weekly Active Contract')
fig.update_yaxes(
    title_text="Weekly Active Contract", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Monthly Active Contract
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df6["Monthly"], y=df6["ACTIVE_CONTRACT"],
                     name="Monthly Active Contract"), secondary_y=False)
fig.update_layout(
    title_text='Monthly Active Contract')
fig.update_yaxes(
    title_text="Monthly Active Contract", secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
