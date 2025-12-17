"""
Unit tests for BERT Analyzer
"""

import pytest
from utils.bert_analyzer import BERTAnalyzer


class TestBERTAnalyzer:
    """Test cases for BERTAnalyzer class"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.analyzer = BERTAnalyzer()
    
    def test_initialization(self):
        """Test analyzer initialization"""
        assert self.analyzer.model_name == "bert-base-uncased"
    
    def test_preprocess_text(self):
        """Test text preprocessing"""
        text = "Hello! @#$ World... Test???"
        cleaned = self.analyzer._preprocess_text(text)
        assert "@#$" not in cleaned
        assert "Hello" in cleaned
    
    def test_extract_title(self):
        """Test title extraction"""
        text = "This is a test paper about AI. It discusses various topics."
        title = self.analyzer._extract_title(text)
        assert len(title) > 0
        assert title.startswith("This is a test paper")
    
    def test_extract_keywords(self):
        """Test keyword extraction"""
        text = """
        Machine learning is a field of artificial intelligence.
        Machine learning algorithms learn from data.
        Neural networks are machine learning models.
        """
        keywords = self.analyzer._extract_keywords(text)
        assert len(keywords) > 0
        assert "machine" in keywords or "learning" in keywords
    
    def test_generate_summary(self):
        """Test summary generation"""
        text = """
        First sentence about the topic.
        Second sentence with more details.
        Third sentence explaining methodology.
        Fourth sentence showing results.
        Fifth sentence with conclusions.
        """
        summary = self.analyzer._generate_summary(text)
        assert len(summary) > 0
        assert "First sentence" in summary


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
