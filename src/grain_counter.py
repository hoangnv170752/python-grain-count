import cv2
import numpy as np

def count_grains(preprocessed_image):
    contours, _ = cv2.findContours(
        preprocessed_image, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE
    )
    
    min_area = 10
    max_area = 1000
    
    filtered_contours = [
        cnt for cnt in contours 
        if min_area < cv2.contourArea(cnt) < max_area
    ]
    
    return len(filtered_contours)
