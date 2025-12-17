"""
PDF Processor Module
Xử lý và trích xuất text từ file PDF
"""

import PyPDF2
from io import BytesIO


class PDFProcessor:
    """Class xử lý file PDF"""
    
    def __init__(self):
        self.max_pages = 20  # Giới hạn số trang để xử lý
        self.max_chars = 50000  # Giới hạn số ký tự
    
    def extract_text(self, pdf_file) -> str:
        """
        Trích xuất text từ file PDF
        
        Args:
            pdf_file: File PDF đã upload
            
        Returns:
            str: Text đã trích xuất
        """
        try:
            # Đọc file PDF
            pdf_bytes = BytesIO(pdf_file.read())
            pdf_reader = PyPDF2.PdfReader(pdf_bytes)
            
            # Trích xuất text từ các trang
            text = ""
            num_pages = min(len(pdf_reader.pages), self.max_pages)
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
            
            # Giới hạn độ dài text
            if len(text) > self.max_chars:
                text = text[:self.max_chars]
            
            # Làm sạch text
            text = self._clean_text(text)
            
            return text
            
        except Exception as e:
            raise Exception(f"Lỗi khi đọc file PDF: {str(e)}")
    
    def _clean_text(self, text: str) -> str:
        """
        Làm sạch text
        
        Args:
            text: Text gốc
            
        Returns:
            str: Text đã làm sạch
        """
        # Xóa các ký tự đặc biệt
        text = text.replace('\x00', '')
        
        # Xóa khoảng trắng thừa
        text = ' '.join(text.split())
        
        return text
    
    def get_metadata(self, pdf_file) -> dict:
        """
        Lấy metadata của file PDF
        
        Args:
            pdf_file: File PDF
            
        Returns:
            dict: Metadata
        """
        try:
            pdf_bytes = BytesIO(pdf_file.read())
            pdf_reader = PyPDF2.PdfReader(pdf_bytes)
            
            metadata = {
                'num_pages': len(pdf_reader.pages),
                'author': pdf_reader.metadata.get('/Author', 'Unknown'),
                'title': pdf_reader.metadata.get('/Title', 'Unknown'),
                'subject': pdf_reader.metadata.get('/Subject', 'Unknown'),
            }
            
            return metadata
            
        except Exception as e:
            return {
                'num_pages': 0,
                'author': 'Unknown',
                'title': 'Unknown',
                'subject': 'Unknown',
                'error': str(e)
            }
