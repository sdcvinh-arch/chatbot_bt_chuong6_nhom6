# Hướng Dẫn Đóng Góp

Cảm ơn bạn đã quan tâm đến việc đóng góp cho Scientific Paper Analyzer! 🎉

## 🚀 Quy Trình Đóng Góp

### 1. Fork Repository

Fork repository này về tài khoản GitHub của bạn.

### 2. Clone Repository

```bash
git clone https://github.com/your-username/scientific-paper-analyzer.git
cd scientific-paper-analyzer
```

### 3. Tạo Branch Mới

```bash
git checkout -b feature/ten-tinh-nang-moi
```

Đặt tên branch theo format:
- `feature/` - Tính năng mới
- `bugfix/` - Sửa lỗi
- `docs/` - Cập nhật tài liệu
- `refactor/` - Tái cấu trúc code

### 4. Cài Đặt Development Environment

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt (Linux/Mac)
source venv/bin/activate

# Kích hoạt (Windows)
venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt

# Cài đặt development dependencies
pip install pytest black flake8 mypy
```

### 5. Viết Code

- Tuân thủ PEP 8 style guide
- Thêm docstrings cho functions và classes
- Viết type hints khi có thể
- Thêm comments cho code phức tạp

### 6. Test Code

```bash
# Chạy tests
pytest

# Check code style
black --check .
flake8 .

# Type checking
mypy .
```

### 7. Commit Changes

```bash
git add .
git commit -m "feat: Thêm tính năng X"
```

Format commit message:
- `feat:` - Tính năng mới
- `fix:` - Sửa lỗi
- `docs:` - Cập nhật tài liệu
- `style:` - Format code
- `refactor:` - Tái cấu trúc
- `test:` - Thêm tests
- `chore:` - Công việc khác

### 8. Push và Tạo Pull Request

```bash
git push origin feature/ten-tinh-nang-moi
```

Sau đó tạo Pull Request trên GitHub với:
- Tiêu đề rõ ràng
- Mô tả chi tiết về thay đổi
- Link đến issue (nếu có)
- Screenshots (nếu thay đổi UI)

## 📋 Code Style Guidelines

### Python Style

```python
# Good
def analyze_paper(text: str, filename: str) -> dict:
    """
    Phân tích bài báo khoa học.
    
    Args:
        text: Nội dung bài báo
        filename: Tên file
        
    Returns:
        dict: Kết quả phân tích
    """
    # Implementation
    pass

# Bad
def analyze(t,f):
    # No docstring
    pass
```

### File Organization

```python
# 1. Standard library imports
import os
import json

# 2. Third-party imports
import streamlit as st
from anthropic import Anthropic

# 3. Local imports
from utils.pdf_processor import PDFProcessor
```

## 🐛 Báo Cáo Lỗi

Khi báo cáo lỗi, vui lòng bao gồm:

1. **Mô tả lỗi**: Mô tả rõ ràng về lỗi
2. **Các bước tái tạo**: Cách tái tạo lỗi
3. **Hành vi mong đợi**: Kết quả bạn mong muốn
4. **Hành vi thực tế**: Kết quả thực tế
5. **Environment**: 
   - OS (Windows/Mac/Linux)
   - Python version
   - Package versions
6. **Screenshots**: Nếu có
7. **Error logs**: Copy full error traceback

### Template Issue

```markdown
## Mô Tả Lỗi
[Mô tả chi tiết lỗi]

## Các Bước Tái Tạo
1. Vào trang X
2. Click nút Y
3. ...

## Hành Vi Mong Đợi
[Kết quả mong muốn]

## Hành Vi Thực Tế
[Kết quả thực tế]

## Environment
- OS: Windows 11
- Python: 3.10.5
- Streamlit: 1.31.0

## Screenshots
[Nếu có]

## Error Logs
```
[Paste error logs here]
```
```

## 💡 Đề Xuất Tính Năng

Khi đề xuất tính năng mới:

1. **Mô tả tính năng**: Tính năng bạn muốn thêm
2. **Use case**: Tại sao tính năng này hữu ích
3. **Giải pháp đề xuất**: Cách bạn nghĩ nên implement
4. **Giải pháp thay thế**: Các cách khác (nếu có)
5. **Context bổ sung**: Thông tin thêm

## ✅ Pull Request Checklist

Trước khi submit PR, đảm bảo:

- [ ] Code tuân thủ style guide
- [ ] Đã thêm/cập nhật docstrings
- [ ] Đã thêm/cập nhật tests
- [ ] Tests pass (`pytest`)
- [ ] Code formatted (`black`)
- [ ] No linting errors (`flake8`)
- [ ] Type hints checked (`mypy`)
- [ ] Cập nhật README.md (nếu cần)
- [ ] Cập nhật CHANGELOG.md
- [ ] Commit messages rõ ràng
- [ ] PR description đầy đủ

## 🎯 Areas for Contribution

Những area cần đóng góp:

### High Priority
- [ ] Hỗ trợ nhiều ngôn ngữ
- [ ] Visualization cho kết quả
- [ ] API endpoint
- [ ] Batch processing

### Medium Priority
- [ ] Thêm unit tests
- [ ] Performance optimization
- [ ] Mobile responsive UI
- [ ] Dark mode

### Low Priority
- [ ] Thêm examples
- [ ] Video tutorials
- [ ] Blog posts
- [ ] Translations

## 📝 Documentation

Khi cập nhật docs:

- Sử dụng tiếng Việt hoặc tiếng Anh
- Thêm examples cho mỗi feature
- Cập nhật screenshots khi UI thay đổi
- Giữ README.md ngắn gọn, link đến docs chi tiết

## 🤝 Code Review Process

1. Maintainers sẽ review PR trong vòng 48h
2. Có thể request changes hoặc approve
3. Sau khi approve, PR sẽ được merge
4. Contributor sẽ được thêm vào CONTRIBUTORS.md

## 📞 Liên Hệ

Nếu có câu hỏi:
- Tạo issue trên GitHub
- Email: nhom6@example.com
- Discord: [Link]

## 🙏 Cảm Ơn

Cảm ơn bạn đã đóng góp! Mỗi contribution đều giúp project tốt hơn. ❤️

---

**Nhóm 6 - Công nghệ số nâng cao** | © 2025
