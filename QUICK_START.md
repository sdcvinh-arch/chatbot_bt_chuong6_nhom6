# 🚀 Hướng Dẫn Khởi Động Nhanh

## Cài Đặt Trong 5 Phút

### Bước 1: Clone Repository

```bash
git clone https://github.com/yourusername/scientific-paper-analyzer.git
cd scientific-paper-analyzer
```

### Bước 2: Cài Đặt Dependencies

**Linux/macOS:**
```bash
./run.sh
```

**Windows:**
```bash
run.bat
```

Hoặc cài đặt thủ công:

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt (Linux/Mac)
source venv/bin/activate

# Kích hoạt (Windows)
venv\Scripts\activate

# Cài đặt packages
pip install -r requirements.txt
```

### Bước 3: Cấu Hình API Key

1. Tạo file `.env`:
```bash
cp .env.example .env
```

2. Lấy API key từ [Anthropic Console](https://console.anthropic.com/)

3. Thêm vào file `.env`:
```env
ANTHROPIC_API_KEY=your_actual_api_key_here
```

### Bước 4: Chạy Ứng Dụng

```bash
streamlit run app.py
```

Truy cập: `http://localhost:8501`

## ⚡ Sử Dụng Nhanh

1. **Upload PDF**: Click "Browse files" và chọn 1-5 bài báo PDF
2. **Nhập API Key**: (Nếu chưa có trong .env) Nhập trong sidebar
3. **Chọn Phân Tích**: Click "🤖 Xử Lý Với GPT" hoặc "🧠 Xử Lý Với BERT"
4. **Xem Kết Quả**: Đọc tóm tắt, từ khóa, phát hiện
5. **Export**: Click "📥 Export JSON" hoặc "📥 Export CSV"

## 🎯 Ví Dụ Demo

### Input
- File: `sample_paper.pdf`
- Phương thức: GPT

### Output
```json
{
  "title": "Deep Learning for Natural Language Processing",
  "summary": "Nghiên cứu này trình bày...",
  "keywords": ["deep learning", "NLP", "transformer"],
  "main_findings": "Kết quả cho thấy...",
  "methodology": "Sử dụng BERT với fine-tuning..."
}
```

## 🔧 Xử Lý Sự Cố

### Lỗi API Key
```
⚠️ Vui lòng nhập Anthropic API Key
```
**Giải pháp**: Kiểm tra file `.env` hoặc nhập API key trong sidebar

### Lỗi Import
```
ModuleNotFoundError: No module named 'streamlit'
```
**Giải pháp**: Chạy `pip install -r requirements.txt`

### Lỗi PDF
```
❌ Lỗi khi đọc file PDF
```
**Giải pháp**: Đảm bảo PDF có text, không phải scan image

## 📚 Tài Liệu Đầy Đủ

Xem [README.md](README.md) để biết thêm chi tiết về:
- Tính năng đầy đủ
- Cấu trúc dự án
- API documentation
- Đóng góp code

## 💡 Tips

- **Tốc độ**: GPT chậm hơn (~15s) nhưng chính xác hơn BERT (~8s)
- **Chất lượng**: GPT cho kết quả chi tiết hơn
- **Chi phí**: BERT miễn phí, GPT cần API key
- **Batch**: Có thể upload 5 files cùng lúc
- **Language**: Hỗ trợ cả tiếng Anh và tiếng Việt

## 🎓 Video Tutorial

Coming soon...

## 📞 Trợ Giúp

- GitHub Issues: [Link to issues]
- Email: nhom6@example.com
- Documentation: [Link to docs]

---

**Thời gian setup**: ~5 phút | **Độ khó**: ⭐⭐ Dễ
