import tempfile
import cv2
import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import sys

st.title('Lane Detection')
st.markdown('Upload a video and detect lane')

st.header('Input Video')

f = st.file_uploader("Upload file")

tfile = tempfile.NamedTemporaryFile(delete=False) 
tfile.write(f.read())

vf = cv2.VideoCapture(tfile.name)

stframe = st.empty()

while vf.isOpened():
    ret, frame = vf.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    stframe.image(gray)

    
# subprocess.run([f"{sys.executable}", "main.py"])

# video_file = open('output.mp4', 'rb')
# video_bytes = video_file.read()

st.video(video_bytes)
