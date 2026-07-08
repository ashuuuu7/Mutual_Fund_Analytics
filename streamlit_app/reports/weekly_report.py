import sqlite3
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from auth.email_sender import send_weekly_report


DB_PATH = Path(__file__).resolve().parent.parent / "bluestock_mf.db"


def get_weekly_report_data():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT scheme_name, return_1yr_pct
        FROM fact_performance
        WHERE return_1yr_pct IS NOT NULL
        ORDER BY return_1yr_pct DESC
        LIMIT 5
    """)
    top_funds = cursor.fetchall()
    cursor.execute("""
        SELECT scheme_name, return_1yr_pct
        FROM fact_performance
        WHERE return_1yr_pct IS NOT NULL
        ORDER BY return_1yr_pct ASC
        LIMIT 5
    """)
    worst_funds = cursor.fetchall()

    cursor.execute("""
        SELECT
            ROUND(AVG(sharpe_ratio),2),
            ROUND(AVG(beta),2),
            ROUND(AVG(alpha),2)
        FROM fact_performance
    """)
    metrics = cursor.fetchone()

    conn.close()

    return {
        "top_funds": top_funds,
        "worst_funds": worst_funds,
        "metrics": metrics
    }

def generate_html_report():

    data = get_weekly_report_data()

    template_path = Path(__file__).resolve().parent.parent / "templates" / "weekly_report.html"

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    top_rows = ""

    for fund in data["top_funds"]:
        top_rows += f"""
        <tr>
            <td>{fund[0]}</td>
            <td>{fund[1]}%</td>
        </tr>
        """

    top_table = f"""
    <table>
        <tr>
            <th>Fund</th>
            <th>Annual Return</th>
        </tr>
        {top_rows}
    </table>
    """

    worst_rows = ""

    for fund in data["worst_funds"]:
        worst_rows += f"""
        <tr>
            <td>{fund[0]}</td>
            <td>{fund[1]}%</td>
        </tr>
        """

    worst_table = f"""
    <table>
        <tr>
            <th>Fund</th>
            <th>Annual Return</th>
        </tr>
        {worst_rows}
    </table>
    """

    html = html.replace("{{TOP_FUNDS}}", top_table)
    html = html.replace("{{WORST_FUNDS}}", worst_table)

    html = html.replace("{{SHARPE}}", str(data["metrics"][0]))
    html = html.replace("{{BETA}}", str(data["metrics"][1]))
    html = html.replace("{{ALPHA}}", str(data["metrics"][2]))

    return html

if __name__ == "__main__":

    report = generate_html_report()

    with open("weekly_report_output.html", "w", encoding="utf-8") as f:
        f.write(report)

    print("Weekly Report Generated Successfully")

    receiver_email = "YOUR_EMAIL@gmail.com"

    if send_weekly_report(receiver_email, report):
        print("Weekly Report Email Sent Successfully")
    else:
        print("Failed to Send Weekly Report")