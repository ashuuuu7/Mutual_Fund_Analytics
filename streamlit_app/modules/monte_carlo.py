import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "bluestock_mf.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_all_funds():
    conn = get_connection()

    query = """
        SELECT scheme_name
        FROM fact_performance
        ORDER BY scheme_name
    """

    funds = pd.read_sql(query, conn)

    conn.close()

    return funds["scheme_name"].tolist()

def get_fund_metrics(scheme_name):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            return_1yr_pct,
            std_dev_ann_pct
        FROM fact_performance
        WHERE scheme_name = ?
    """, (scheme_name,))

    row = cursor.fetchone()

    conn.close()

    return row

def show_monte_carlo():
    st.title("📈 Monte Carlo Simulation")
    st.write("5-Year NAV Projection using Monte Carlo Simulation")

    st.markdown("---")

    funds = get_all_funds()

    selected_fund = st.selectbox(
        "Select Mutual Fund",
        funds
    )

    metrics = get_fund_metrics(selected_fund)

    if metrics is None:
        st.error("Fund data not found.")
        return

    expected_return = metrics[0] / 100
    volatility = metrics[1] / 100
    st.markdown("---")

    years = st.slider(
        "Projection Years",
        1,
        5,
        5
    )

    simulations = st.slider(
        "Number of Simulations",
        100,
        1000,
        500,
        step=100
    )

    initial_nav = 100

    days = years * 252

    simulated = np.zeros((days, simulations))

    for i in range(simulations):

        prices = [initial_nav]

        for _ in range(days - 1):

            daily_return = np.random.normal(
                expected_return / 252,
                volatility / np.sqrt(252)
            )

            prices.append(
                prices[-1] * (1 + daily_return)
            )

        simulated[:, i] = prices
    fig = go.Figure()

    for j in range(min(simulations, 50)):
        fig.add_trace(
            go.Scatter(
                y=simulated[:, j],
                mode="lines",
                line=dict(width=1),
                opacity=0.25,
                showlegend=False
            )
        )

    fig.update_layout(
        title="5-Year Monte Carlo NAV Projection",
        xaxis_title="Trading Days",
        yaxis_title="Projected NAV",
        height=650,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    final_values = simulated[-1]
    median_nav = np.median(final_values)
    best_case = np.percentile(final_values, 95)
    worst_case = np.percentile(final_values, 5)
    probability_profit = np.mean(final_values > initial_nav) * 100

    st.markdown("---")
    st.subheader("📊 Simulation Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📈 Median Final NAV", f"{median_nav:.2f}")
        st.metric("🚀 Best Case (95%)", f"{best_case:.2f}")

    with col2:
        st.metric("📉 Worst Case (5%)", f"{worst_case:.2f}")
        st.metric("🎯 Probability of Profit", f"{probability_profit:.2f}%")