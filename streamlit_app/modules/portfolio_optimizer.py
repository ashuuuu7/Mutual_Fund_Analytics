import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "bluestock_mf.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def get_top_funds():

    conn = get_connection()

    query = """
        SELECT
            scheme_name,
            return_1yr_pct,
            std_dev_ann_pct
        FROM fact_performance
        ORDER BY return_1yr_pct DESC
        LIMIT 5
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

def show_portfolio_optimizer():

    st.title("📊 Portfolio Optimizer")

    st.write("Markowitz Efficient Frontier (Top 5 Mutual Funds)")

    st.markdown("---")

    funds = get_top_funds()

    st.subheader("Top 5 Funds Used")

    display_df = funds.rename(columns={
        "scheme_name": "Fund Name",
        "return_1yr_pct": "1-Year Return (%)",
        "std_dev_ann_pct": "Annual Risk (%)"
    })

    display_df["1-Year Return (%)"] = display_df["1-Year Return (%)"].map(lambda x: f"{x:.2f}%")
    display_df["Annual Risk (%)"] = display_df["Annual Risk (%)"].map(lambda x: f"{x:.2f}%")

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    returns = funds["return_1yr_pct"].values / 100
    risk = funds["std_dev_ann_pct"].values / 100

    num_portfolios = 5000

    results = []

    for _ in range(num_portfolios):

        weights = np.random.random(len(funds))
        weights /= np.sum(weights)

        portfolio_return = np.sum(weights * returns)

        portfolio_risk = np.sqrt(np.sum((weights * risk) ** 2))

        sharpe = portfolio_return / portfolio_risk

        results.append([
            portfolio_return,
            portfolio_risk,
            sharpe,
            weights
        ])

    portfolio_df = pd.DataFrame(
        results,
        columns=[
            "Return",
            "Risk",
            "Sharpe",
            "Weights"
        ]
    )

    best = portfolio_df.loc[portfolio_df["Sharpe"].idxmax()]

    fig = px.scatter(
    portfolio_df,
    x="Risk",
    y="Return",
    color="Sharpe",
    title="Markowitz Efficient Frontier",
    color_continuous_scale="Viridis"
)

    fig.add_scatter(
        x=[best["Risk"]],
        y=[best["Return"]],
        mode="markers",
        marker=dict(
            size=18,
            color="red",
            symbol="star"
        ),
        name="Optimal Portfolio"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        key="efficient_frontier"
    )

    st.markdown("---")
    st.subheader("⭐ Optimal Portfolio Allocation")

    weights = best["Weights"]

    allocation = pd.DataFrame({
        "Fund": funds["scheme_name"],
        "Allocation (%)": (weights * 100).round(2)
    })

    allocation = allocation.sort_values(
        by="Allocation (%)",
        ascending=False
    )

    st.dataframe(
        allocation,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")
    st.subheader("🥧 Portfolio Allocation Chart")

    fig2 = px.pie(
        allocation,
        names="Fund",
        values="Allocation (%)",
        hole=0.45,
        title="Recommended Investment Distribution"
    )

    st.plotly_chart(
        fig2,
        width="stretch",
        key="portfolio_pie"
    )

    st.markdown("---")

    st.success(
        f"""
    ### 🎯 Recommendation

    ✅ Expected Return : **{best['Return']*100:.2f}%**

    ✅ Portfolio Risk : **{best['Risk']*100:.2f}%**

    ✅ Sharpe Ratio : **{best['Sharpe']:.2f}**

    This portfolio provides the highest risk-adjusted return among all simulated portfolios.
    """
    )

    st.info("""
    💡 **Investment Insight**

    This portfolio provides the highest risk-adjusted return (Maximum Sharpe Ratio)
    among all simulated portfolios. It offers an optimal balance between expected
    return and risk based on the Markowitz Efficient Frontier.
    """)