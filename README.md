# /README.md

## 📌 專案簡介
模組化台股盤後寫入系統，支援每日三次自動執行，將資料寫入 Google Sheets `post_review`。

## 🧩 模組說明
- `post_market.py`: 主程式，抓資料、算指標、寫入 Sheet
- `utils.py`: 工具函式，包含 Sheet ID 查詢與資料處理
- `requirements.txt`: 套件清單
- `.github/workflows/post_market.yml`: GitHub Actions 排程設定

## 🕒 執行時間（台灣時間）
- 09:05
- 15:00
- 20:30

## 🔐 注意事項
- 請將 `service_account.json` 放在根目錄，並設定為私密
- Sheet 權限需開放給該 service account

## 🧪 測試方式
```bash
python post_market.py
