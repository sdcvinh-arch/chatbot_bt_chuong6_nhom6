@echo off
REM Script để chạy Scientific Paper Analyzer trên Windows
REM Tác giả: BERT Research Team

echo ============================
echo 🧠 Scientific Paper Analyzer
echo ============================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python chưa được cài đặt!
    echo Vui lòng cài đặt Python 3.9 hoặc cao hơn
    pause
    exit /b 1
)

echo ✅ Python đã được cài đặt
echo.

REM Kiểm tra virtual environment
if not exist "venv\" (
    echo 📦 Tạo virtual environment...
    python -m venv venv
    echo ✅ Virtual environment đã được tạo
    echo.
)

REM Kích hoạt virtual environment
echo 🔄 Kích hoạt virtual environment...
call venv\Scripts\activate.bat

REM Kiểm tra requirements
if not exist "venv\installed" (
    echo 📥 Cài đặt dependencies...
    pip install -r requirements.txt
    echo. > venv\installed
    echo ✅ Dependencies đã được cài đặt
    echo.
)

REM Kiểm tra .env file
if not exist ".env" (
    echo ⚠️  File .env chưa tồn tại
    echo 📝 Tạo file .env từ .env.example...
    copy .env.example .env
    echo ✅ File .env đã được tạo
    echo 🔑 Vui lòng thêm ANTHROPIC_API_KEY vào file .env
    echo.
)

REM Chạy ứng dụng
echo 🚀 Khởi động ứng dụng...
echo.
streamlit run app.py

pause
