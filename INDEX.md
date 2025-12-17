# 📑 Danh Mục Dự Án - Scientific Paper Analyzer

## 📚 Tài Liệu Chính

| File | Mô Tả | Đối Tượng |
|------|-------|-----------|
| [README.md](README.md) | Tài liệu chính, hướng dẫn đầy đủ | Tất cả |
| [QUICK_START.md](QUICK_START.md) | Hướng dẫn khởi động nhanh 5 phút | Người dùng mới |
| [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) | Tổng quan kiến trúc và thiết kế | Developers |
| [README_GITHUB.md](README_GITHUB.md) | Hướng dẫn đưa lên GitHub | Developers |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Hướng dẫn đóng góp code | Contributors |
| [CHANGELOG.md](CHANGELOG.md) | Lịch sử phát triển | Tất cả |
| [LICENSE](LICENSE) | Giấy phép MIT | Tất cả |

## 💻 Source Code

### Core Application
| File | Mô Tả | Lines | Chức Năng |
|------|-------|-------|-----------|
| [app.py](app.py) | Ứng dụng Streamlit chính | ~350 | UI, workflow, state management |

### Utilities Package (utils/)
| File | Mô Tả | Lines | Chức Năng |
|------|-------|-------|-----------|
| [utils/__init__.py](utils/__init__.py) | Package init | ~5 | Package marker |
| [utils/pdf_processor.py](utils/pdf_processor.py) | Xử lý PDF | ~100 | Extract text, metadata |
| [utils/gpt_analyzer.py](utils/gpt_analyzer.py) | Phân tích GPT | ~150 | Claude API integration |
| [utils/bert_analyzer.py](utils/bert_analyzer.py) | Phân tích BERT | ~250 | BERT model, NLP |
| [utils/export_handler.py](utils/export_handler.py) | Export kết quả | ~150 | JSON, CSV, MD, HTML |

### Tests Package (tests/)
| File | Mô Tả | Lines | Coverage |
|------|-------|-------|----------|
| [tests/__init__.py](tests/__init__.py) | Package init | ~5 | - |
| [tests/test_pdf_processor.py](tests/test_pdf_processor.py) | Test PDF processor | ~50 | ~60% |
| [tests/test_bert_analyzer.py](tests/test_bert_analyzer.py) | Test BERT analyzer | ~70 | ~50% |

## 🔧 Configuration Files

| File | Mô Tả | Mục Đích |
|------|-------|----------|
| [requirements.txt](requirements.txt) | Python dependencies | Cài đặt packages |
| [setup.py](setup.py) | Package setup | Phân phối package |
| [.env.example](.env.example) | Environment template | Cấu hình API keys |
| [.gitignore](.gitignore) | Git ignore rules | Bảo mật và clean repo |

## 🚀 Scripts

| File | Platform | Mô Tả |
|------|----------|-------|
| [run.sh](run.sh) | Linux/macOS | Auto setup và chạy app |
| [run.bat](run.bat) | Windows | Auto setup và chạy app |

## 📊 Thống Kê Dự Án

### Code Statistics
```
Total Files:     21
Python Files:    9
Markdown Files:  7
Config Files:    4
Scripts:         2

Total Lines:     ~2,500+
Code Lines:      ~1,200
Comment Lines:   ~400
Documentation:   ~900
```

### File Size Distribution
```
Small (<100 lines):    8 files
Medium (100-300):      7 files  
Large (>300):          6 files
```

## 🎯 File Purpose Matrix

### 📖 For Reading
- **New Users**: README.md → QUICK_START.md
- **Developers**: PROJECT_OVERVIEW.md → CONTRIBUTING.md
- **Maintainers**: CHANGELOG.md → All docs

### 💻 For Coding
- **Main Logic**: app.py
- **PDF Processing**: utils/pdf_processor.py
- **AI Analysis**: utils/gpt_analyzer.py, utils/bert_analyzer.py
- **Export**: utils/export_handler.py

### 🧪 For Testing
- **Unit Tests**: tests/test_*.py
- **Manual Test**: Run app.py

### 🚀 For Deployment
- **Local**: run.sh or run.bat
- **Production**: setup.py, requirements.txt
- **Docker**: (Coming soon)

## 📂 Directory Structure

```
scientific-paper-analyzer/
│
├── 📄 Documentation (7 files)
│   ├── README.md                   ⭐ Start here
│   ├── QUICK_START.md              ⚡ 5-minute guide
│   ├── PROJECT_OVERVIEW.md         🏗️ Architecture
│   ├── README_GITHUB.md            📤 GitHub guide
│   ├── CONTRIBUTING.md             🤝 Contribute
│   ├── CHANGELOG.md                📋 History
│   └── LICENSE                     ⚖️ MIT License
│
├── 💻 Application (1 file)
│   └── app.py                      🎯 Main app
│
├── 🔧 Utils (5 files)
│   ├── __init__.py
│   ├── pdf_processor.py            📄 PDF handler
│   ├── gpt_analyzer.py             🤖 GPT analysis
│   ├── bert_analyzer.py            🧠 BERT analysis
│   └── export_handler.py           📥 Export handler
│
├── 🧪 Tests (3 files)
│   ├── __init__.py
│   ├── test_pdf_processor.py
│   └── test_bert_analyzer.py
│
├── ⚙️ Config (4 files)
│   ├── requirements.txt            📦 Dependencies
│   ├── setup.py                    🔧 Setup script
│   ├── .env.example                🔑 Env template
│   └── .gitignore                  🚫 Git ignore
│
└── 🚀 Scripts (2 files)
    ├── run.sh                      🐧 Linux/Mac
    └── run.bat                     🪟 Windows
```

## 🔍 Quick Navigation

### Want to...

**Install the app?**
→ See [QUICK_START.md](QUICK_START.md)

**Understand the code?**
→ See [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)

**Contribute code?**
→ See [CONTRIBUTING.md](CONTRIBUTING.md)

**Deploy to GitHub?**
→ See [README_GITHUB.md](README_GITHUB.md)

**Check what changed?**
→ See [CHANGELOG.md](CHANGELOG.md)

**Report a bug?**
→ Create issue on GitHub

**Ask a question?**
→ Email: nhom6@example.com

## 📝 File Templates

### For Bug Reports
```markdown
**Describe the bug**
A clear description of the bug.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g. Windows 10]
 - Python: [e.g. 3.10]
 - Version: [e.g. 1.0.0]
```

### For Feature Requests
```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want.

**Describe alternatives you've considered**
Alternative solutions or features.

**Additional context**
Any other context or screenshots.
```

## 🎓 Learning Path

### Level 1: User (1 hour)
1. Read README.md overview
2. Follow QUICK_START.md
3. Try the app with sample PDFs
4. Export results

### Level 2: Developer (4 hours)
1. Read PROJECT_OVERVIEW.md
2. Study app.py structure
3. Review utils/ modules
4. Run tests
5. Make small changes

### Level 3: Contributor (1 day)
1. Read CONTRIBUTING.md
2. Setup dev environment
3. Study code in detail
4. Write tests
5. Submit PR

### Level 4: Maintainer (1 week)
1. Understand full architecture
2. Review all documentation
3. Learn deployment process
4. Help other contributors
5. Plan new features

## 📊 Dependency Graph

```
app.py
  ├─→ streamlit
  ├─→ utils/pdf_processor.py
  │     └─→ PyPDF2
  ├─→ utils/gpt_analyzer.py
  │     └─→ anthropic
  ├─→ utils/bert_analyzer.py
  │     ├─→ transformers
  │     ├─→ torch
  │     └─→ scikit-learn
  └─→ utils/export_handler.py
        └─→ pandas
```

## 🔄 Update Checklist

When making changes:

- [ ] Update code
- [ ] Update docstrings
- [ ] Update README.md (if needed)
- [ ] Update CHANGELOG.md
- [ ] Run tests
- [ ] Update version in setup.py
- [ ] Commit with clear message
- [ ] Push to GitHub

## 🌟 Key Files to Understand First

1. **README.md** - Overall understanding
2. **app.py** - Application flow
3. **utils/gpt_analyzer.py** - AI integration
4. **utils/bert_analyzer.py** - NLP processing
5. **PROJECT_OVERVIEW.md** - Architecture

## 💡 Pro Tips

- **Before coding**: Read CONTRIBUTING.md
- **Before deploying**: Read README_GITHUB.md
- **When stuck**: Check PROJECT_OVERVIEW.md
- **For quick start**: Use run.sh/run.bat
- **For clean code**: Follow PEP 8

## 📞 Support Files

| Issue Type | File to Check | Action |
|------------|---------------|--------|
| Installation | QUICK_START.md | Follow steps |
| Bug | CONTRIBUTING.md | Report issue |
| Feature idea | CONTRIBUTING.md | Open discussion |
| Code question | PROJECT_OVERVIEW.md | Understand architecture |
| Deployment | README_GITHUB.md | Follow guide |

---

**Last Updated**: 2025-12-17
**Version**: 1.0.0
**Maintained By**: Nhóm 6 - Công nghệ số nâng cao

---

📖 **Happy Reading & Coding!** 🚀
