import streamlit as st
from app import menu

from Config import Config

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

def show():
    st.title("Tổng quan nghiên cứu")
    
    st.markdown("## I. Lý do chọn đề tài")
    st.markdown("""
    Ung thư vú là loại ung thư phổ biến nhất ở phụ nữ với khoảng 2,3 triệu ca mới mỗi năm trên toàn cầu. Khoảng 20-30% bệnh nhân ung thư vú sẽ tiến triển đến giai đoạn di căn, trong đó 70-85% ca di căn liên quan đến xương.

    Việc phát hiện sớm nguy cơ di căn xương là then chốt để cải thiện chất lượng cuộc sống và tăng tỷ lệ sống còn của bệnh nhân. Tuy nhiên, các phương pháp hiện tại như chụp xương đồng vị, PET/CT thường tốn kém và chỉ phát hiện khi đã có tổn thương.

    **Dấu ấn sinh học (biomarker)** cung cấp một giải pháp tiềm năng: có thể dự đoán nguy cơ di căn sớm thông qua phân tích biểu hiện gen từ mẫu máu hoặc mô u ban đầu. Việc áp dụng học máy (machine learning) vào phân tích dữ liệu gen giúp xây dựng mô hình dự đoán chính xác và hiệu quả.
    """)
    # Optional image from old HTML
    try:
        from pathlib import Path
        img_path = Path(__file__).resolve().parents[2] / "old_app" / "media" / "graphic-asr-inc-both-sexes-in-2022-breast.png"
        if img_path.exists():
            st.image(str(img_path), caption="Tỉ lệ mắc ung thư vú toàn cầu và Việt Nam", use_column_width=True)
        else:
            st.info("Hình ảnh tổng quan chưa được thêm (media/graphic-asr-inc-both-sexes-in-2022-breast.png).")
    except Exception:
        st.info("Hình ảnh tổng quan chưa được thêm (media/graphic-asr-inc-both-sexes-in-2022-breast.png).")
    
    st.markdown("---")
    st.markdown("## II. Mục tiêu nghiên cứu")
    
    st.markdown("### Mục tiêu chung")
    st.markdown("Xây dựng mô hình học máy sử dụng dấu ấn sinh học để dự đoán nguy cơ di căn xương ở bệnh nhân ung thư vú.")
    
    st.markdown("### Mục tiêu cụ thể")
    st.markdown("""
    - Xác định các dấu ấn sinh học (gen) có khả năng dự đoán di căn xương
    - So sánh hiệu quả của các thuật toán học máy khác nhau
    - Đánh giá độ chính xác của mô hình trên dữ liệu độc lập
    - Phát triển công cụ dự đoán nguy cơ có thể ứng dụng thực tiễn
    """)
    
    st.markdown("---")
    st.markdown("## III. Nhiệm vụ nghiên cứu")
    
    tasks = [
        ("📊", "Thu thập và xử lý dữ liệu", "Tổng hợp dữ liệu biểu hiện gen từ các cơ sở dữ liệu công khai (GEO, ArrayExpress), chuẩn hóa và làm sạch dữ liệu."),
        ("🧬", "Sàng lọc dấu ấn sinh học", "Áp dụng các phương pháp thống kê và học máy để xác định các gen có khả năng phân biệt nhóm di căn xương và không di căn."),
        ("🤖", "Xây dựng và đánh giá mô hình", "Huấn luyện nhiều mô hình học máy, so sánh hiệu suất, và chọn mô hình tối ưu. Đánh giá trên tập dữ liệu độc lập."),
    ]
    
    for icon, title, desc in tasks:
        st.markdown(f"### {icon} {title}")
        st.markdown(desc)
    
    st.markdown("---")
    st.markdown("## IV. Ý nghĩa nghiên cứu")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ✨ Tính mới")
        st.markdown("Nghiên cứu đầu tiên tại Việt Nam áp dụng học máy để dự đoán di căn xương ung thư vú dựa trên dấu ấn sinh học PTPN11 và MICAL2.")
        
        st.markdown("### 🔬 Tính khoa học")
        st.markdown("Sử dụng phương pháp nghiên cứu nghiêm ngặt, dữ liệu công khai có thể tái lập, và đánh giá trên nhiều tập dữ liệu độc lập.")
    
    with col2:
        st.markdown("### 🏥 Tính thực tiễn")
        st.markdown("Cung cấp công cụ hỗ trợ quyết định lâm sàng, giúp bác sĩ xác định bệnh nhân nguy cơ cao cần theo dõi sát sao.")
        
        st.markdown("### 🌍 Tính cộng đồng")
        st.markdown("Tiềm năng giảm chi phí theo dõi, phát hiện sớm di căn, cải thiện chất lượng cuộc sống và tỷ lệ sống còn của bệnh nhân.")

show()
menu()