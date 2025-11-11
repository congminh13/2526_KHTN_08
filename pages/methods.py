import streamlit as st
from app import menu

from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )
  
def show():
    st.title("Dữ liệu và Phương pháp nghiên cứu")
    
    st.markdown("## 2.1 Dữ liệu nghiên cứu")
    
    st.markdown("### Nguồn dữ liệu")
    st.markdown("""
    Dữ liệu được thu thập từ các cơ sở dữ liệu công khai:
    - **Gene Expression Omnibus (GEO)** - NCBI
    - **ArrayExpress** - EMBL-EBI
    """)
    
    st.markdown("### Tiêu chí lựa chọn")
    st.markdown("""
    - Dữ liệu biểu hiện gen từ mẫu mô ung thư vú người
    - Có thông tin rõ ràng về tình trạng di căn xương
    - Chất lượng dữ liệu đạt chuẩn (kiểm soát chất lượng)
    - Kích thước mẫu đủ lớn để phân tích thống kê
    """)
    
    st.markdown("### Xử lý dữ liệu")
    st.markdown("""
    - Chuẩn hóa dữ liệu biểu hiện gen
    - Loại bỏ các gen có biểu hiện thấp hoặc không thay đổi
    - Xử lý giá trị thiếu và ngoại lệ
    - Chia tập dữ liệu: huấn luyện, kiểm tra, và đánh giá độc lập
    """)
    
    st.markdown("---")
    st.markdown("## 2.2 Phương pháp nghiên cứu")
    
    st.markdown("### Quy trình nghiên cứu")
    # Placeholder for workflow diagram from old HTML
    st.info("Sơ đồ: Quy trình phân tích dữ liệu (image placeholder trong HTML)")
    steps = [
        ("1", "Thu thập & Tiền xử lý dữ liệu", "Tải dữ liệu từ GEO/ArrayExpress, chuẩn hóa, làm sạch dữ liệu"),
        ("2", "Sàng lọc gen khác biệt", "Phân tích thống kê (t-test, fold change) để xác định gen có biểu hiện khác biệt giữa nhóm di căn và không di căn"),
        ("3", "Lựa chọn đặc trưng", "Áp dụng các phương pháp học máy (LASSO, Random Forest feature importance) để chọn gen quan trọng nhất"),
        ("4", "Xây dựng mô hình", "Huấn luyện 7 thuật toán khác nhau: Logistic Regression, Random Forest, SVM, KNN, Decision Tree, AdaBoost, XGBoost"),
        ("5", "Đánh giá & Tối ưu", "So sánh hiệu suất mô hình trên tập kiểm tra và tập độc lập, chọn mô hình tối ưu"),
    ]
    
    for num, title, desc in steps:
        st.markdown(f"**Bước {num}: {title}**")
        st.markdown(f"*{desc}*")
        st.markdown("")
    
    st.markdown("### Các thuật toán học máy được sử dụng")
    st.markdown("""
    - **Logistic Regression:** Mô hình tuyến tính đơn giản, dễ giải thích
    - **Random Forest:** Tập hợp nhiều cây quyết định
    - **Support Vector Machine (SVM):** Tìm siêu phẳng phân chia tối ưu
    - **K-Nearest Neighbors (KNN):** Phân loại dựa trên k mẫu gần nhất
    - **Decision Tree:** Mô hình cây quyết định đơn giản
    - **AdaBoost & XGBoost:** Các phương pháp boosting nâng cao
    """)
    
    st.markdown("### Chỉ số đánh giá")
    st.markdown("""
    - **AUC (Area Under ROC Curve):** Đo lường khả năng phân biệt giữa hai nhóm
    - **Sensitivity (Độ nhạy):** Tỷ lệ phát hiện đúng ca di căn
    - **Specificity (Độ đặc hiệu):** Tỷ lệ phát hiện đúng ca không di căn
    - **Accuracy (Độ chính xác):** Tỷ lệ dự đoán đúng tổng thể
    """)
show()
menu()
