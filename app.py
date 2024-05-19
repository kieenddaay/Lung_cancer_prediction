import streamlit as st
from Tabs import home, predict, about, history

### TITLE
st.set_page_config(
    page_title='LCP', 
    page_icon=':lungs:',
    layout = 'wide',
)

### DICTIONARY FOR PAGES
Tabs = {
    "Home": home,
    "Prediction": predict,
    # "History Check": history,
    "About": about
}

### SIDEBAR
st.sidebar.markdown(
    """<p style="font-size:30px; color:white; font-weight:bold;" >
           NAVIGATION
        </p>
    """, unsafe_allow_html=True
)

# background
sidebar_bg = '''
    <style>
    [data-testid=stSidebar] {
    background-image: url("https://img.freepik.com/free-photo/human-lungs-anatomy-3d-illustration-vintage-style-toned_1057-36441.jpg?t=st=1715522989~exp=1715526589~hmac=3c83adcd740a76ad32ef6275cc0a7358336288cc7557a35adfd851455ec2158d&w=740");
    background-size: cover;
    }
    </style>
'''
st.sidebar.markdown(sidebar_bg, unsafe_allow_html=True)

# option to navigate
page = st.sidebar.radio("Pages", list(Tabs.keys()))
Tabs[page].app()