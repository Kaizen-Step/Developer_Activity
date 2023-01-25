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
st.set_page_config(page_title='Glossory - Developer Activity',
                   page_icon=':bar_chart:', layout='wide')
st.title('📜Glossory')

st.write(""" ## SQL Codes ## """)
# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write("""  In this dashboard, some comparisons are derived from [Mr. Hesam Inanloo's dashboard-Surge of Optimism](https://app.flipsidecrypto.com/dashboard/a-surge-of-optimism-QOVd_S) that analyzes Optimism token price over time.    

At the following links, you can find the SQL codes that are used in this dashboard: 

""")

# SQL Codes
st.write("""
1. https://app.flipsidecrypto.com/velocity/queries/830bbb73-4837-4302-bb3a-69a3ec13c1f5
2. https://app.flipsidecrypto.com/velocity/queries/6b354e38-ee84-4c7a-a57c-5cc320688ee1
3. https://app.flipsidecrypto.com/velocity/queries/5639fadf-49df-4a66-83b9-e94e3fec6c56
4. https://app.flipsidecrypto.com/velocity/queries/b9360da6-852c-4caf-885e-f3c1639b18ed
5. https://app.flipsidecrypto.com/velocity/queries/6cc96469-ed94-4d32-86de-b73d49565c5e
6. https://app.flipsidecrypto.com/velocity/queries/c3fb1a80-6d3f-4f25-ac4e-912cd1557db2


""")
