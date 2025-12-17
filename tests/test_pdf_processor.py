"""
Unit tests for PDF Processor
"""

import pytest
from utils.pdf_processor import PDFProcessor


class TestPDFProcessor:
    """Test cases for PDFProcessor class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.processor = PDFProcessor()
    
    def test_initialization(self):
        """Test processor initialization"""
        assert self.processor.max_pages == 20
        assert self.processor.max_chars == 50000
    
    def test_clean_text(self):
        """Test text cleaning"""
        text = "Hello   World  \x00  Test"
        cleaned = self.processor._clean_text(text)
        assert cleaned == "Hello World Test"
    
    def test_clean_text_empty(self):
        """Test cleaning empty text"""
        text = ""
        cleaned = self.processor._clean_text(text)
        assert cleaned == ""
    
    def test_clean_text_whitespace(self):
        """Test cleaning text with only whitespace"""
        text = "   \n\n  \t  "
        cleaned = self.processor._clean_text(text)
        assert cleaned == ""


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
