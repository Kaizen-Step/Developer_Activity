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


# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Refrences
st.write(""" ## Refrences ## """)

st.write("""  In this dashboard, Electric Capital charts and graphs are used for 'Near in EC 2022'  and "Near VS peer' tab for full EC 2022 developer report review you can visit the website ([Developer Report](https://developerreport.com/)) and also the PDF file that provided. For the other tabs orginal SQL code written that used [Flipside Crypto](https://flipsidecrypto.xyz/) massive data base.  
""")


# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


st.write("""
1. https://app.flipsidecrypto.com/velocity/queries/830bbb73-4837-4302-bb3a-69a3ec13c1f5
2. https://app.flipsidecrypto.com/velocity/queries/6b354e38-ee84-4c7a-a57c-5cc320688ee1
3. https://app.flipsidecrypto.com/velocity/queries/5639fadf-49df-4a66-83b9-e94e3fec6c56
4. https://app.flipsidecrypto.com/velocity/queries/b9360da6-852c-4caf-885e-f3c1639b18ed
5. https://app.flipsidecrypto.com/velocity/queries/6cc96469-ed94-4d32-86de-b73d49565c5e
6. https://app.flipsidecrypto.com/velocity/queries/c3fb1a80-6d3f-4f25-ac4e-912cd1557db2
7. https://app.flipsidecrypto.com/velocity/queries/597ad03e-7c4d-4a91-8820-813b3d3601c6
8. https://app.flipsidecrypto.com/velocity/queries/d03ef29a-6b58-4ba8-b8f3-aaf342a026c5
9. https://app.flipsidecrypto.com/velocity/queries/381491f5-fd68-49b5-81a9-922a62f2bec1
10. https://app.flipsidecrypto.com/velocity/queries/1195dba7-1104-484e-84e3-6d9e5d70ba9a
11. https://app.flipsidecrypto.com/velocity/queries/ed66c235-2df4-452d-81a2-fecbcfc41d08
12. https://app.flipsidecrypto.com/velocity/queries/b1a6b6f2-e502-4b37-b40a-ee3a60a436fc
13. https://app.flipsidecrypto.com/velocity/queries/94d7fae6-5b46-4d3b-91dd-925cedb3d9e1
14. https://app.flipsidecrypto.com/velocity/queries/c35c6142-3216-4973-9aed-2b6c1a255e55
15. https://app.flipsidecrypto.com/velocity/queries/684c459d-baf8-4f40-9e02-7a9b203c05c1
16. https://app.flipsidecrypto.com/velocity/queries/7a334f6d-78ac-412b-b3a2-a5d964317d0a
17. https://app.flipsidecrypto.com/velocity/queries/6523a238-75a4-4d57-8104-c4b4ad486867
18. https://app.flipsidecrypto.com/velocity/queries/37022a6b-4b75-41fc-9d62-5172b46a8b05
19. https://app.flipsidecrypto.com/velocity/queries/0fa27680-ed8b-4fe5-8806-ddc6670cfcfb
20. https://app.flipsidecrypto.com/velocity/queries/c705f29c-28e5-4867-8009-899b252c7d3c
21. https://app.flipsidecrypto.com/velocity/queries/76234e77-ea51-41c7-9175-d91b4dfe6681
22. https://app.flipsidecrypto.com/velocity/queries/e8319f1b-829a-4295-a6ec-a87969c57a73

""")


st.write(""" ## Gratitude ## """)
st.write(""" Finally there are many more crypto developers than are accounted for in our report. Some teams are working on closed-source projects or deploy their code on-chain without ever open sourcing their contracts. We also undercount developers in roles such as backporting, testing, or release engineering as their efforts may not result in unique code contributions. Some teams first work in a closed source environment, then open-source their code later. It requires more than just software engineers to build 
crypto products that reach mainstream adoption, so this is a dramatic undercounting of the number of people building in crypto.
""")
