# 📤 Hướng Dẫn Đưa Dự Án Lên GitHub

## Bước 1: Tạo Repository Trên GitHub

1. Đăng nhập vào [GitHub](https://github.com)
2. Click nút "+" ở góc trên bên phải → "New repository"
3. Điền thông tin:
   - **Repository name**: `scientific-paper-analyzer`
   - **Description**: `Ứng dụng phân tích bài báo khoa học sử dụng GPT và BERT`
   - **Visibility**: Public hoặc Private
   - **Không** chọn "Initialize with README" (vì đã có sẵn)
4. Click "Create repository"

## Bước 2: Chuẩn Bị Dự Án Local

### 2.1. Di chuyển vào thư mục dự án

```bash
cd scientific-paper-analyzer
```

### 2.2. Kiểm tra cấu trúc

```bash
ls -la
```

Bạn sẽ thấy:
```
app.py
requirements.txt
README.md
LICENSE
.gitignore
setup.py
run.sh
run.bat
.env.example
CONTRIBUTING.md
CHANGELOG.md
QUICK_START.md
utils/
tests/
```

### 2.3. Đảm bảo file .env không được commit

File `.gitignore` đã bao gồm `.env`, nhưng hãy kiểm tra:

```bash
cat .gitignore | grep .env
```

Nếu không thấy, thêm vào:
```bash
echo ".env" >> .gitignore
```

## Bước 3: Khởi Tạo Git Repository

```bash
# Khởi tạo git
git init

# Thêm tất cả files
git add .

# Commit đầu tiên
git commit -m "Initial commit: Scientific Paper Analyzer v1.0.0"
```

## Bước 4: Kết Nối Với GitHub

Thay `yourusername` bằng username GitHub của bạn:

```bash
# Thêm remote repository
git remote add origin https://github.com/yourusername/scientific-paper-analyzer.git

# Kiểm tra remote
git remote -v
```

## Bước 5: Push Code Lên GitHub

### 5.1. Push lần đầu

```bash
# Push code lên branch main
git branch -M main
git push -u origin main
```

### 5.2. Nhập credentials

Nếu được yêu cầu nhập username và password:
- **Username**: GitHub username của bạn
- **Password**: Sử dụng **Personal Access Token** (không phải password)

#### Tạo Personal Access Token:

1. Vào GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Đặt tên: `scientific-paper-analyzer`
4. Chọn scopes: `repo` (full control of private repositories)
5. Click "Generate token"
6. **Copy token và lưu lại** (chỉ hiển thị 1 lần)
7. Sử dụng token này làm password khi push

## Bước 6: Verify Trên GitHub

1. Mở trình duyệt và vào: `https://github.com/yourusername/scientific-paper-analyzer`
2. Kiểm tra xem tất cả files đã được upload chưa
3. README.md sẽ tự động hiển thị ở trang chính

## Bước 7: Tùy Chỉnh Repository (Optional)

### 7.1. Thêm Topics

1. Vào repository trên GitHub
2. Click "Add topics"
3. Thêm: `python`, `streamlit`, `bert`, `gpt`, `nlp`, `machine-learning`, `scientific-papers`

### 7.2. Thêm Description

Đã có sẵn khi tạo repo, có thể edit thêm

### 7.3. Tạo Releases

1. Vào tab "Releases"
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `Scientific Paper Analyzer v1.0.0 - Initial Release`
5. Description: Copy từ CHANGELOG.md
6. Click "Publish release"

### 7.4. Thêm GitHub Actions (CI/CD)

Tạo file `.github/workflows/python-app.yml`:

```yaml
name: Python Application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest black flake8
    
    - name: Lint with flake8
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    
    - name: Format with black
      run: |
        black --check .
    
    - name: Test with pytest
      run: |
        pytest
```

Commit và push:
```bash
git add .github/
git commit -m "Add GitHub Actions workflow"
git push
```

## Bước 8: Cập Nhật Code Sau Này

### Workflow thông thường:

```bash
# 1. Kiểm tra status
git status

# 2. Thêm files đã thay đổi
git add .

# 3. Commit với message rõ ràng
git commit -m "feat: Thêm tính năng X"

# 4. Push lên GitHub
git push
```

### Tạo branch cho feature mới:

```bash
# 1. Tạo và chuyển sang branch mới
git checkout -b feature/new-feature

# 2. Code và commit
git add .
git commit -m "feat: Implement new feature"

# 3. Push branch
git push -u origin feature/new-feature

# 4. Tạo Pull Request trên GitHub
# 5. Merge vào main sau khi review
```

## Bước 9: Thêm Badges Vào README

Thêm vào đầu README.md:

```markdown
![GitHub stars](https://img.shields.io/github/stars/yourusername/scientific-paper-analyzer?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/scientific-paper-analyzer?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/scientific-paper-analyzer)
![GitHub license](https://img.shields.io/github/license/yourusername/scientific-paper-analyzer)
![Python version](https://img.shields.io/badge/python-3.9%2B-blue)
```

## Bước 10: Chia Sẻ Repository

Repository URL của bạn:
```
https://github.com/yourusername/scientific-paper-analyzer
```

Chia sẻ trên:
- LinkedIn
- Twitter
- Reddit (r/Python, r/MachineLearning)
- Dev.to
- Medium

## 📋 Checklist

Trước khi public repository:

- [ ] File .env không được commit
- [ ] Đã thêm .gitignore đầy đủ
- [ ] README.md đầy đủ và rõ ràng
- [ ] LICENSE đã có
- [ ] CONTRIBUTING.md đã có
- [ ] Code đã được test
- [ ] Không có API keys hoặc secrets trong code
- [ ] Links trong README đã được cập nhật
- [ ] Version number đúng

## 🚨 Lưu Ý Quan Trọng

### ⚠️ Security

- **KHÔNG BAO GIỜ** commit file `.env` chứa API keys
- **KHÔNG** hardcode API keys trong code
- Sử dụng environment variables
- Review code trước khi push

### 📦 Best Practices

- Commit messages rõ ràng và có ý nghĩa
- Tạo branch cho mỗi feature mới
- Sử dụng Pull Requests cho review
- Viết tests cho code mới
- Cập nhật documentation
- Tag releases với semantic versioning

## 🆘 Xử Lý Sự Cố

### Lỗi: Repository already exists

```bash
# Xóa remote cũ
git remote remove origin

# Thêm remote mới
git remote add origin https://github.com/yourusername/scientific-paper-analyzer.git
```

### Lỗi: Failed to push

```bash
# Pull code mới nhất trước
git pull origin main --rebase

# Sau đó push
git push
```

### Đã commit file .env nhầm

```bash
# Xóa file khỏi git (giữ lại local)
git rm --cached .env

# Commit
git commit -m "Remove .env from git"

# Đảm bảo .env trong .gitignore
echo ".env" >> .gitignore

# Push
git push
```

## 🎉 Hoàn Thành!

Repository của bạn đã sẵn sàng trên GitHub! 🚀

Next steps:
- Thêm tài liệu wiki
- Setup GitHub Pages cho documentation
- Tạo project board để quản lý tasks
- Enable discussions cho community

---

**Happy Coding!** 💻✨

**Phát triển bởi: Nhóm 6 - Công nghệ số nâng cao** | © 2025
