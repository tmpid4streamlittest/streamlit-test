#!/usr/bin python3
# -*- coding: utf-8 -*-

import streamlit as st
import cv2
import time
from PIL import Image

st.markdown("# Camera Application")

device = user_input = st.text_input("input your video/camera device", "0")
if device.isnumeric():
    # e.g. "0" -> 0
    device = int(device)

cap = cv2.VideoCapture(device)

image_loc = st.empty()
while cap.isOpened:
    ret, img = cap.read()
    time.sleep(0.01)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image_loc.image(img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

# Reference
"""
# Web カメラで得た画像を Streamlit 上で表示する
# https://qiita.com/SatoshiTerasaki/items/f1724d68deecdc14103f
"""

# memo
"""
# 
"""
