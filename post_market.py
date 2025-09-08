# /post_market.py
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from utils import get_sheet_id_by_name, fetch_tw_stock_data, calculate_indicators

def main():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(creds)

    sheet_id = get_sheet_id_by_name("post_review")
    sheet = client.open_by_key(sheet_id).sheet1

    df = fetch_tw_stock_data()
    df = calculate_indicators(df)

    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

if __name__ == "__main__":
    main()
