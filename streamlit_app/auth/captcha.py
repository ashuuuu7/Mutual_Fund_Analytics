import random
import streamlit as st


def generate_captcha():

    if "captcha_num1" not in st.session_state:
        st.session_state.captcha_num1 = random.randint(1, 20)

    if "captcha_num2" not in st.session_state:
        st.session_state.captcha_num2 = random.randint(1, 20)


def refresh_captcha():

    st.session_state.captcha_num1 = random.randint(1, 20)
    st.session_state.captcha_num2 = random.randint(1, 20)