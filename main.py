import streamlit as st
from PIL import Image
import time

# 加载网络图片
image_url = "http://cw.hubwiz.com/images/cw-cta-1.png"
image = Image.open(image_url)
width, height = image.size
scale = 0.3  # 调整图片大小
image = image.resize((int(scale * width), int(scale * height)))

# 设置初始位置和移动速度
x_pos = 0
speed = 5

while True:
    # 创建画布并绘制图片
    canvas = st.empty()
    canvas.image(image, use_column_width=True, clamp=True)

    # 移动图片
    x_pos += speed
    if x_pos > 1:
        x_pos = -scale
    time.sleep(0.2)
    

