import streamlit as st
import numpy as np
import time


def move_ball(paddle_pos, ball_pos, ball_dir):
    """移动球"""
    # 更新球的位置
    ball_pos += ball_dir
    # 检查是否撞到了上下墙壁
    if ball_pos[1] < 0 or ball_pos[1] > 1:
        ball_dir[1] *= -1
    # 检查是否撞到了挡板
    if ball_pos[0] < 0 and abs(ball_pos[1] - paddle_pos) < 0.2:
        ball_dir[0] *= -1
    # 检查是否输了
    if ball_pos[0] < 0:
        return False, ball_pos, ball_dir
    return True, ball_pos, ball_dir


def play_game(difficulty):
    """游戏主循环"""
    st.write(f"难度：{difficulty}")
    paddle_pos = 0.5  # 挡板初始位置
    ball_pos = np.array([0.9, 0.5])  # 球的初始位置
    ball_speed = 0.02 * difficulty  # 球的速度（难度越高，速度越快）
    ball_dir = np.array([-1, 0.5]) * ball_speed  # 球的初始方向

    st_canvas = st.sidebar.empty()
    canvas_result = st_canvas.canvas(
        width=300, height=300, background_color="#fff", key="canvas"
    )

    running = True
    score = 0
    while running:
        # 绘制游戏画面
        canvas_result.clear()
        canvas_result.rect(
            int(paddle_pos * 300) - 5,
            250,
            int(paddle_pos * 300) + 5,
            255,
            fill_color="#000",
        )
        canvas_result.circle(
            int(ball_pos[0] * 300), int(ball_pos[1] * 300), 5, fill_color="#000"
        )

        # 读取鼠标事件
        mouse_events = st_canvas.get_drawing_inputs()
        for event in mouse_events:
            if event["type"] == "mousemove":
                paddle_pos = event["x"] / 300

        # 移动球并更新游戏状态
        running, ball_pos, ball_dir = move_ball(paddle_pos, ball_pos, ball_dir)
        if not running:
            st.write(f"游戏结束！得分：{score}")
            break
        score += 1
        time.sleep(0.01)

    st.write("再来一局？")
    restart = st.button("重新开始")
    if restart:
        play_game(difficulty)
        
           st.title("用鼠标和 AI 打乒乓")
        if __name__ == '__main__':
 
    difficulty = st.slider("选择难度", 1, 10, 5)
    play_game(difficulty)
