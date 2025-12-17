"""
Scientific Paper Analyzer
Ứng dụng phân tích bài báo khoa học sử dụng GPT và BERT
Phát triển bởi: Nhóm 6 - Công nghệ số nâng cao
"""

import streamlit as st
import os
from datetime import datetime
import json
import config
from utils.pdf_processor import PDFProcessor
from utils.gpt_analyzer import GPTAnalyzer
from utils.bert_analyzer import BERTAnalyzer
from utils.chatgpt_analyzer import ChatGPTAnalyzer
from utils.groq_analyzer import GroqAnalyzer
from utils.export_handler import ExportHandler
from utils.chatbot import DataChatbot, DataProcessor

# Cấu hình trang
st.set_page_config(
    page_title="Scientific Paper Analyzer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e3a8a 0%, #312e81 50%, #1e3a8a 100%);
    }
    
    .upload-box {
        border: 3px dashed #60a5fa;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        background: rgba(255, 255, 255, 0.05);
        margin: 20px 0;
    }
    
    .result-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .keyword-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-weight: 600;
    }
    
    .section-header {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 30px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .info-box {
        background: rgba(96, 165, 250, 0.2);
        border-left: 4px solid #60a5fa;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
        color: white;
    }
    
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a8a 0%, #312e81 100%);
    }
    
    div[data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

def init_session_state():
    """Khởi tạo session state"""
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = []
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None
    if 'processing_type' not in st.session_state:
        st.session_state.processing_type = None
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = None
    if 'chatbot_data_loaded' not in st.session_state:
        st.session_state.chatbot_data_loaded = False
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def display_header():
    """Hiển thị header"""
    st.markdown('<h1 class="section-header">🧠 Scientific Paper Analyzer</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; color: #93c5fd; font-size: 1.2rem; margin-bottom: 30px;">
            Phân tích bài báo khoa học thông minh với AI
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

def get_page_selection():
    """Lấy lựa chọn trang từ sidebar"""
    with st.sidebar:
        st.markdown("### 📑 ĐIỀU HƯỚNG")
        page = st.radio(
            "Chọn chức năng:",
            ["📄 Phân Tích Bài Báo", "💬 Chatbot Dữ Liệu"],
            label_visibility="collapsed"
        )
        st.markdown("---")
    return page

def display_sidebar():
    """Hiển thị sidebar với thông tin và cài đặt"""
    with st.sidebar:
        st.markdown("### ⚙️ Cài Đặt")
        
        # API Key cho Groq (Từ config.py)
        if config.GROQ_API_KEY:
            os.environ['GROQ_API_KEY'] = config.GROQ_API_KEY
            st.success("✅ Groq API Key đã được cài đặt sẵn!")
        else:
            groq_key = st.text_input(
                "Groq API Key (MIỄN PHÍ) ⭐",
                type="password",
                help="API key MIỄN PHÍ, lấy tại: https://console.groq.com/keys"
            )
            if groq_key:
                os.environ['GROQ_API_KEY'] = groq_key
        
        st.markdown("---")
        
        # API Key cho ChatGPT (TÙY CHỌN)
        with st.expander("💬 ChatGPT API (Có phí - Không bắt buộc)"):
            openai_key = st.text_input(
                "OpenAI API Key (ChatGPT)",
                type="password",
                help="Chỉ cần nếu muốn dùng ChatGPT. Lấy tại: https://platform.openai.com/api-keys"
            )
            
            if openai_key:
                os.environ['OPENAI_API_KEY'] = openai_key
        
        st.markdown("---")
        
        # Thông tin
        st.markdown("### 📊 Thông Tin")
        st.markdown("""
        **Tính năng:**
        - 📄 Import file PDF
        - 🚀 Phân tích với Groq (MIỄN PHÍ) ⭐
        - 💬 Phân tích với ChatGPT (Có phí)
        - 🧠 Phân tích với BERT (MIỄN PHÍ)
        - 📥 Export kết quả
        
        **Giới hạn:**
        - Tối đa 5 bài báo/lần
        - Format: PDF
        - Kích thước: < 50MB/file
        
        **Khuyến nghị:**
        - ⭐ Groq: MIỄN PHÍ + Nhanh nhất!
        - 🧠 BERT: MIỄN PHÍ + Offline
        - 💬 ChatGPT: Có phí (~$10)
        """)
        
        st.markdown("---")
        
        st.markdown("### 👨‍💻 Về Dự Án")
        st.markdown("""
        **Phiên bản:** 1.0.0
        
        **Công nghệ:**
        - Python 3.9+
        - Streamlit
        - Transformers (BERT)
        - Groq API (LLaMA 3.3)
        
        **Tác giả:** Nhóm 6 - Công nghệ số nâng cao
        
        © 2025 All rights reserved
        """)

def display_upload_section():
    """Hiển thị phần upload file"""
    st.markdown("### 📄 Import Bài Báo Khoa Học")
    
    uploaded_files = st.file_uploader(
        "Chọn tối đa 5 file PDF",
        type=['pdf'],
        accept_multiple_files=True,
        help="Kéo thả hoặc click để chọn file PDF"
    )
    
    if uploaded_files:
        if len(uploaded_files) > 5:
            st.error("⚠️ Vui lòng chỉ chọn tối đa 5 bài báo!")
            return None
        
        st.session_state.uploaded_files = uploaded_files
        
        # Hiển thị danh sách file
        st.markdown("#### 📋 Danh Sách File Đã Chọn")
        for i, file in enumerate(uploaded_files, 1):
            file_size = file.size / (1024 * 1024)  # Convert to MB
            st.markdown(f"""
                <div class="info-box">
                    <strong>{i}. {file.name}</strong><br>
                    Kích thước: {file_size:.2f} MB
                </div>
            """, unsafe_allow_html=True)
        
        return uploaded_files
    
    return None

def display_processing_section(uploaded_files):
    """Hiển thị phần xử lý"""
    st.markdown("### 🚀 Xử Lý Phân Tích")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Xử Lý Với Groq", use_container_width=True, type="primary"):
            if not os.environ.get('GROQ_API_KEY'):
                st.error("⚠️ Vui lòng nhập Groq API Key trong sidebar!")
                st.info("💡 MIỄN PHÍ! Lấy tại: https://console.groq.com/keys")
                return
            
            with st.spinner("🔄 Đang xử lý với Groq (LLaMA 3.3)..."):
                try:
                    processor = PDFProcessor()
                    analyzer = GroqAnalyzer()
                    
                    results = []
                    progress_bar = st.progress(0)
                    
                    for i, file in enumerate(uploaded_files):
                        text = processor.extract_text(file)
                        analysis = analyzer.analyze(text, file.name)
                        results.append(analysis)
                        progress_bar.progress((i + 1) / len(uploaded_files))
                    
                    st.session_state.analysis_results = {
                        'type': 'Groq (LLaMA 3.3) - MIỄN PHÍ',
                        'timestamp': datetime.now().isoformat(),
                        'papers': results
                    }
                    st.session_state.processing_type = 'Groq'
                    st.success("✅ Hoàn thành phân tích với Groq!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Lỗi xử lý: {str(e)}")
                    st.info("💡 Kiểm tra lại API key hoặc thử lại sau vài giây")
    
    with col2:
        if st.button("💬 Xử Lý Với ChatGPT", use_container_width=True, type="secondary"):
            if not os.environ.get('OPENAI_API_KEY'):
                st.warning("⚠️ Cần OpenAI API Key (có phí)")
                st.info("💡 Hoặc dùng Groq (miễn phí) ở cột bên trái!")
                return
            
            with st.spinner("🔄 Đang xử lý với ChatGPT..."):
                try:
                    processor = PDFProcessor()
                    analyzer = ChatGPTAnalyzer()
                    
                    results = []
                    progress_bar = st.progress(0)
                    
                    for i, file in enumerate(uploaded_files):
                        text = processor.extract_text(file)
                        analysis = analyzer.analyze(text, file.name)
                        results.append(analysis)
                        progress_bar.progress((i + 1) / len(uploaded_files))
                    
                    st.session_state.analysis_results = {
                        'type': 'ChatGPT (OpenAI)',
                        'timestamp': datetime.now().isoformat(),
                        'papers': results
                    }
                    st.session_state.processing_type = 'ChatGPT'
                    st.success("✅ Hoàn thành phân tích với ChatGPT!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Lỗi xử lý: {str(e)}")
    
    with col3:
        if st.button("🧠 Xử Lý Với BERT", use_container_width=True, type="secondary"):
            with st.spinner("🔄 Đang xử lý với BERT..."):
                try:
                    processor = PDFProcessor()
                    analyzer = BERTAnalyzer()
                    
                    results = []
                    progress_bar = st.progress(0)
                    
                    for i, file in enumerate(uploaded_files):
                        text = processor.extract_text(file)
                        analysis = analyzer.analyze(text, file.name)
                        results.append(analysis)
                        progress_bar.progress((i + 1) / len(uploaded_files))
                    
                    st.session_state.analysis_results = {
                        'type': 'BERT',
                        'timestamp': datetime.now().isoformat(),
                        'papers': results
                    }
                    st.session_state.processing_type = 'BERT'
                    st.success("✅ Hoàn thành phân tích với BERT!")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Lỗi xử lý: {str(e)}")

def display_chatbot_page():
    """Hiển thị trang Chatbot"""
    st.markdown("## 💬 Chatbot Tương Tác Với Dữ Liệu")
    
    st.markdown("""
        <div class="info-box">
            <strong>🎯 Hướng dẫn sử dụng:</strong><br>
            1. Upload file dữ liệu (Excel, CSV, hoặc PDF)<br>
            2. Đặt câu hỏi về dữ liệu<br>
            3. Chatbot sẽ trả lời dựa trên dữ liệu đã upload<br>
            <br>
            <em>💡 Chatbot sử dụng Groq AI (miễn phí) để phân tích và trả lời câu hỏi</em>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📂 Bước 1: Upload Dữ Liệu")
    
    uploaded_data = st.file_uploader(
        "Chọn file dữ liệu",
        type=['xlsx', 'xls', 'csv', 'pdf'],
        help="Hỗ trợ: Excel (.xlsx, .xls), CSV (.csv), PDF (.pdf)",
        key="chatbot_uploader"
    )
    
    if uploaded_data:
        file_size = uploaded_data.size / (1024 * 1024)
        file_type = uploaded_data.name.split('.')[-1].upper()
        
        st.markdown(f"""
            <div class="info-box">
                <strong>📄 File đã chọn:</strong> {uploaded_data.name}<br>
                <strong>📊 Loại:</strong> {file_type}<br>
                <strong>💾 Kích thước:</strong> {file_size:.2f} MB
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔄 Load Dữ Liệu", type="primary", use_container_width=True):
            if not os.environ.get('GROQ_API_KEY'):
                st.error("⚠️ Vui lòng nhập Groq API Key trong sidebar!")
                st.info("💡 Lấy key MIỄN PHÍ tại: https://console.groq.com/keys")
                return
            
            with st.spinner(f"Đang xử lý file {file_type}..."):
                try:
                    if st.session_state.chatbot is None:
                        st.session_state.chatbot = DataChatbot()
                    
                    data_processor = DataProcessor()
                    
                    if file_type in ['XLSX', 'XLS']:
                        data_text = data_processor.process_excel(uploaded_data)
                    elif file_type == 'CSV':
                        data_text = data_processor.process_csv(uploaded_data)
                    elif file_type == 'PDF':
                        pdf_processor = PDFProcessor()
                        data_text = data_processor.process_pdf(uploaded_data, pdf_processor)
                    else:
                        st.error("Định dạng file không được hỗ trợ!")
                        return
                    
                    st.session_state.chatbot.load_data_context(data_text, uploaded_data.name)
                    st.session_state.chatbot_data_loaded = True
                    st.session_state.chat_history = []
                    
                    st.success(f"✅ Đã load dữ liệu từ {uploaded_data.name}!")
                    st.info("💬 Bây giờ bạn có thể đặt câu hỏi ở phần bên dưới!")
                    
                except Exception as e:
                    st.error(f"❌ Lỗi: {str(e)}")
    
    if st.session_state.chatbot_data_loaded:
        st.markdown("---")
        st.markdown("### 💬 Bước 2: Đặt Câu Hỏi")
        
        if st.session_state.chat_history:
            st.markdown("#### 📜 Lịch Sử Hội Thoại")
            for chat in st.session_state.chat_history:
                if chat['role'] == 'user':
                    st.markdown(f"""
                        <div style="background: rgba(96, 165, 250, 0.2); padding: 15px; border-radius: 10px; margin: 10px 0;">
                            <strong>👤 Bạn:</strong><br>{chat['content']}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div style="background: rgba(168, 85, 247, 0.2); padding: 15px; border-radius: 10px; margin: 10px 0;">
                            <strong>🤖 Chatbot:</strong><br>{chat['content']}
                        </div>
                    """, unsafe_allow_html=True)
        
        st.markdown("#### ✍️ Câu Hỏi Mới")
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_question = st.text_input(
                "Nhập câu hỏi của bạn:",
                placeholder="Ví dụ: Tổng số bao nhiêu? Có bao nhiêu mục?",
                label_visibility="collapsed",
                key="chat_input"
            )
        
        with col2:
            ask_button = st.button("🚀 Hỏi", use_container_width=True, type="primary")
        
        if ask_button and user_question:
            with st.spinner("🤔 Đang suy nghĩ..."):
                try:
                    answer = st.session_state.chatbot.ask(user_question)
                    
                    st.session_state.chat_history.append({
                        'role': 'user',
                        'content': user_question
                    })
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': answer
                    })
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Lỗi: {str(e)}")
        
        if st.session_state.chat_history:
            if st.button("🗑️ Xóa Lịch Sử Hội Thoại", type="secondary"):
                st.session_state.chat_history = []
                st.session_state.chatbot.clear_history()
                st.rerun()

def display_results():
    """Hiển thị kết quả phân tích"""
    results = st.session_state.analysis_results
    
    if not results:
        return
    
    st.markdown("---")
    st.markdown(f"### 📊 Kết Quả Phân Tích - {results['type']}")
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col2:
        export_handler = ExportHandler()
        json_data = export_handler.to_json(results)
        st.download_button(
            label="📥 Export JSON",
            data=json_data,
            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    with col3:
        csv_data = export_handler.to_csv(results)
        st.download_button(
            label="📥 Export CSV",
            data=csv_data,
            file_name=f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    for i, paper in enumerate(results['papers'], 1):
        with st.expander(f"📄 Bài báo {i}: {paper['title'][:100]}...", expanded=True):
            st.markdown(f"**Tên file:** {paper['filename']}")
            
            st.markdown("#### 📝 Tóm Tắt")
            st.info(paper['summary'])
            
            st.markdown("#### 🔑 Từ Khóa")
            keywords_html = "".join([
                f'<span class="keyword-tag">{kw}</span>' 
                for kw in paper['keywords']
            ])
            st.markdown(keywords_html, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### 🎯 Phát Hiện Chính")
                st.success(paper['main_findings'])
            
            with col2:
                st.markdown("#### 🔬 Phương Pháp Nghiên Cứu")
                st.warning(paper['methodology'])

def main():
    """Hàm chính"""
    init_session_state()
    display_header()
    
    page = get_page_selection()
    display_sidebar()
    
    if page == "📄 Phân Tích Bài Báo":
        uploaded_files = display_upload_section()
        
        if uploaded_files and len(uploaded_files) <= 5:
            display_processing_section(uploaded_files)
        
        if st.session_state.analysis_results:
            display_results()
    
    elif page == "💬 Chatbot Dữ Liệu":
        display_chatbot_page()
    
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #93c5fd; padding: 20px;">
            Phát triển với ❤️ bởi Nhóm 6 - Công nghệ số nâng cao | © 2025
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()