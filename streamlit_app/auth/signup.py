import streamlit as st
from auth.security import hash_password
from utils.database import create_user
import time


def signup():

    st.title("📝 Create Account")

    if st.button("⬅ Back to Login"):
        st.session_state.show_signup = False
        st.rerun()

    with st.form("signup_form", clear_on_submit=False):

        username = st.text_input(
            "👤 Username",
            placeholder="Choose Username",
            autocomplete="username",
            key="signup_username"
        )

        mobile = st.text_input(
            "📱 Mobile Number",
            placeholder="Enter 10-digit Mobile Number",
            key="signup_mobile"
        )

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your Email",
            key="signup_email"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Create Strong Password",
            autocomplete="new-password",
            key="signup_password"
        )

        confirm_password = st.text_input(
            "🔒 Confirm Password",
            type="password",
            placeholder="Confirm Password",
            autocomplete="new-password",
            key="signup_confirm_password"
        )

        submit = st.form_submit_button(
            "Create Account",
            use_container_width=True
        )

    if submit:

        if username.strip() == "":
            st.error("Username is required.")
            return

        if email.strip() == "":
            st.error("Email is required.")
            return

        if password.strip() == "":
            st.error("Password is required.")
            return

        if confirm_password.strip() == "":
            st.error("Confirm Password is required.")
            return
        
        if mobile and (not mobile.isdigit() or len(mobile) != 10):
            st.error("Enter a valid 10-digit mobile number.")
            return

        if "@" not in email or "." not in email:
            st.error("Enter a valid email address.")
            return
        
        if password != confirm_password:
            st.error("Passwords do not match.")
            return
        
        if len(password) < 8:
            st.error("Password must be at least 8 characters long.")
            return
        
        hashed_password = hash_password(password)

        success = create_user(username, email, mobile, hashed_password)

        if success:
            st.success("Account created successfully! Please login.")
            time.sleep(1.5)
            st.session_state.show_signup = False
            st.rerun()
        else:
            st.error("Username, Email or Mobile already exists.")