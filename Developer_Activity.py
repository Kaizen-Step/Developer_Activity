# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Developer Activity-Electric Capital Report',
                   page_icon=':bar_chart:', layout='wide')
st.title('Developer Activity')

# Content
c1, c2, c3 = st.columns(3)
c3.image(Image.open('Images/near-logo.png'), width=240)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.write("""  ## ⚡Electric Capital (Developer Report)""")
st.text(" \n")

st.write("""

### What is Electric Capital


Electric Capital is a crypto asset management firm focused on technology fundamentals. The company invests in tokens that are programmable money and invest in both liquid and illiquid tokens that are emerging stores of value and rooted in novel technology. Electric Capital is started by technology entrepreneurs, engineers, and successful investors. [Avichal Garg](https://www.linkedin.com/in/avichalgarg), defines himself as “an NFT maximalist,” who believes that nonfungible tokens (NFTs) will play an essential role in bringing crypto to the masses, is the CEO and co-founder of this firm. Learn more at [ElectricCapital.com](https://www.electriccapital.com/). 

### Electric Capital Developer Report ###
The fourth annual Electric Capital Developer Report was released with an in-depth analysis of the developer community around crypto. The report analyzed over 250 million code commits and sought input from over 300 individuals.  
Despite the crypto community having faced one of the most intense years on record in the industry, where prices fell an average of 70%, the developer community grew by 5%, according to the report.  
Ethereum boasts the largest developer community with over 5K total developers. NEAR developer community is growing quickly past 800 devs while multichain developers keep growing as well. Bitcoin, in contrast, has around 900 active monthly developers.  
A list of report highlights:  
* Monthly developers grew 5% year over year  
* Average of over 23,000 monthly developers  
* Over 100,000 developers have worked on crypto since 2021  
* Average of 471,000 monthly code commits  
* Average 3,900 monthly developers, specifically in Decentralized Finance (DeFi)  
* 61,000 new developers entered crypto in 2022  

Overall the growth across 2022 was slower than the bull runs through 2020 and 2021. However, the growth was consistent with previous bear markets lending credence to the concept of cycles in the crypto market.

For a full review of the report and Data, check out [Developer Report](https://developerreport.com/).

### How E.C Measure Developer Activity

An early and leading indicator of value creation in emerging platforms is developer engagement. 
Developers build killer applications that deliver value to end users, which attracts more customers, 
which then draws more developers.  
Because crypto is significantly open source, they have a unique and unprecedented ability to 
understand an emerging industry that may be worth many trillions.  
For the 2022 report, they analyzed 250M code commits. The taxonomy of projects is crowdsourced 
from , the foundations from many of the ecosystems, as well as CoinGecko, 
CoinMarketCap, DappRadar, DefiLlama, Github,Gitlab, and others. They infer non-original commits, which account for 65% of the total, and credit only the original 
authors and original ecosystems that produce code.  
The taxonomy of projects is available at our Github:   
 [github.com/electric-capital/crypto-ecosystems](github.com/electric-capital/crypto-ecosystems)


## Methodology
With Electric Capital’s release of its annual report on developer activity, the topic of “developers” is a hot topic across crypto.  
Produce a rich analysis of NEAR developer activity, using metrics and definitions of your choice to answer the questions:  
* How many developers are active on NEAR?
* How active are they?
* How this has changed over time?
Feel free to reference (and cite) the Electric Capital report to provide background  
To answer these questions we try to dive in Electric Capital developers report(2022 & 2021) for NEAR Ecosystem Data, we use plots and charts of this report to focus on NEAR 2022 developer comunity activity and compare it with other peers like Terra and Cosmos finnaly we use on chain data from Flipside Crypto Data Base table " near.beta.github_activity " to add Results to Electric Capital Report and make comparison over the results as possible.





""")

st.write("""   
##### Sources #####   """)
st.write("""    1.https://https://www.electriccapital.com/  
        2.https://www.bsc.news/post/electric-capital-developer-report  
        3.https://developerreport.com  
        4.https://www.linkedin.com/in/avichalgarg
      
              """)
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Project GuitHub:  [GuitHub](https://github.com/Kaizen-Step/Terra_Price_Run_Investigation)**', icon="💻")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Twitter:  [Ludvig.1989](https://flipsidecrypto.xyz/)**', icon="🦜")
