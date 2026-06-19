import streamlit as st

st.set_page_config(page_title="技能")

st.title("技能")

st.subheader("程式與工具")
st.markdown("""
- Python（爬蟲 / 自動化 / FastAPI 後端開發）
- SQL Server（ETL）
- Power BI（KPI / Dashboard）
- SSAS / SSRS
""")

st.subheader("資料工程能力")
st.markdown("""
- ETL 流程設計
- API 設計與爬蟲整合 (FastAPI)
- Azure SQL / PostgreSQL
""")

st.subheader("專案能力")
st.markdown("""
- 即時新聞爬蟲與 LINE 推播 (NLP)
- FastAPI 後端分層架構與 JWT 認證
- 遊戲開發與團隊管理 (Unity)
""")