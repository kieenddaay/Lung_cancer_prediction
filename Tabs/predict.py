import streamlit as st
from web_function import image_processing, vgg16_model, storeMongo

def app():
    st.markdown('<style>h1 { color: lightgreen; }</style>', unsafe_allow_html=True)
    st.title("Prediction")

    st.subheader('Upload an image')
    uploaded_image = st.file_uploader("upload here", type=["jpg", "jpeg", "png"])

    # check button to pass input to model
    if uploaded_image is not None:
        st.image(uploaded_image, caption='Uploaded image') 
        check_button = st.button("check", key='checkBtn')
        if check_button:
            uploaded_image = image_processing(uploaded_image=uploaded_image)
            vgg16_load_model = vgg16_model(uploaded_image)
            predicted_class = vgg16_load_model[0]
            confidence = vgg16_load_model[1]

            st.write('Predicted class:', predicted_class)
            st.write('Confidence:', confidence)

            if predicted_class == 0:
                st.warning('You may have lung cancer!😭🙏')
            elif predicted_class == 1:
                st.error('You have lung cancer💀👻')
            else:
                st.success('You are okay bro💪😏👍')

            storeMongo(uploaded_image, predicted_class, confidence)