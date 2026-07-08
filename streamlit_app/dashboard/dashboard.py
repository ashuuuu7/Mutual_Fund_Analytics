import streamlit as st
from utils.database import get_connection, get_dashboard_kpis
from reports.weekly_report import generate_html_report
from auth.email_sender import send_weekly_report
from datetime import datetime
import pandas as pd
import numpy as np


def show_dashboard():

    conn = get_connection()
    cursor = conn.cursor()

    total_schemes, total_aum, avg_return, risk = get_dashboard_kpis()

    st.title("📈 Bluestock Mutual Fund Analytics")

    current_date = datetime.now().strftime("%d %B %Y")

    st.markdown(f"""
    <div style="
    padding:18px;
    border-radius:12px;
    background:#1E293B;
    margin-bottom:20px;
    ">
    <h2 style="margin:0;color:white;">
    👋 Welcome back!
    </h2>

    <p style="margin:0;color:#CBD5E1;">
    Bluestock Mutual Fund Analytics Dashboard
    </p>

    <p style="margin-top:8px;color:#94A3B8;">
    📅 {current_date}
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📊 Total Schemes",
            value=f"{total_schemes:,}"
        )

    with col2:
        st.metric(
            label="💰 Total AUM",
            value=f"₹ {total_aum:,.2f} Cr"
        )

    with col3:
        st.metric(
            label="📈 Avg 1Y Return",
            value=f"{avg_return:.2f}%"
        )

    with col4:
        st.metric(
            label="⚠️ Most Common Risk",
            value=risk
        )

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.subheader("📈 NAV Trend")

        cursor.execute("""
            SELECT
                date,
                AVG(nav)
            FROM fact_nav
            GROUP BY date
            ORDER BY date
        """)

        chart_df = pd.DataFrame(
            cursor.fetchall(),
            columns=["Date", "NAV"]
        )

        chart_df["Date"] = pd.to_datetime(chart_df["Date"])

        st.line_chart(
            chart_df.set_index("Date")
        )

    with right:

        st.subheader("🏆 Top Performing Funds")

        cursor = conn.cursor()

        cursor.execute("""
            SELECT scheme_name, return_1yr_pct
            FROM fact_performance
            ORDER BY return_1yr_pct DESC
            LIMIT 5
        """)

        top_funds = cursor.fetchall()

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        for medal, fund in zip(medals, top_funds):
            st.write(f"{medal} {fund[0]} ({fund[1]}%)")

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader("📊 Category Distribution")

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                category,
                COUNT(*) as total_funds
            FROM fact_performance
            GROUP BY category
            ORDER BY total_funds DESC
        """)

        category_df = pd.DataFrame(
            cursor.fetchall(),
            columns=["Category", "Funds"]
        )

        st.bar_chart(category_df.set_index("Category"))


    with right:

        st.subheader("⚠️ Risk Distribution")

        cursor.execute("""
            SELECT
                risk_grade,
                COUNT(*)
            FROM fact_performance
            GROUP BY risk_grade
            ORDER BY COUNT(*) DESC
        """)

        risk_df = pd.DataFrame(
            cursor.fetchall(),
            columns=["Risk Level", "Funds"]
        )

        st.bar_chart(risk_df.set_index("Risk Level"))


    st.markdown("---")

    st.subheader("🏆 Top Performing Mutual Funds")

    cursor.execute("""
        SELECT
            scheme_name,
            category,
            return_1yr_pct,
            risk_grade
        FROM fact_performance
        ORDER BY return_1yr_pct DESC
        LIMIT 10
    """)

    fund_df = pd.DataFrame(
        cursor.fetchall(),
        columns=[
            "Fund Name",
            "Category",
            "1Y Return (%)",
            "Risk"
        ]
    )

    st.dataframe(
        fund_df,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    st.subheader("📧 Weekly Report")

    receiver_email = st.text_input(
        "Enter email address",
        value="",
        placeholder="example@gmail.com"
    )

    if st.button("📨 Send Weekly Report"):

        if receiver_email.strip() == "":
            st.warning("Please enter an email address.")

        else:
            report = generate_html_report()

            if send_weekly_report(receiver_email, report):
                st.success("✅ Weekly report sent successfully!")

            else:
                st.error("❌ Failed to send weekly report.")

    conn.close()