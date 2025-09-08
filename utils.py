# /utils.py
import gspread
import pandas as pd

def get_sheet_id_by_name(name):
    # 模擬查表邏輯，可改為讀 config.json 或 index sheet
    mapping = {
        "post_review": "1bV0v-53zVU1XqujVmc9AdKlvh1_q4Pqi__MFX1opXuI",
        "CC_0050_list": "your_other_sheet_id"
    }
    return mapping.get(name)

def fetch_tw_stock_data():
    # 模擬資料抓取，可改為 API 或爬蟲
    data = {
        "股票代號": ["2330", "2317"],
        "收盤價": [600, 120],
        "漲跌幅": [1.2, -0.5]
    }
    return pd.DataFrame(data)

def calculate_indicators(df):
    df["強度指標"] = df["漲跌幅"].apply(lambda x: "強" if x > 0.5 else "弱")
    return df
