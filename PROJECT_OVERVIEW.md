# 📊 Tổng Quan Dự Án - Scientific Paper Analyzer

## 🎯 Mục Tiêu

Xây dựng một ứng dụng web Python chuyên nghiệp để phân tích bài báo khoa học tự động, giúp nhà nghiên cứu tiết kiệm thời gian trong việc đọc và tóm tắt tài liệu.

## 🏗️ Kiến Trúc Hệ Thống

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                       │
│                  (Streamlit Web App)                    │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                    Main Application                     │
│                      (app.py)                           │
└─────────────────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
    ┌──────────────────────┐  ┌──────────────────────┐
    │   PDF Processor      │  │   Export Handler     │
    │  (pdf_processor.py)  │  │ (export_handler.py)  │
    └──────────────────────┘  └──────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
┌──────────────┐  ┌──────────────┐
│ GPT Analyzer │  │ BERT Analyzer│
│(gpt_analyzer)│  │(bert_analyzer)│
└──────────────┘  └──────────────┘
        │               │
        ▼               ▼
┌──────────────┐  ┌──────────────┐
│ Claude API   │  │ BERT Model   │
│ (Anthropic)  │  │(Transformers)│
└──────────────┘  └──────────────┘
```

## 📦 Cấu Trúc Thư Mục

```
scientific-paper-analyzer/
│
├── 📄 app.py                          # Ứng dụng chính
├── 📄 requirements.txt                # Dependencies
├── 📄 setup.py                        # Package setup
├── 📄 .env.example                    # Template environment
├── 📄 .gitignore                      # Git ignore rules
│
├── 📄 README.md                       # Tài liệu chính
├── 📄 QUICK_START.md                  # Hướng dẫn nhanh
├── 📄 README_GITHUB.md                # Hướng dẫn GitHub
├── 📄 CONTRIBUTING.md                 # Hướng dẫn đóng góp
├── 📄 CHANGELOG.md                    # Lịch sử thay đổi
├── 📄 LICENSE                         # Giấy phép MIT
├── 📄 PROJECT_OVERVIEW.md             # File này
│
├── 🔧 run.sh                          # Script Linux/Mac
├── 🔧 run.bat                         # Script Windows
│
├── 📁 utils/                          # Thư viện tiện ích
│   ├── __init__.py
│   ├── pdf_processor.py              # Xử lý PDF
│   ├── gpt_analyzer.py               # Phân tích GPT
│   ├── bert_analyzer.py              # Phân tích BERT
│   └── export_handler.py             # Export kết quả
│
└── 📁 tests/                          # Unit tests
    ├── __init__.py
    ├── test_pdf_processor.py
    └── test_bert_analyzer.py
```

## 🔧 Công Nghệ Sử Dụng

### Backend & Core
- **Python 3.9+**: Ngôn ngữ chính
- **Streamlit 1.31.0**: Web framework
- **PyPDF2 3.0.1**: Xử lý PDF

### AI/ML Models
- **Anthropic Claude (Sonnet 4)**: GPT analysis
- **BERT (base-uncased)**: Transformer model
- **Transformers 4.36.2**: Hugging Face library
- **PyTorch 2.1.2**: Deep learning framework

### Data Processing
- **Scikit-learn 1.3.2**: ML utilities (TF-IDF)
- **Pandas 2.1.4**: Data manipulation
- **NumPy 1.26.3**: Numerical computing

### Utilities
- **python-dotenv 1.0.0**: Environment variables
- **Plotly 5.18.0**: Visualization (future use)

## 🎨 Giao Diện Người Dùng

### Design System
- **Color Scheme**: Blue-Purple gradient
- **Layout**: Wide, responsive
- **Components**: Cards, buttons, progress bars
- **Style**: Modern, clean, professional

### Pages/Sections
1. **Header**: Branding và title
2. **Sidebar**: Settings và API key input
3. **Upload Section**: File uploader
4. **Processing Section**: GPT/BERT buttons
5. **Results Section**: Analysis display
6. **Export Section**: Download buttons

## 🔄 Luồng Xử Lý

### 1. Upload Flow
```
User selects PDF files
    → Validate file count (max 5)
    → Validate file type (.pdf)
    → Store in session state
    → Display file list
```

### 2. GPT Analysis Flow
```
Check API key
    → Extract text from PDF
    → Create prompt for Claude
    → Call Anthropic API
    → Parse JSON response
    → Store results
    → Display to user
```

### 3. BERT Analysis Flow
```
Load BERT model
    → Extract text from PDF
    → Preprocess text
    → Extract keywords (TF-IDF)
    → Generate summary (extractive)
    → Analyze methodology
    → Store results
    → Display to user
```

### 4. Export Flow
```
User clicks export
    → Format data (JSON/CSV/MD/HTML)
    → Create download button
    → User downloads file
```

## 📊 Data Models

### Paper Analysis Result
```python
{
    "filename": str,              # Tên file PDF
    "title": str,                 # Tiêu đề bài báo
    "summary": str,               # Tóm tắt (4-5 câu)
    "keywords": List[str],        # 8 từ khóa
    "main_findings": str,         # Phát hiện chính
    "methodology": str            # Phương pháp nghiên cứu
}
```

### Analysis Results
```python
{
    "type": str,                  # "GPT" hoặc "BERT"
    "timestamp": str,             # ISO format
    "papers": List[PaperResult]   # Danh sách kết quả
}
```

## 🧪 Testing Strategy

### Unit Tests
- `test_pdf_processor.py`: Test PDF processing
- `test_bert_analyzer.py`: Test BERT analysis
- Future: `test_gpt_analyzer.py`, `test_export_handler.py`

### Integration Tests
- Full pipeline testing (coming soon)
- API integration testing
- End-to-end user flows

### Test Coverage Goals
- **Current**: ~40%
- **Target**: 80%+

## 🔐 Security Considerations

### API Key Management
- Store in `.env` file (not committed)
- Or input via UI (not stored)
- Environment variable support
- No hardcoding in code

### Data Privacy
- No data uploaded to external servers (except API calls)
- No logging of sensitive data
- Local processing only
- User owns all data

### Input Validation
- File type checking (.pdf only)
- File size limits (< 50MB)
- File count limits (max 5)
- Text length limits (50k chars)

## ⚡ Performance

### Benchmarks
| Operation | Time | Notes |
|-----------|------|-------|
| PDF extraction | 1-3s | Per 20 pages |
| GPT analysis | 10-15s | Per paper |
| BERT analysis | 5-8s | Per paper |
| Export JSON | < 1s | All formats |

### Optimization
- Lazy loading of BERT model
- Batch processing support
- Progress indicators
- Caching (future)

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud (Free)
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Deploy with one click
4. Free tier: 1GB RAM

### Docker (Coming soon)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
```

### Heroku/Railway/Render
- All support Python apps
- Easy deployment
- Free tiers available

## 📈 Roadmap

### Version 1.0 (Current) ✅
- [x] Basic PDF processing
- [x] GPT analysis
- [x] BERT analysis
- [x] Export functionality
- [x] Web UI

### Version 1.1 (Next)
- [ ] Multi-language support
- [ ] Visualization
- [ ] Batch processing
- [ ] API endpoints
- [ ] Docker support

### Version 2.0 (Future)
- [ ] Compare papers
- [ ] Citation network
- [ ] Mobile app
- [ ] Collaboration features
- [ ] Database integration

## 🎓 Learning Resources

### For Users
- README.md - Comprehensive guide
- QUICK_START.md - Fast setup
- YouTube tutorials (coming)

### For Developers
- CONTRIBUTING.md - How to contribute
- Code comments - Inline documentation
- Docstrings - Function docs
- Type hints - Better IDE support

### For DevOps
- README_GITHUB.md - GitHub setup
- setup.py - Package configuration
- requirements.txt - Dependencies

## 📞 Support & Community

### Get Help
- GitHub Issues - Bug reports
- GitHub Discussions - Questions
- Email - nhom6@example.com

### Contribute
- Fork and PR - Code contributions
- Issues - Feature requests
- Documentation - Improve docs
- Translations - Add languages

## 📊 Metrics & Analytics

### Target Metrics
- User satisfaction: 90%+
- Analysis accuracy: 85%+
- Processing speed: < 20s/paper
- Uptime: 99.9%

### Success Criteria
- 1000+ GitHub stars
- 100+ contributors
- 10000+ users
- Featured on Product Hunt

## 🏆 Competitive Advantages

### vs Traditional Methods
- **10x faster** than manual reading
- **Consistent** analysis quality
- **Scalable** to many papers
- **Affordable** (mostly free)

### vs Other Tools
- **Open source** (free)
- **Privacy-first** (local processing)
- **Modern UI** (better UX)
- **Flexible** (multiple models)

## 💡 Innovation Points

1. **Dual Model Approach**: Combine GPT and BERT
2. **Local + Cloud**: Balance privacy and power
3. **No Login Required**: Frictionless usage
4. **Export Flexibility**: Multiple formats
5. **Developer Friendly**: Easy to extend

## 🎯 Target Users

### Primary
- Academic researchers
- Graduate students
- University professors
- Research assistants

### Secondary
- Journal editors
- Literature reviewers
- Research analysts
- Science writers

## 💰 Business Model (Future)

### Free Tier
- 5 papers/day
- BERT analysis
- Basic export

### Pro Tier ($9.99/month)
- Unlimited papers
- GPT analysis
- Advanced export
- API access

### Enterprise ($99/month)
- Custom deployment
- Dedicated support
- Batch processing
- Custom models

## 🌟 Vision

**"Democratize scientific paper analysis through AI, making research accessible to everyone."**

### Long-term Goals
- Process 1M+ papers
- Support 50+ languages
- Integrate 10+ AI models
- Build researcher community
- Impact scientific productivity

---

**Project Status**: ✅ Production Ready (v1.0.0)

**Last Updated**: 2025-12-17

**Maintained By**: Nhóm 6 - Công nghệ số nâng cao

**License**: MIT

---

💙 Built with passion for science and technology
