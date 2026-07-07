import streamlit as st

def show_about():

    st.title("ℹ️ About Bluestock Mutual Fund Analytics")

    st.markdown("---")

    st.markdown("""
## 📊 Project Overview

Bluestock Mutual Fund Analytics is a professional Streamlit application developed to analyze and compare mutual funds.

The application helps investors explore mutual funds, compare different schemes, calculate SIP returns, and visualize fund performance.

---
""")

    st.subheader("🚀 Features")

    st.markdown("""
- 📈 Dashboard Analytics
- 🔍 Live Fund Explorer
- ⚖️ Compare Mutual Funds
- 💰 SIP Calculator
- 📊 Performance Charts
- 📋 Fund Details
- 🔐 Secure Login System
""")

    st.markdown("---")

    st.subheader("🛠 Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
        st.write("• Python")
        st.write("• Streamlit")
        st.write("• Pandas")
        st.write("• NumPy")

    with col2:
        st.write("• SQLite")
        st.write("• Plotly")
        st.write("• Matplotlib")
        st.write("• SHA-256 Authentication")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.success("Ashutosh Giri")

    st.write("AI & Data Science Student")

    st.write("Bluestock Mutual Fund Analytics Capstone Project")

    st.markdown("---")

    st.caption("Version 1.0 | © 2026")