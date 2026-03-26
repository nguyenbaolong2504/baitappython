import streamlit as st
import google.generativeai as genai

# --- CẤU HÌNH API KEY ---
# Dán mã AIzaSy... của bạn vào đây
MY_API_KEY = "AIzaSyDCw3xwceIMoETpeR6t5bHb9tSihtmfpcI"

genai.configure(api_key=MY_API_KEY)

# --- GIAO DIỆN ---
st.set_page_config(page_title="AI Code Generator", page_icon="🤖")
st.title("🤖 AI Code Generator (Gemini Fixed)")

# Ô nhập yêu cầu
user_input = st.text_area("Nhập yêu cầu bài lập trình của bạn:", 
                          placeholder="Ví dụ: Viết code tính tổng từ 1 đến n")

if st.button("Tạo mã nguồn ✨"):
    if user_input:
        with st.spinner("Đang xử lý..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                
                response = model.generate_content(f"Viết code Python cho: {user_input}. Giải thích ngắn gọn bằng tiếng Việt.")
                
                st.success("Hoàn thành!")
                st.markdown("### Kết quả mã nguồn:")
                st.code(response.text, language="python")
                
            except Exception as e:
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Vui lòng nhập nội dung yêu cầu!")