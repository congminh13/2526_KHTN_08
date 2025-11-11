import streamlit as st
import pandas as pd
from app import menu

from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

def show():
    st.title("Kết quả nghiên cứu")
    
    st.markdown("## Kết quả sàng lọc dấu ấn sinh học")
    
    st.markdown("""
    Sau quá trình phân tích và sàng lọc, chúng tôi xác định được **10 gen** có khả năng dự đoán di căn xương:
    """)
    
    genes = ["NFYC", "CEP57", "CD44", "ABCC5", "TGFB1I1", "PTPN11", "SMARCA2", "MICAL2", "SLC36A1", "ZXDA"]
    
    cols = st.columns(5)
    for i, gene in enumerate(genes):
        with cols[i % 5]:
            if gene in ["PTPN11", "MICAL2"]:
                st.info(f"**{i+1}. {gene}**")
            else:
                st.write(f"**{i+1}. {gene}**")
    
    st.warning("**Đặc biệt chú ý:** Hai gen **PTPN11** và **MICAL2** được xác định là các dấu ấn sinh học quan trọng nhất, có khả năng dự đoán cao và ổn định trên nhiều tập dữ liệu.")
    
    st.markdown("---")
    st.markdown("## So sánh hiệu suất các mô hình")
    
    st.markdown("Chúng tôi đã huấn luyện và so sánh 7 mô hình học máy khác nhau:")
    
    model_data = {
        "Mô hình": ["Logistic Regression", "SVM", "KNN", "XGBoost", "AdaBoost", "Random Forest", "Decision Tree"],
        "Các gen sử dụng": ["PTPN11, MICAL2", "PTPN11, MICAL2", "ABCC5, TGFB1I1, PTPN11, SLC36A1", "ABCC5, TGFB1I1, SMARCA2, SLC36A1", "ABCC5, TGFB1I1, PTPN11, MICAL2, SLC36A1", "PTPN11, MICAL2", "MICAL2, NFYC, CD44"],
        "AUC Huấn luyện": [0.68, 0.66, 0.728, 0.659, 0.685, 0.746, 0.735],
        "AUC Kiểm tra": ["−", "−", "−", "−", "−", "−", "−"],
        "AUC Độc lập": [0.774, 0.772, 0.758, 0.747, 0.723, 0.69, 0.686],
    }
    
    df = pd.DataFrame(model_data)
    st.dataframe(df, use_container_width=True)
    
    st.success("**Mô hình tối ưu: Logistic Regression** ✓\n\nMô hình **Logistic Regression** sử dụng 2 gen PTPN11 và MICAL2 đạt hiệu suất cao nhất trên tập dữ liệu độc lập (AUC = 0,774), đồng thời có ưu điểm là đơn giản, dễ giải thích và triển khai trong thực tế.")
    
    st.markdown("---")
    st.markdown("## Đánh giá chi tiết mô hình tối ưu")
    
    st.markdown("### Chỉ số hiệu suất")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("AUC", "0.774", "Khả năng phân biệt tốt")
    
    with col2:
        st.metric("Độ nhạy", "77.8%", "Phát hiện ca di căn")
    
    with col3:
        st.metric("Độ đặc hiệu", "65.2%", "Phát hiện ca không di căn")
    
    with col4:
        st.metric("Độ chính xác", "71.5%", "Dự đoán đúng tổng thể")
    
    st.markdown("### Cải thiện so với baseline")
    st.markdown("""
    - AUC tăng từ 0,69 (tập kiểm tra) lên 0,774 (tập độc lập)
    - Độ nhạy 77,8% đảm bảo phát hiện được phần lớn ca di căn
    - Mô hình ổn định và tổng quát tốt trên dữ liệu mới
    """)
    # Placeholders for figures from old HTML
    st.markdown("### Hình minh hoạ")
    c1, c2 = st.columns(2)
    with c1:
        st.info("Biểu đồ Venn: Giao điểm các phương pháp sàng lọc (placeholder)")
        st.info("Biểu đồ Violin: Phân bố điểm dự đoán (placeholder)")
    with c2:
        st.info("Đường cong ROC: AUC = 0,774 (placeholder)")
        st.info("Ma trận nhầm lẫn (placeholder)")

show()
menu()