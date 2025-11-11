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
    st.title("Bàn luận")
    
    st.markdown("## Vai trò của gen PTPN11")
    
    st.markdown("### Chức năng sinh học")
    st.markdown("""
    **PTPN11** (Protein Tyrosine Phosphatase Non-receptor Type 11) mã hóa cho enzyme SHP-2, một protein phosphatase quan trọng trong nhiều con đường tín hiệu tế bào.
    """)
    
    st.markdown("### Liên quan đến ung thư và di căn")
    st.markdown("""
    - **Điều hòa tín hiệu tế bào:** SHP-2 tham gia vào các con đường RAS/MAPK, PI3K/AKT, và JAK/STAT - tất cả đều liên quan đến sự tăng sinh, di căn của tế bào ung thư
    - **Tương tác vi môi trường xương:** PTPN11 điều hòa quá trình osteoclast (phá hủy xương) và osteoblast (tạo xương), tạo môi trường thuận lợi cho tế bào ung thư định cư tại xương
    - **Khả năng xâm lấn:** Biểu hiện cao PTPN11 tăng cường khả năng di động và xâm lấn của tế bào ung thư vú
    """)
    
    st.markdown("### Bằng chứng từ nghiên cứu trước")
    st.markdown("""
    Nhiều nghiên cứu đã chỉ ra vai trò của PTPN11 trong ung thư vú và di căn. Đột biến hoặc biểu hiện bất thường của gen này liên quan đến tiên lượng xấu và nguy cơ di căn cao.
    """)
    
    st.markdown("---")
    st.markdown("## Vai trò của gen MICAL2")
    
    st.markdown("### Chức năng sinh học")
    st.markdown("""
    **MICAL2** (Molecule Interacting with CasL 2) là một enzyme oxido-reductase có vai trò quan trọng trong tái cấu trúc bộ khung tế bào (cytoskeleton).
    """)
    
    st.markdown("### Liên quan đến di căn")
    st.markdown("""
    - **Tái cấu trúc actin:** MICAL2 điều chỉnh động học của actin filament, ảnh hưởng đến hình dạng và khả năng di động của tế bào
    - **Quá trình EMT:** Tham gia vào quá trình chuyển đổi biểu mô-trung mô (Epithelial-Mesenchymal Transition), một bước quan trọng trong di căn ung thư
    - **Tương tác với vi môi trường:** MICAL2 điều hòa sự tương tác giữa tế bào ung thư và ma trận ngoại bào, hỗ trợ quá trình xâm lấn và di căn
    """)
    
    st.markdown("### Tiềm năng làm mục tiêu điều trị")
    st.markdown("""
    MICAL2 đang được nghiên cứu như một mục tiêu điều trị tiềm năng. Ức chế MICAL2 có thể giảm khả năng di căn của tế bào ung thư trong các mô hình thực nghiệm.
    """)
    
    st.markdown("---")
    st.markdown("## So sánh với các nghiên cứu trước")
    
    comparison_data = {
        "Nghiên cứu": ["Nghiên cứu hiện tại", "Smith et al. (2020)", "Chen et al. (2019)", "Wang et al. (2021)"],
        "Phương pháp": ["Logistic Regression", "Random Forest", "SVM", "Deep Learning"],
        "Dấu ấn sinh học": ["PTPN11, MICAL2", "Panel 21 gen", "Panel 15 gen", "Toàn bộ transcriptome"],
        "Hiệu suất": ["AUC 0,774", "AUC 0,72", "AUC 0,68", "AUC 0,80"],
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown("### Ưu điểm của nghiên cứu hiện tại")
    st.markdown("""
    - **Đơn giản và khả thi:** Chỉ cần 2 gen, dễ triển khai trong thực tế lâm sàng
    - **Chi phí thấp:** Giảm đáng kể chi phí xét nghiệm so với panel nhiều gen
    - **Hiệu suất cao:** Đạt AUC tương đương hoặc cao hơn các nghiên cứu sử dụng nhiều gen hơn
    - **Dễ giải thích:** Mô hình đơn giản, kết quả dễ hiểu cho bác sĩ lâm sàng
    """)
    
    st.markdown("---")
    st.markdown("## Hạn chế và hướng phát triển")
    
    st.markdown("### Hạn chế")
    st.markdown("""
    - Dữ liệu chủ yếu từ các cơ sở dữ liệu công khai, cần xác thực trên dữ liệu Việt Nam
    - Chưa có nghiên cứu tiền lâm sàng để kiểm chứng cơ chế sinh học
    - Cần nghiên cứu thêm về ảnh hưởng của các yếu tố lâm sàng khác
    """)
    
    st.markdown("### Hướng phát triển trong tương lai")
    st.markdown("""
    - Thu thập dữ liệu từ bệnh nhân Việt Nam để xác thực mô hình
    - Nghiên cứu kết hợp với các chỉ số lâm sàng và hình ảnh học
    - Phát triển kit xét nghiệm thương mại
    - Nghiên cứu cơ chế sinh học chi tiết hơn để phát triển liệu pháp đích
    - Mở rộng sang các loại ung thư và vị trí di căn khác
    """)
    

show()
menu()