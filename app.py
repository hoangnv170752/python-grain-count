import streamlit as st
import cv2
import numpy as np
from src.image_processing import preprocess_image
from src.grain_counter import count_grains

def main():
    st.title("Phát Hiện và So Sánh Số Lượng Hạt")
    
    st.sidebar.header("Tải Lên Hình Ảnh")
    
    col1, col2 = st.columns(2)
    
    with st.sidebar:
        uploaded_file1 = st.file_uploader(
            "Chọn hình ảnh thứ nhất...", 
            type=["jpg", "jpeg", "png"],
            key="file1"
        )
        
        uploaded_file2 = st.file_uploader(
            "Chọn hình ảnh thứ hai...", 
            type=["jpg", "jpeg", "png"],
            key="file2"
        )
    
    if uploaded_file1 is not None:
        with col1:
            st.header("Hình Ảnh 1")
            process_image(uploaded_file1, "Hình Ảnh 1")
    
    if uploaded_file2 is not None:
        with col2:
            st.header("Hình Ảnh 2")
            process_image(uploaded_file2, "Hình Ảnh 2")
    
    if uploaded_file1 is not None and uploaded_file2 is not None:
        st.header("So Sánh")
        st.write("Chênh lệch số lượng hạt: ", 
                 abs(st.session_state.get("grain_count_1", 0) - 
                     st.session_state.get("grain_count_2", 0)))

def process_image(uploaded_file, label):
    uploaded_file.seek(0)
    preprocessed, original = preprocess_image(uploaded_file)
    
    st.subheader("Hình Ảnh Gốc")
    st.image(original, channels="BGR")
    
    st.subheader("Hình Ảnh Đã Xử Lý")
    st.image(preprocessed, channels="GRAY")
    
    grain_count = count_grains(preprocessed)
    
    st.subheader("Số Lượng Hạt")
    st.write(f"Số lượng hạt phát hiện được: {grain_count}")
    
    if label == "Hình Ảnh 1":
        st.session_state["grain_count_1"] = grain_count
    else:
        st.session_state["grain_count_2"] = grain_count
    
    return grain_count

if __name__ == "__main__":
    main()