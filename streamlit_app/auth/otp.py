import random
import time
import streamlit as st


def generate_otp():

    otp = random.randint(100000, 999999)

    st.session_state.otp = str(otp)

    st.session_state.otp_created_time = time.time()

    return str(otp)


def verify_otp(user_otp):

    if "otp" not in st.session_state:
        return False, "OTP not generated."

    if time.time() - st.session_state.otp_created_time > 300:
        return False, "OTP expired."

    if user_otp != st.session_state.otp:
        return False, "Invalid OTP."

    return True, "OTP Verified"