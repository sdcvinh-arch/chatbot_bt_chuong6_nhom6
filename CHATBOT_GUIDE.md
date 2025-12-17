# 💬 Hướng Dẫn Sử Dụng Chatbot Dữ Liệu

## 🎯 Tính Năng Mới: Chatbot Tương Tác

Ứng dụng bây giờ có **2 CHỨC NĂNG CHÍNH**:

### **1. 📄 Phân Tích Bài Báo**
- Phân tích bài báo khoa học (PDF)
- Trích xuất tóm tắt, từ khóa, phương pháp
- Export kết quả

### **2. 💬 Chatbot Dữ Liệu** ⭐ MỚI!
- Upload dữ liệu (Excel, CSV, PDF)
- Đặt câu hỏi về dữ liệu
- Chatbot trả lời thông minh

---

## 🚀 Cách Sử Dụng Chatbot

### **Bước 1: Chuyển sang trang Chatbot**

1. Chạy ứng dụng: `streamlit run app.py`
2. Mở **Sidebar** (click mũi tên `>` nếu đóng)
3. Chọn **"💬 Chatbot Dữ Liệu"**

### **Bước 2: Upload Dữ Liệu**

**Hỗ trợ các định dạng:**
- ✅ **Excel** (.xlsx, .xls) - Bảng tính
- ✅ **CSV** (.csv) - Dữ liệu phân cách bằng dấu phẩy
- ✅ **PDF** (.pdf) - Tài liệu, báo cáo

**Cách upload:**
1. Click **"Browse files"** hoặc kéo thả file
2. Click **"🔄 Load Dữ Liệu"**
3. Chờ xử lý (3-5 giây)
4. ✅ Thấy thông báo "Đã load dữ liệu"!

### **Bước 3: Đặt Câu Hỏi**

1. Nhập câu hỏi vào ô text
2. Click **"🚀 Hỏi"**
3. Chatbot trả lời trong 2-3 giây
4. Hỏi tiếp câu hỏi khác!

---

## 💡 Ví Dụ Sử Dụng

### **Ví Dụ 1: Phân Tích Dữ Liệu Sinh Viên**

**File:** `danh_sach_sinh_vien.xlsx`

| STT | Họ Tên | MSSV | Điểm TB | Xếp Loại |
|-----|--------|------|---------|----------|
| 1 | Nguyễn Văn A | 2021001 | 8.5 | Giỏi |
| 2 | Trần Thị B | 2021002 | 7.2 | Khá |
| 3 | Lê Văn C | 2021003 | 9.0 | Xuất sắc |

**Câu hỏi có thể hỏi:**
```
👤 "Có bao nhiêu sinh viên trong danh sách?"
🤖 "Trong danh sách có 3 sinh viên."

👤 "Sinh viên nào có điểm cao nhất?"
🤖 "Lê Văn C có điểm cao nhất với 9.0 điểm, xếp loại Xuất sắc."

👤 "Điểm trung bình của lớp là bao nhiêu?"
🤖 "Điểm trung bình của lớp là 8.23 điểm."

👤 "Có bao nhiêu sinh viên xếp loại Giỏi trở lên?"
🤖 "Có 2 sinh viên xếp loại Giỏi trở lên (1 Giỏi và 1 Xuất sắc)."
```

---

### **Ví Dụ 2: Phân Tích Doanh Thu**

**File:** `doanh_thu_2024.csv`

| Tháng | Doanh Thu | Chi Phí | Lợi Nhuận |
|-------|-----------|---------|-----------|
| 1 | 100,000,000 | 70,000,000 | 30,000,000 |
| 2 | 120,000,000 | 80,000,000 | 40,000,000 |
| 3 | 150,000,000 | 90,000,000 | 60,000,000 |

**Câu hỏi:**
```
👤 "Tổng doanh thu quý 1 là bao nhiêu?"
🤖 "Tổng doanh thu quý 1 (3 tháng đầu năm) là 370,000,000 VNĐ."

👤 "Tháng nào có lợi nhuận cao nhất?"
🤖 "Tháng 3 có lợi nhuận cao nhất với 60,000,000 VNĐ."

👤 "Tỷ lệ lợi nhuận trung bình là bao nhiêu?"
🤖 "Tỷ lệ lợi nhuận trung bình là 35.14% (130,000,000 / 370,000,000)."
```

---

### **Ví Dụ 3: Tóm Tắt Tài Liệu PDF**

**File:** `bao_cao_nghien_cuu.pdf`

**Câu hỏi:**
```
👤 "Tóm tắt nội dung chính của tài liệu"
🤖 "Tài liệu trình bày nghiên cứu về ứng dụng AI trong giáo dục, 
     bao gồm 3 phần chính: (1) Tổng quan công nghệ AI, (2) Ứng dụng 
     trong dạy và học, (3) Kết quả thí nghiệm tại 5 trường đại học."

👤 "Có bao nhiêu trường tham gia thí nghiệm?"
🤖 "Có 5 trường đại học tham gia thí nghiệm."

👤 "Kết luận chính của nghiên cứu là gì?"
🤖 "Kết luận chính là việc áp dụng AI giúp cải thiện hiệu quả 
     học tập lên 35% và tăng sự hứng thú của sinh viên lên 48%."
```

---

## 🎓 Use Cases Cho Sinh Viên

### **1. Phân Tích Dữ Liệu Đồ Án**

Upload file Excel/CSV chứa dữ liệu khảo sát, thí nghiệm:
```
"Số lượng mẫu khảo sát là bao nhiêu?"
"Tỷ lệ người trả lời Đồng ý là bao nhiêu?"
"Có sự khác biệt giữa nam và nữ không?"
```

### **2. Tổng Hợp Tài Liệu**

Upload file PDF (bài báo, luận văn):
```
"Tóm tắt nội dung chính"
"Phương pháp nghiên cứu là gì?"
"Tác giả đề xuất giải pháp gì?"
```

### **3. Phân Tích Số Liệu**

Upload dữ liệu thống kê:
```
"Giá trị trung bình là bao nhiêu?"
"Giá trị cao nhất/thấp nhất?"
"Xu hướng thay đổi như thế nào?"
```

---

## 💬 Tips Đặt Câu Hỏi Hiệu Quả

### **✅ NÊN:**

**Cụ thể và rõ ràng:**
```
❌ "Thông tin gì?"
✅ "Tổng doanh thu tháng 3 là bao nhiêu?"

❌ "Số liệu?"
✅ "Số lượng sinh viên xếp loại Giỏi là bao nhiêu?"
```

**Hỏi từng phần:**
```
✅ "Có bao nhiêu bản ghi?"
✅ "Giá trị trung bình của cột X?"
✅ "So sánh A và B như thế nào?"
```

**Sử dụng từ khóa:**
```
✅ "Tổng, trung bình, tỷ lệ"
✅ "Cao nhất, thấp nhất, nhiều nhất"
✅ "So sánh, khác biệt, tương quan"
```

### **❌ KHÔNG NÊN:**

```
❌ "Nói hết cho tôi" (quá rộng)
❌ "Câu 5 là gì?" (không có trong dữ liệu)
❌ "Dự đoán tương lai" (chatbot chỉ phân tích dữ liệu có sẵn)
```

---

## 🔧 Tính Năng Chatbot

### **1. Context-Aware**
- Chatbot nhớ toàn bộ dữ liệu đã upload
- Trả lời dựa trên dữ liệu thực tế
- Không bịa đặt thông tin

### **2. Multi-Turn Conversation**
- Có thể hỏi nhiều câu liên tiếp
- Chatbot nhớ ngữ cảnh hội thoại
- Giới hạn 10 tin nhắn gần nhất

### **3. Smart Analysis**
- Tự động tính toán (tổng, trung bình, tỷ lệ)
- So sánh và phân tích xu hướng
- Trích dẫn số liệu cụ thể

### **4. Multiple File Types**
- Excel: Đọc tất cả sheets
- CSV: Tự động detect encoding
- PDF: Trích xuất text (tối đa 20 trang)

---

## 📊 Giới Hạn

### **Dung Lượng:**
- Dữ liệu: 30,000 ký tự (~15-20 trang)
- Excel: Tối đa 1000 hàng
- PDF: Tối đa 20 trang

### **Chức Năng:**
- ✅ Phân tích dữ liệu có sẵn
- ✅ Tính toán thống kê
- ✅ Tóm tắt nội dung
- ❌ Không dự đoán tương lai
- ❌ Không tạo dữ liệu mới
- ❌ Không vẽ biểu đồ (chỉ mô tả)

---

## 🆘 Xử Lý Lỗi

### **Lỗi: "GROQ_API_KEY không được thiết lập"**
```
⚠️ Cần Groq API Key để sử dụng Chatbot
```
**Giải pháp:**
1. Lấy key MIỄN PHÍ tại: https://console.groq.com/keys
2. Nhập vào Sidebar → "Groq API Key"

### **Lỗi: "Không tìm thấy thông tin"**
```
🤖 "Không tìm thấy thông tin này trong dữ liệu"
```
**Nguyên nhân:**
- Thông tin không có trong file
- Câu hỏi không liên quan đến dữ liệu
- Dữ liệu quá lớn (bị cắt)

**Giải pháp:**
- Hỏi câu khác cụ thể hơn
- Kiểm tra lại dữ liệu đã upload
- Upload file nhỏ hơn

### **Lỗi: "Error reading Excel/CSV"**
```
❌ Lỗi đọc file Excel
```
**Giải pháp:**
- Kiểm tra file không bị hỏng
- Đảm bảo đúng định dạng .xlsx, .xls, .csv
- Thử save lại file

---

## 💡 Best Practices

### **Để Có Kết Quả Tốt Nhất:**

1. **Chuẩn bị dữ liệu tốt:**
   - File không quá lớn (< 1MB)
   - Dữ liệu có cấu trúc rõ ràng
   - Có headers/tiêu đề cột

2. **Đặt câu hỏi rõ ràng:**
   - Một câu hỏi, một vấn đề
   - Sử dụng từ khóa cụ thể
   - Tham khảo ví dụ ở trên

3. **Kiểm tra kết quả:**
   - Cross-check với dữ liệu gốc
   - Hỏi lại nếu không chắc chắn
   - Sử dụng cho tham khảo, không 100% chính xác

---

## 🎯 Kết Luận

**Chatbot Dữ Liệu là công cụ mạnh mẽ để:**
- ✅ Phân tích dữ liệu nhanh chóng
- ✅ Trả lời câu hỏi thông minh
- ✅ Tiết kiệm thời gian nghiên cứu
- ✅ 100% MIỄN PHÍ với Groq API!

**Hoàn hảo cho:**
- 📚 Sinh viên làm đồ án
- 🔬 Nghiên cứu khoa học
- 📊 Phân tích dữ liệu
- 📄 Tóm tắt tài liệu

---

## 📖 Tài Liệu Liên Quan

- **START_HERE.md** - Hướng dẫn tổng quan
- **GROQ_GUIDE.md** - Chi tiết về Groq API
- **README.md** - Tài liệu đầy đủ

---

**Chúc bạn sử dụng hiệu quả!** 🎉

**Nhóm 6 - Công nghệ số nâng cao** | © 2025
