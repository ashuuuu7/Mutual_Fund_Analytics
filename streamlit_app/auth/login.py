import streamlit as st
from auth.captcha import generate_captcha, refresh_captcha
from PIL import Image
from pathlib import Path
import time
import hashlib
from auth.signup import signup
from utils.database import get_user
from auth.security import hash_password


def login():

    left, center, right = st.columns([1, 1, 1])

    with center:
        logo_path = Path(__file__).parent.parent / "assets" / "app_logo.webp"
        logo = Image.open(logo_path)

        _, img_col, _ = st.columns([1, 2, 1])

        with img_col:
            st.image(logo,use_container_width=True)

        generate_captcha()

        st.markdown("""
        <h1 style="
        text-align:center;
        font-size:40px;
        font-weight:700;
        margin-bottom:4px;
        letter-spacing:0.5px;
        ">
        Bluestock Mutual Fund Analytics
        </h1>

        <p style="
        text-align:center;
        font-size:17px;
        color:#9CA3AF;
        margin-top:0;
        margin-bottom:12px;
        ">
        Secure Financial Analytics Platform
        </p>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown(
            "<div style='height:25px;'></div>",
            unsafe_allow_html=True
        )

        username_or_email = st.text_input(
            "👤 Username or Email",
            placeholder="Enter your Username or Email",
            key="login_username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your Password",
            autocomplete="current-password",
            key="login_password"
        )


        st.markdown("### 🔐 Security Verification")

        col1, col2 = st.columns([10, 1])

        with col1:
            st.info(
                f"Solve: {st.session_state.captcha_num1} + {st.session_state.captcha_num2}"
            )

        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("↻", key="refresh_captcha", help="Refresh CAPTCHA"):
                refresh_captcha()
                st.rerun()

        captcha = st.text_input(
            "Enter CAPTCHA",
            placeholder="Type your answer"
        )

        col1, col2 = st.columns(2)

        with col1:
            signup_btn = st.button(
                "📝 Create New Account",
                use_container_width=True,
                key="signup_btn"
            )

        with col2:
            login_btn = st.button(
                "🔐 Sign In",
                use_container_width=True,
                key="login_btn"
            )

        if st.button("🔑 Forgot Password?"):
            st.session_state.show_forgot_password = True
            st.rerun()

        if signup_btn:
            st.session_state.show_signup = True
            st.rerun()

        if login_btn:

            correct_captcha = (
            captcha.isdigit()
            and int(captcha)
            == st.session_state.captcha_num1 + st.session_state.captcha_num2
        )

            entered_password_hash = hash_password(password)
            user = get_user(username_or_email)

            if (user and user[4] == entered_password_hash and correct_captcha):
                st.session_state.logged_in = True 
                st.session_state.username = user[1]

                st.success("Authentication Successful. Redirecting to Dashboard...")

                time.sleep(1)

                st.rerun()

            else:

                refresh_captcha()

                st.error("Invalid Username/Email, Password or CAPTCHA.\nPlease verify your credentials and try again.")

        st.markdown("""
        <hr>

        <p style='text-align:center;
        color:gray;
        font-size:14px'>
        © 2026 Bluestock Mutual Fund Analytics
        <br>
        Developed by Ashutosh Giri
        </p>
        """, unsafe_allow_html=True)