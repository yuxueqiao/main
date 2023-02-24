import streamlit as st
from PIL import Image

def move_image(start_pos, end_pos, image):
    """将图像从起始位置移动到目标位置"""
    st_canvas = st.sidebar.empty()
    canvas_result = st_canvas.canvas(
        width=300, height=300, background_color="#fff", key="canvas"
    )

    step_size = 0.05
    curr_pos = start_pos
    while curr_pos != end_pos:
        # 清空画布
        canvas_result.clear()

        # 绘制图像
        canvas_result.image(image, curr_pos, curr_pos + 0.2)

        # 计算下一步位置
        step_dir = (end_pos - start_pos) / abs(end_pos - start_pos)
        curr_pos += step_dir * step_size

        # 等待一段时间
        st_canvas.sleep(200)

    # 显示移动完成的图像
    canvas_result.image(image, end_pos, end_pos + 0.2)

# 加载要移动的图像
image = Image.open("image.png")

# 定义起始位置和目标位置
start_pos = 0.3
end_pos = 0.7

# 移动图像
move_image(start_pos, end_pos,  "http://cw.hubwiz.com/images/cw-cta-1.png")
