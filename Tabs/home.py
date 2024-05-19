import streamlit as st

def app():
    st.markdown('<style>h1 { color: Turquoise; }</style>', unsafe_allow_html=True)
    st.title('Lung Cancer Prediction')
    st.image('https://img.freepik.com/premium-photo/radiology-doctor-working-diagnose-treatment-virtual-human-lungs-long-covid-19_102957-1108.jpg?w=1380')
    st.markdown(
    """<p style="font-size:20px;">
            Lung cancer is a devastating disease characterized by uncontrolled cell growth in the tissues of the lungs. It is one of the most common and deadliest types of cancer worldwide. Early detection and accurate prediction of lung cancer are crucial for improving patient outcomes and guiding treatment decisions.
        </p>
    """, unsafe_allow_html=True)
