import os
import streamlit as st
from Config import Config

def menu():
  st.sidebar.page_link('./app.py', label='Trang chủ')
  st.sidebar.page_link('./pages/overview.py', label='Tổng quan')
  st.sidebar.page_link('./pages/methods.py', label='Phương pháp')
  st.sidebar.page_link('./pages/results.py', label='Kết quả')
  st.sidebar.page_link('./pages/discussion.py', label='Bàn luận')
  st.sidebar.page_link('./pages/calculator.py', label='Tính toán')
  st.sidebar.page_link('./pages/extras.py', label='Phụ lục')



if __name__ == '__main__':
  st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon=Config.APP_ICON,
    layout="wide"
  )

  def show():
    st.title("ỨNG DỤNG MÔ HÌNH HỌC MÁY SỬ DỤNG DẤU ẤN SINH HỌC ĐỂ DỰ ĐOÁN UNG THƯ VÚ DI CĂN XƯƠNG")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Mã số:** 2526_KHTN_08
        
        **Trường:** Trường THPT Gia Định, TP. Hồ Chí Minh
        """)
    
    with col2:
        st.markdown("""
        **Học sinh thực hiện:** Trần Nguyễn Anh Thoa, Trần Ngọc Khôi Nguyên
        
        **Giáo viên hướng dẫn:** ThS. Cao Hoài Đức
        """)
    
    st.markdown("---")
    
    # Statistics Section
    st.markdown("### Thống kê chính")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Số ca ung thư vú mới/năm", "2.3 triệu")
        st.caption("Trên toàn cầu")
    
    with col2:
        st.metric("Tỷ lệ tiến triển di căn", "25%")
        st.caption("Chuyển sang giai đoạn di căn")
    
    with col3:
        st.metric("Tỷ lệ di căn xương", "77.5%")
        st.caption("Ca di căn liên quan đến xương")
    
    st.markdown("---")
    
    st.markdown("### Giới thiệu dự án")
    st.markdown("""
    Nghiên cứu của chúng tôi phát triển một mô hình học máy sử dụng hai dấu ấn sinh học (PTPN11 và MICAL2) để dự đoán nguy cơ di căn xương ở bệnh nhân ung thư vú. Với độ chính xác AUC 0,774 và độ nhạy 77,8%, công cụ này có tiềm năng hỗ trợ phát hiện sớm và theo dõi bệnh nhân nguy cơ cao.
    """)
    
    # col1, col2 = st.columns(2)
    # with col1:
    #     if st.button("Thử nghiệm công cụ dự đoán", key="home_calc"):
    #         st.session_state.page = "Công cụ dự đoán"
    #         st.rerun()
    
    # with col2:
    #     if st.button("Tìm hiểu thêm", key="home_overview"):
    #         st.session_state.page = "Tổng quan"
    #         st.rerun()

  show()

  menu()
  


  
