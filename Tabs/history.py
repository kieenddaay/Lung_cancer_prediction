import streamlit as st

def app():
    st.markdown('<style>h1 { color: GoldenRod; }</style>', unsafe_allow_html=True)
    st.title('History check')
    phoneNumber = st.text_input("Enter your phone number", key='historyCheck')
    submit_button = st.button("Check", key='historyBtn')

    if phoneNumber.strip() == "":
        st.error("Please enter your phone number!")
    else:
        if submit_button:
            pass # api call back to see history check

    