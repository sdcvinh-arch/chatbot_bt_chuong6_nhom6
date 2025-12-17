#!/bin/bash

# Script để chạy Scientific Paper Analyzer
# Tác giả: BERT Research Team

echo "🧠 Scientific Paper Analyzer"
echo "============================"
echo ""

# Kiểm tra Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 chưa được cài đặt!"
    echo "Vui lòng cài đặt Python 3.9 hoặc cao hơn"
    exit 1
fi

echo "✅ Python version: $(python3 --version)"
echo ""

# Kiểm tra virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Tạo virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment đã được tạo"
    echo ""
fi

# Kích hoạt virtual environment
echo "🔄 Kích hoạt virtual environment..."
source venv/bin/activate

# Kiểm tra requirements
if [ ! -f "venv/installed" ]; then
    echo "📥 Cài đặt dependencies..."
    pip install -r requirements.txt
    touch venv/installed
    echo "✅ Dependencies đã được cài đặt"
    echo ""
fi

# Kiểm tra .env file
if [ ! -f ".env" ]; then
    echo "⚠️  File .env chưa tồn tại"
    echo "📝 Tạo file .env từ .env.example..."
    cp .env.example .env
    echo "✅ File .env đã được tạo"
    echo "🔑 Vui lòng thêm ANTHROPIC_API_KEY vào file .env"
    echo ""
fi

# Chạy ứng dụng
echo "🚀 Khởi động ứng dụng..."
echo ""
streamlit run app.py
