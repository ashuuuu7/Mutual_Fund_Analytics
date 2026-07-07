import streamlit as st
import pandas as pd
from pathlib import Path
from modules.about import show_about
from auth.login import login
from dashboard.dashboard import show_dashboard
from utils.database import (
    create_users_table,
    get_filtered_funds,
    get_all_funds,
    get_fund_details,
    get_all_fund_houses,
    get_all_categories,
    get_all_risk_levels
)
import plotly.express as px
from auth.signup import signup
from auth.logout import logout

create_users_table()

st.set_page_config(
    page_title="Bluestock Mutual Fund Analytics",
    page_icon="📈",
    layout="wide"
)

css_path = Path(__file__).parent / "assets" / "style.css"

with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if "show_forgot_password" not in st.session_state:
    st.session_state.show_forgot_password = False

if not st.session_state.logged_in:

    if st.session_state.show_signup:
        signup()

    elif st.session_state.show_forgot_password:
        from auth.forgot_password import forgot_password
        forgot_password()

    else:
        login()

    st.stop()

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "🔍 Fund Explorer",
        "⚖️ Compare Funds",
        "💰 SIP Calculator",
        "ℹ️ About"
    ]
)


fund_house = st.sidebar.selectbox(
    "Fund House",
    ["All"] + get_all_fund_houses()
)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + get_all_categories()
)

risk = st.sidebar.selectbox(
    "Risk Level",
    ["All"] + get_all_risk_levels()
)

st.sidebar.markdown("---")

st.sidebar.subheader("🎯 Filters")

st.sidebar.markdown("---")

st.sidebar.write(f"👤 Logged in as")
st.sidebar.success(st.session_state.get("username", "User"))

if st.sidebar.button("Logout", width="stretch"):
    logout()


if page == "🏠 Dashboard":
    show_dashboard()

elif page == "🔍 Fund Explorer":

    st.title("🔍 Live Fund Explorer")

    funds = get_filtered_funds(
    fund_house=fund_house,
    category=category,
    risk=risk
)
    
    if not funds:
        st.warning("⚠️ No funds found for the selected filters.")
        st.stop()

    search = st.text_input(
        "🔍 Search Fund",
        placeholder="Search by fund name..."
    )

    if search:
        filtered_funds = [
            fund for fund in funds
            if search.lower() in fund.lower()
        ]
    else:
        filtered_funds = funds

    if len(filtered_funds) == 0:
        st.warning("No matching mutual fund found.")

    else:

        selected_fund = st.selectbox(
            "Matching Funds",
            filtered_funds
        )

        st.markdown("---")

        st.subheader("📄 Fund Details")

        st.info(f"Selected Fund: {selected_fund}")

        details = get_fund_details(selected_fund)

        if details:

            st.markdown("### 📊 Fund Overview")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🏢 Fund House", details["fund_house"])

            with col2:
                st.metric("📂 Category", details["category"])

            with col3:
                st.metric("⚠️ Risk", details["risk"])

            col4, col5, col6 = st.columns(3)

            with col4:
                st.metric("💰 AUM", f"₹ {details['aum']:,.2f} Cr")

            with col5:
                st.metric("📈 1Y Return", f"{details['return_1yr']} %")

            with col6:
                st.metric("💸 Expense Ratio", f"{details['expense']} %")

            col7, col8 = st.columns(2)

            with col7:
                st.metric("📊 3Y Return", f"{details['return_3yr']} %")

            with col8:
                st.metric("📈 5Y Return", f"{details['return_5yr']} %")

            st.markdown("---")

            st.subheader("📋 Scheme Information")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Scheme Name**")
                st.info(details["scheme_name"])

            with col2:
                st.write("**Plan Type**")
                st.info(details["plan"])
        
        else:
            st.error("Fund details not found.")

elif page == "⚖️ Compare Funds":

    st.title("⚖️ Compare Mutual Funds")

    col1, col2 = st.columns(2)
    funds = get_all_funds()

    with col1:
        fund1 = st.selectbox(
            "Select Fund 1", funds,
            key="fund1"
        )

    with col2:
        fund2 = st.selectbox(
            "Select Fund 2", funds,
            key="fund2"
        )

    st.markdown("---")

    st.subheader("📊 Comparison Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"📌 Fund 1\n\n{fund1}")

    with col2:
        st.info(f"📌 Fund 2\n\n{fund2}")

    details1 = get_fund_details(fund1)
    details2 = get_fund_details(fund2)

    # st.write(details1)
    # st.write(details2)
    if details1 and details2:

        st.markdown("## 📊 Fund Comparison")

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("📌 Fund 1")

            st.metric("🏢 Fund House", details1["fund_house"])
            st.metric("📂 Category", details1["category"])
            st.metric("⚠️ Risk", details1["risk"])
            st.metric("💰 AUM", f"₹ {details1['aum']:,.2f} Cr")
            st.metric("📈 1Y Return", f"{details1['return_1yr']} %")
            st.metric("💸 Expense Ratio", f"{details1['expense']} %")

        with c2:

            st.subheader("📌 Fund 2")

            st.metric("🏢 Fund House", details2["fund_house"])
            st.metric("📂 Category", details2["category"])
            st.metric("⚠️ Risk", details2["risk"])
            st.metric("💰 AUM", f"₹ {details2['aum']:,.2f} Cr")
            st.metric("📈 1Y Return", f"{details2['return_1yr']} %")
            st.metric("💸 Expense Ratio", f"{details2['expense']} %")

        st.markdown("---")

        st.subheader("📋 Detailed Comparison")

        comparison_data = {
            "Feature": [
                "Fund House",
                "Category",
                "Risk",
                "AUM (Cr)",
                "1Y Return (%)",
                "3Y Return (%)",
                "5Y Return (%)",
                "Expense Ratio (%)",
                "Plan"
            ],
            fund1: [
                details1["fund_house"],
                details1["category"],
                details1["risk"],
                details1["aum"],
                details1["return_1yr"],
                details1["return_3yr"],
                details1["return_5yr"],
                details1["expense"],
                details1["plan"]
            ],
            fund2: [
                details2["fund_house"],
                details2["category"],
                details2["risk"],
                details2["aum"],
                details2["return_1yr"],
                details2["return_3yr"],
                details2["return_5yr"],
                details2["expense"],
                details2["plan"]
            ]
        }

        comparison_df = pd.DataFrame(comparison_data)

        st.dataframe(
            comparison_df,
            use_container_width=True,
            hide_index=True
        )
        chart_df = pd.DataFrame({
            "Metric": [
                "1Y Return",
                "3Y Return",
                "5Y Return"
            ],

            fund1: [
                details1["return_1yr"],
                details1["return_3yr"],
                details1["return_5yr"]
            ],

            fund2: [
                details2["return_1yr"],
                details2["return_3yr"],
                details2["return_5yr"]
            ]
        })

        chart_df = chart_df.melt(
            id_vars="Metric",
            var_name="Fund",
            value_name="Return"
        )

        fig = px.bar(
            chart_df,
            x="Metric",
            y="Return",
            color="Fund",
            barmode="group",
            text="Return",
            title="Mutual Fund Performance Comparison"
        )

        fig.update_layout(
            height=500,
            xaxis_title="",
            yaxis_title="Return (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("---")
        st.subheader("🏆 Overall Recommendation")

        score1 = 0
        score2 = 0

        # Higher return is better
        if details1["return_1yr"] > details2["return_1yr"]:
            score1 += 1
        else:
            score2 += 1

        if details1["return_3yr"] > details2["return_3yr"]:
            score1 += 1
        else:
            score2 += 1

        if details1["return_5yr"] > details2["return_5yr"]:
            score1 += 1
        else:
            score2 += 1

        # Lower expense ratio is better
        if details1["expense"] < details2["expense"]:
            score1 += 1
        else:
            score2 += 1

        # Higher AUM is better
        if details1["aum"] > details2["aum"]:
            score1 += 1
        else:
            score2 += 1

        if score1 > score2:
            st.success(f"🏆 Recommended Fund: {fund1}")
        elif score2 > score1:
            st.success(f"🏆 Recommended Fund: {fund2}")
        else:
            st.info("🤝 Both funds perform similarly.")

        st.markdown("---")
        st.subheader("🏆 Winner Summary")

        winner_return = fund1 if details1["return_1yr"] > details2["return_1yr"] else fund2
        winner_expense = fund1 if details1["expense"] < details2["expense"] else fund2
        winner_aum = fund1 if details1["aum"] > details2["aum"] else fund2

        col1, col2, col3 = st.columns(3)

        with col1:
            st.success(f"📈 Better Return\n\n{winner_return}")

        with col2:
            st.success(f"💸 Lower Expense\n\n{winner_expense}")

        with col3:
            st.success(f"💰 Higher AUM\n\n{winner_aum}")

elif page == "💰 SIP Calculator":

    st.title("💰 SIP Calculator")

    monthly = st.number_input(
        "Monthly SIP (₹)",
        min_value=500,
        value=5000,
        step=500
    )

    years = st.slider(
        "Investment Period (Years)",
        1,
        40,
        10
    )

    rate = st.slider(
        "Expected Annual Return (%)",
        1.0,
        25.0,
        12.0
    )

    r = rate / 12 / 100
    n = years * 12

    future_value = monthly * (((1 + r) ** n - 1) / r) * (1 + r)

    invested = monthly * n

    profit = future_value - invested

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💵 Total Investment", f"₹ {invested:,.0f}")

    with col2:
        st.metric("📈 Estimated Value", f"₹ {future_value:,.0f}")

    with col3:
        st.metric("💰 Wealth Gained", f"₹ {profit:,.0f}")

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("1Y Return", "18.4%")
        st.metric("Risk", "Moderate")
        st.metric("Expense Ratio", "0.82%")

    with c2:
        st.metric("1Y Return", "17.8%")
        st.metric("Risk", "Moderate")
        st.metric("Expense Ratio", "0.91%")

elif page == "ℹ️ About":
    show_about()