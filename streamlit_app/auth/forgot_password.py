import streamlit as st
from utils.database import (
    get_user_by_email,
)
from auth.otp import generate_otp, verify_otp
from auth.email_sender import send_email_otp
from utils.database import (
    get_user_by_email,
    update_password
)
from auth.security import hash_password

def forgot_password():

    st.title("🔑 Forgot Password")

    st.markdown(
        "Enter your registered email address to reset your password."
    )

    email = st.text_input(
        "📧 Registered Email",
        placeholder="Enter your registered email",
        key="forgot_email"
    )

    otp_method = "📧 Email OTP"

    send_otp = st.button(
        "📨 Send OTP",
        use_container_width=True
    )

    if send_otp:

        if otp_method == "📧 Email OTP":

            user = get_user_by_email(email)

            if not user:
                st.error("❌ Email not registered.")
                return

            st.success("✅ Email verified.")
            
            otp = generate_otp()

            try:
                result = send_email_otp(email, otp)
                print("Result =", result)

                if result:
                    st.success("✅ OTP sent to your registered email.")
                else:
                    st.error("❌ Failed to send OTP.")

            except Exception as e:
                print("Forgot Password Error:", e)
                st.error(str(e))

    if "otp" in st.session_state:

        st.divider()

        st.subheader("🔐 Verify OTP")

        entered_otp = st.text_input(
            "Enter 6-digit OTP",
            max_chars=6,
            key="entered_otp"
        )

        if st.button("✅ Verify OTP", use_container_width=True):

            valid, message = verify_otp(entered_otp)

            if valid:
                st.session_state.otp_verified = True
                st.success("✅ OTP Verified Successfully!")
            else:
                st.error(message)

        if st.session_state.get("otp_verified", False):

            new_password = st.text_input(
                "🔒 New Password",
                type="password"
            )

            confirm_password = st.text_input(
                "🔒 Confirm Password",
                type="password"
            )

            if st.button("Reset Password"):

                if new_password != confirm_password:
                    st.error("Passwords do not match.")
                    return

                hashed_password = hash_password(new_password)

                update_password(email, hashed_password)

                st.success("✅ Password Reset Successfully!")

                st.session_state.show_forgot_password = False
                st.rerun()

            if st.button("⬅ Back to Login"):
                st.session_state.show_forgot_password = False
                st.rerun()