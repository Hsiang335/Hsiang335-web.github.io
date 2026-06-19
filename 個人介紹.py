import streamlit as st

# 🔹 基本設定
st.set_page_config(
    page_title="個人求職頁",
    layout="wide"
)

# 🔹 自訂CSS（簡約沈穩風）
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #ffffff;
}
h1, h2, h3 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# ======================
# 個人介紹
# ======================
st.title("個人介紹")

col1, col2 = st.columns([1, 2])

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "assets", "p1.jpg")

with col1:
    st.image(image_path, use_container_width=True)

with col2:
    st.subheader("勝翔")
    st.write("資料分析 / 資料工程")

st.markdown("---")

# ======================
# 自我簡介
# ======================
st.subheader("自我簡介")
st.write("""
您好，我是勝翔。出生於嘉義縣，目前與妻子定居台中，育有一子一女。  
在家庭與育兒過程中培養了耐心與責任感。

畢業於正修科技大學電機工程系，具備Unity3D、C#、單晶片8051、C語言、PLC基礎。  
目前於職訓局進修「Python人工智慧與數據分析班」。
""")

st.markdown("---")

# ======================
# 工作經歷
# ======================
st.subheader("工作經歷")
st.write("""
**凌發科技（Unity 組長 / 主任）**  
*2020/05 ~ 2025/07*  
- 主導 Unity3D 博弈遊戲包網平台開發，導入 Addressable Bundle 技術架構，負責元宇宙與直播系統開發。  

**網銀國際（資深工程師 / 組長）**  
*2012/04 ~ 2020/04*  
- 擔任《世界大亨》Client 端主程，負責雙平台發佈、框架維護與效能優化。  
""")

st.markdown("---")

# ======================
# 技術能力
# ======================
st.subheader("技術能力")
st.write("""
- Python（爬蟲 / 自動化 / FastAPI 後端開發）
- SQL Server（ETL）
- SSAS / SSRS
- Power BI
""")

st.markdown("[查看網頁版技術技能樹](https://chengshiang335-web.github.io/)")

st.markdown("---")

# ======================
# 專案與專題經驗
# ======================
st.subheader("近期開發專案 (做中學成果)")

st.markdown("""
### 📊 1. 大型數據資料分析（Power BI 專題）

**📌 專案內容：**
- 建立 Power BI 銷售分析儀表板  
- 資料模型設計（Star Schema）  
- KPI 指標分析（營收 / 成長率 / 客戶分析）  
- 大數據資料整合與視覺化呈現  

**🚀 技術應用：**
- Power BI（DAX / 資料建模 / 視覺化）
- SQL Server（資料整理 / ETL）
- Azure SQL Database

**📎 專案連結：**
- 📽️ [PPT 簡報](https://docs.google.com/presentation/d/1vKofcCD7jqhMZdQzVjEwo_z2RVMB3DxbIUQrxneBkX4/edit)  
- 📊 [Power BI Dashboard 報表](https://app.powerbi.com/view?r=eyJrIjoiNWM4NjQzNTEtMjEyYS00MjI2LThiMmUtMmVhNTM5NjhmZjI1IiwidCI6IjQ3N2JmZWFhLTUyOTEtNGY4My04YjE0LTAzMWMzMDljZDExNyJ9)
""")

st.markdown("---")

st.markdown("""
### 📡 2. 美國總統動態即時監控系統 (BI + AI 整合)

**📌 專案內容：**
- 每 5 分鐘抓取即時新聞並寫入 Azure SQL Database。
- 進行 NLP 情感分析（正負向判斷）並透過 LINE Notify 即時推播至群組與智慧手錶。

**🚀 技術應用：**
- Python 爬蟲 / NLP 情感分析
- Azure SQL Database / LINE 推播
""")

st.markdown("---")

st.subheader("⚡ 3. FastAPI 後端分層架構與驗證系統 (FastAPITest)")
st.write("""
**📌 專案內容：**
- 實作 **Router ➔ Service ➔ Repository ➔ Database** 後端分層架構，降低耦合度，便於維護。
- 使用 **JWT (JSON Web Token)** 與 **bcrypt** 實作安全的使用者註冊、登入與密碼雜湊驗證機制。
- 使用 **pytest** 撰寫單元測試，並運用相依性注入 (DI) 抽換為 **Fake Repository**，實現輕量獨立的測試環境。
- 整合 **SQLAlchemy ORM** 與 **PostgreSQL** 進行文件 CRUD 操作，並以 **Docker-Compose** 進行容器化部署。
""")
st.markdown("**🚀 技術應用：** `FastAPI` | `SQLAlchemy` | `JWT 驗證` | `PostgreSQL` | `Docker` | `pytest`")
st.markdown("""
**📎 專案連結：**
- 📽️ YouTube 實作演示：https://youtu.be/K3fE7Kp4ziY
- 💻 GitHub 程式碼：https://github.com/Hsiang335/FastAPITest.git
""")
st.video("https://youtu.be/K3fE7Kp4ziY")

st.markdown("---")

st.subheader("職涯理念")
st.write("""
重視實作與成果，持續優化系統與流程，  
希望在資料分析與工程領域創造價值。
""")