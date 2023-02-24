import streamlit as st
import pong

st.title("用鼠标和 AI 打乒乓")
difficulty = st.slider("选择难度", 1, 10, 5)
pong.play_game(difficulty)
