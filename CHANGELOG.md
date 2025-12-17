# Changelog

Tất cả các thay đổi quan trọng của dự án sẽ được ghi lại ở đây.

Format dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và dự án tuân theo [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Hỗ trợ đa ngôn ngữ (tiếng Việt, tiếng Anh, v.v.)
- Visualization cho kết quả phân tích
- So sánh nhiều bài báo
- API endpoint
- Mobile app version

## [1.0.0] - 2025-12-17

### Added
- ✨ Phiên bản đầu tiên của Scientific Paper Analyzer
- 📄 Hỗ trợ import file PDF (tối đa 5 files)
- 🤖 Phân tích với GPT (Claude Sonnet 4)
- 🧠 Phân tích với BERT transformer
- 🔑 Trích xuất từ khóa tự động
- 📝 Tóm tắt nội dung chi tiết
- 📊 Phân tích phương pháp và phát hiện chính
- 📥 Export kết quả (JSON, CSV, Markdown, HTML)
- 🎨 Giao diện Streamlit hiện đại và thân thiện
- 📚 Tài liệu đầy đủ (README, CONTRIBUTING, LICENSE)
- 🔧 Scripts tự động (run.sh, run.bat)
- 🐛 Xử lý lỗi toàn diện

### Components
- `app.py` - Ứng dụng Streamlit chính
- `utils/pdf_processor.py` - Xử lý file PDF
- `utils/gpt_analyzer.py` - Phân tích với Claude API
- `utils/bert_analyzer.py` - Phân tích với BERT
- `utils/export_handler.py` - Export đa định dạng

### Technical Details
- Python 3.9+
- Streamlit 1.31.0
- Transformers 4.36.2 (BERT)
- Anthropic 0.18.1 (Claude API)
- PyTorch 2.1.2
- PyPDF2 3.0.1

---

## Version Format

### [MAJOR.MINOR.PATCH] - YYYY-MM-DD

### Types of Changes
- `Added` - Tính năng mới
- `Changed` - Thay đổi trong tính năng hiện có
- `Deprecated` - Tính năng sẽ bị loại bỏ
- `Removed` - Tính năng đã bị loại bỏ
- `Fixed` - Bug fixes
- `Security` - Cập nhật bảo mật
