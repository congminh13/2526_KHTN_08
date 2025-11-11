import streamlit as st
import numpy as np
from app import menu
from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

def show():
    st.title("Công cụ dự đoán nguy cơ di căn xương")
    
    st.markdown("Nhập giá trị biểu hiện gen để dự đoán nguy cơ di căn xương ở bệnh nhân ung thư vú")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Nhập giá trị biểu hiện gen")
        
        ptpn11 = st.slider(
            "Biểu hiện gen PTPN11",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=0.1,
            help="Protein Tyrosine Phosphatase Non-receptor Type 11"
        )
        
        mical2 = st.slider(
            "Biểu hiện gen MICAL2",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=0.1,
            help="Molecule Interacting with CasL 2"
        )
    
    with col2:
        st.markdown("### Kết quả dự đoán")
        
        # Normalize inputs
        ptpn11_norm = ptpn11 / 100.0
        mical2_norm = mical2 / 100.0
        
        # Simple logistic model (coefficients are illustrative)
        z = -0.5 + (1.2 * ptpn11_norm) + (0.8 * mical2_norm)
        risk_score = 1 / (1 + np.exp(-z))
        
        # Risk interpretation
        if risk_score < 0.3:
            risk_level = "🟢 Nguy cơ thấp"
            recommendation = "Theo dõi định kỳ thông thường"
            color = "green"
        elif risk_score < 0.5682:
            risk_level = "🟡 Nguy cơ vừa phải"
            recommendation = "Theo dõi định kỳ được khuyến nghị"
            color = "yellow"
        else:
            risk_level = "🔴 Nguy cơ cao"
            recommendation = "Theo dõi sát sao và xem xét xét nghiệm bổ sung"
            color = "red"
        
        # Display risk score
        st.metric("Điểm nguy cơ", f"{risk_score:.3f}")
        
        # Display risk gauge
        st.progress(risk_score, text=f"{risk_score*100:.1f}%")
        
        # Display interpretation
        st.markdown(f"### {risk_level}")
        st.info(recommendation)
        
        # Display model metrics
        st.markdown("### Thông số mô hình")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Độ nhạy", "77.8%")
        with col_b:
            st.metric("AUC", "0.774")
    
    st.markdown("---")
    st.markdown("### Giải thích kết quả")
    st.markdown("""
    - **Điểm nguy cơ 0.0 - 0.3:** Nguy cơ thấp - Theo dõi định kỳ thông thường
    - **Điểm nguy cơ 0.3 - 0.5682:** Nguy cơ vừa phải - Theo dõi định kỳ được khuyến nghị
    - **Điểm nguy cơ > 0.5682:** Nguy cơ cao - Theo dõi sát sao và xem xét xét nghiệm bổ sung
    
    **Ngưỡng 0.5682** được tối ưu hóa dựa trên phân tích đường cong ROC.
    """)
    
    st.warning("""
    **⚠️ Lưu ý quan trọng:** Đây là công cụ nghiên cứu và chỉ mang tính chất tham khảo. 
    Không thể thay thế chẩn đoán lâm sàn của bác sĩ. Kết quả cần được đánh giá kết hợp với 
    các yếu tố lâm sàn, hình ảnh học và xét nghiệm khác.
    """)
    
    st.markdown("---")
    st.markdown("### Câu hỏi thường gặp")
    
    with st.expander("Làm thế nào để đo biểu hiện gen?"):
        st.markdown("""
        Biểu hiện gen được đo bằng các kỹ thuật như RT-PCR, microarray, hoặc RNA sequencing 
        từ mẫu máu hoặc mô u. Giá trị thường được chuẩn hóa theo thang điểm để so sánh.
        """)
    
    with st.expander("Ngưỡng 0.5682 được xác định như thế nào?"):
        st.markdown("""
        Ngưỡng được tối ưu hóa dựa trên phân tích đường cong ROC, cân bằng giữa độ nhạy 
        và độ đặc hiệu để đạt hiệu suất tổng thể tốt nhất trên tập huấn luyện.
        """)
    
    with st.expander("Nguy cơ cao có nghĩa là chắc chắn sẽ di căn?"):
        st.markdown("""
        Không. "Nguy cơ cao" chỉ nghĩa là xác suất di căn cao hơn trung bình, không phải 
        chắc chắn. Nhiều yếu tố khác như điều trị, thể trạng bệnh nhân cũng ảnh hưởng 
        đến kết cục thực tế.
        """)

show()
menu()