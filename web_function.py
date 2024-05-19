import numpy as np
import pandas as pd
import streamlit as st
from keras.models import load_model
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from PIL import Image

@st.cache_data
def image_processing(uploaded_image):
    # Đọc ảnh và chuyển đổi sang định dạng mà mô hình yêu cầu
    image = Image.open(uploaded_image)
    image = image.resize((256, 256))  # Đảm bảo kích thước đầu vào đúng với kích thước mà mô hình đã được huấn luyện
    image_array = np.array(image) / 255.0  # Chuẩn hóa giá trị pixel về khoảng [0, 1]
    image_array = np.expand_dims(image_array, axis=0)  # Thêm một chiều cho batch
    return image_array


@st.cache_resource
def vgg16_model(image_array):
    # Đường dẫn đến tệp mô hình
    vgg16_path = 'D:\\KPDL\\UI\\testmodel\\lung_model4.h5'

    # Load mô hình từ tệp
    vgg16_model = load_model(vgg16_path)

    # Dự đoán lớp của ảnh
    predictions = vgg16_model.predict(image_array)
    print(predictions)
    # Lấy lớp dự đoán và xác suất tương ứng
    predicted_class = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class]

    return predicted_class, confidence

