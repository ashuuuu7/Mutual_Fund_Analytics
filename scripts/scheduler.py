import schedule
import time
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
SCRIPT = PROJECT_DIR / "live_nav_fetch.py"

def run_etl():

    print("=" * 50)
    print("Running Daily NAV ETL...")
    print("=" * 50)

    subprocess.run(
        ["python", str(SCRIPT)]
    )

    print("ETL Completed Successfully.")

schedule.every().monday.at("20:00").do(run_etl)
schedule.every().tuesday.at("20:00").do(run_etl)
schedule.every().wednesday.at("20:00").do(run_etl)
schedule.every().thursday.at("20:00").do(run_etl)
schedule.every().friday.at("20:00").do(run_etl)

print("ETL Scheduler Started...")
print("Waiting for 8:00 PM (Monday-Friday)...")

while True:
    schedule.run_pending()
    time.sleep(30)