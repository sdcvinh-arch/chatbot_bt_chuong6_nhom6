# 💬 Hướng Dẫn Sử Dụng ChatGPT API

## 🎯 Tại Sao Dùng ChatGPT?

- ✅ **Phổ biến nhất**: ChatGPT là model AI nổi tiếng nhất
- ✅ **Giá rẻ**: GPT-4o-mini chỉ $0.15/$0.60 per 1M tokens
- ✅ **Nhanh**: Response time ~2-5 giây
- ✅ **Chính xác cao**: 95%+ accuracy
- ✅ **Dễ mua**: Có thể mua credit dễ dàng

## 🔑 Lấy OpenAI API Key

### Bước 1: Đăng Ký/Đăng Nhập

1. Truy cập: **https://platform.openai.com/**
2. Click **"Sign Up"** hoặc **"Log In"**
3. Đăng ký bằng:
   - Email
   - Google Account
   - Microsoft Account

### Bước 2: Nạp Tiền (Bắt Buộc)

⚠️ **OpenAI không cho free credit**, bạn phải nạp tiền trước!

1. Vào **Settings** → **Billing**
2. Click **"Add payment method"**
3. Thêm thẻ tín dụng/debit
4. Nạp tối thiểu **$5** (khuyến nghị $10-20)

**Lưu ý**: 
- Chấp nhận Visa, Mastercard, AmEx
- Có thể dùng thẻ ảo (VCB, MB, TP Bank...)
- $10 = phân tích được ~500-1000 bài báo!

### Bước 3: Tạo API Key

1. Vào **API keys** (menu bên trái)
2. Click **"+ Create new secret key"**
3. Đặt tên: `Scientific Paper Analyzer`
4. Permissions: `All` hoặc chỉ `Write`
5. Click **"Create secret key"**
6. **COPY KEY NGAY** (dạng `sk-proj-xxxxx...` hoặc `sk-xxxxx...`)
7. ⚠️ Lưu lại, không thể xem lại!

## 📝 Cấu Hình Trong Project

### Cách 1: Dùng File .env (Khuyến nghị)

1. Mở file `.env` (hoặc tạo từ `.env.example`)
2. Thêm dòng:
```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
```
3. Save file
4. Restart ứng dụng

### Cách 2: Nhập Trong Ứng Dụng

1. Chạy app: `streamlit run app.py`
2. Mở Sidebar (click mũi tên `>`)
3. Tìm ô **"OpenAI API Key (ChatGPT)"**
4. Paste API key
5. Nhấn Enter
6. ✅ Xong!

## 🎮 Sử Dụng

1. Upload file PDF
2. Click nút **"💬 Xử Lý Với ChatGPT"**
3. Chờ 5-10 giây
4. Xem kết quả!

## 💰 Chi Phí

### Giá API (Tháng 12/2025)

| Model | Input | Output | Khuyến Nghị |
|-------|--------|--------|-------------|
| **gpt-4o-mini** | $0.15/1M tokens | $0.60/1M tokens | ⭐ Tốt nhất cho SV |
| gpt-4o | $2.50/1M tokens | $10.00/1M tokens | Chính xác nhất |
| gpt-3.5-turbo | $0.50/1M tokens | $1.50/1M tokens | Cũ hơn |

### Ước Tính Chi Phí

**Với gpt-4o-mini** (khuyến nghị):
- 1 bài báo (5 trang): ~$0.002-0.005 (~50-125đ)
- 100 bài báo: ~$0.30 (~7,500đ)
- 500 bài báo: ~$1.50 (~37,500đ)

**➡️ Nạp $10 = đủ xài cả năm học!**

### So Sánh Chi Phí

| Phương Pháp | 100 Bài | 500 Bài |
|-------------|---------|---------|
| ChatGPT (gpt-4o-mini) | ~$0.30 | ~$1.50 |
| Claude (Sonnet 4) | ~$0.50 | ~$2.50 |
| BERT | $0 | $0 |

## 🔧 Chọn Model

Trong file `utils/chatgpt_analyzer.py`, tìm dòng:

```python
self.model = "gpt-4o-mini"  # RẺ NHẤT, VẪN RẤT TỐT ⭐
```

Bạn có thể đổi thành:

```python
# Rẻ nhất, tốt cho sinh viên
self.model = "gpt-4o-mini"  # $0.15/$0.60 per 1M tokens

# Chính xác nhất, đắt hơn
self.model = "gpt-4o"       # $2.50/$10.00 per 1M tokens

# Model cũ hơn
self.model = "gpt-3.5-turbo"  # $0.50/$1.50 per 1M tokens
```

## 📊 So Sánh ChatGPT vs Claude vs BERT

| Tiêu Chí | ChatGPT | Claude | BERT |
|----------|---------|--------|------|
| **Giá** | $0.30/100 bài | $0.50/100 bài | $0 |
| **Free Credit** | ❌ Không | ✅ $5 | ✅ Miễn phí |
| **Độ chính xác** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Tốc độ** | ⚡⚡ Nhanh | ⚡ Trung bình | ⚡⚡⚡ Rất nhanh |
| **Phổ biến** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Dễ mua** | ✅ Rất dễ | ⚠️ Khó hơn | N/A |

## 🎓 Khuyến Nghị Cho Sinh Viên

### Phương Án 1: Chỉ BERT (Miễn Phí 100%)
```
✅ Hoàn toàn miễn phí
✅ Đủ tốt cho đồ án
✅ Không cần thẻ tín dụng
```

### Phương Án 2: BERT + ChatGPT (Khuyến Nghị)
```
✅ Dùng BERT cho phần lớn
✅ Dùng ChatGPT cho demo/so sánh
✅ Chi phí: ~$5-10 (đủ cả năm)
```

### Phương Án 3: ChatGPT + Claude (Chuyên Nghiệp)
```
✅ So sánh 2 model GPT
✅ Kết quả tốt nhất
✅ Chi phí: ~$15-20
```

## 🔐 Bảo Mật

### ✅ NÊN:
- Lưu key trong `.env`
- Không push `.env` lên GitHub
- Không share key công khai
- Set spending limits trong OpenAI dashboard

### ❌ KHÔNG NÊN:
- Hardcode key trong code
- Share key với người khác
- Commit key lên Git
- Để key trong public repo

## 🆘 Xử Lý Lỗi

### Lỗi: "Invalid API key"
```python
AuthenticationError: Invalid API key provided
```
**Giải pháp:**
- Kiểm tra key có đúng không
- Key phải bắt đầu bằng `sk-` hoặc `sk-proj-`
- Không có khoảng trắng thừa
- Tạo key mới

### Lỗi: "Insufficient quota"
```python
RateLimitError: You exceeded your current quota
```
**Giải pháp:**
- Nạp thêm tiền vào account
- Kiểm tra billing trong Settings

### Lỗi: "Rate limit"
```python
RateLimitError: Rate limit reached
```
**Giải pháp:**
- Chờ 1 phút rồi thử lại
- Nâng cấp tier (nếu cần)

## 💡 Tips Tiết Kiệm

1. **Dùng gpt-4o-mini**: Rẻ nhất, vẫn rất tốt
2. **Batch processing**: Xử lý nhiều bài cùng lúc
3. **Cache results**: Lưu kết quả để không gọi lại
4. **Set limits**: Giới hạn chi tiêu trong dashboard
5. **Monitor usage**: Theo dõi usage trong OpenAI dashboard

## 📱 Mua API Key Ở Đâu?

### Cách 1: Mua Trực Tiếp (Khuyến Nghị)
- Website: https://platform.openai.com/
- Dùng thẻ Visa/Mastercard
- Nạp qua ví điện tử có thẻ ảo

### Cách 2: Mua Từ Đại Lý (Không Khuyến Nghị)
⚠️ **Cẩn thận lừa đảo!**
- Giá thường đắt hơn
- Có thể bị khóa key
- Không được support chính thức

### Cách 3: Chia Sẻ Trong Nhóm
- 1 người mua, cả nhóm dùng
- Chia tiền công bằng
- Set spending limit để kiểm soát

## 🎯 Kết Luận

**ChatGPT là lựa chọn TỐT NHẤT cho sinh viên vì:**
1. ✅ Giá rẻ ($0.30/100 bài với gpt-4o-mini)
2. ✅ Chính xác cao (95%+)
3. ✅ Dễ mua và sử dụng
4. ✅ Phổ biến, dễ support
5. ✅ Nhiều model để chọn

**Nạp $10 = đủ xài cả năm học!** 💰

---

**Có câu hỏi?** Inbox cho tôi nhé! 😊

**Nhóm 6 - Công nghệ số nâng cao** | © 2025
