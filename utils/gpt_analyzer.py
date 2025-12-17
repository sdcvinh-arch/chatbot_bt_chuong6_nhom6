"""
GPT Analyzer Module
Sử dụng Anthropic Claude API để phân tích bài báo
"""

import os
import json
from anthropic import Anthropic


class GPTAnalyzer:
    """Class phân tích bài báo với GPT (Claude)"""
    
    def __init__(self):
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY không được thiết lập")
        
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"
        self.max_tokens = 2000
    
    def analyze(self, text: str, filename: str) -> dict:
        """
        Phân tích bài báo khoa học
        
        Args:
            text: Nội dung bài báo
            filename: Tên file
            
        Returns:
            dict: Kết quả phân tích
        """
        try:
            # Tạo prompt
            prompt = self._create_prompt(text)
            
            # Gọi API Claude
            message = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            # Xử lý response
            response_text = message.content[0].text
            
            # Parse JSON response
            result = self._parse_response(response_text)
            result['filename'] = filename
            
            return result
            
        except Exception as e:
            # Trả về kết quả mặc định nếu có lỗi
            return {
                'filename': filename,
                'title': 'Không thể phân tích',
                'summary': f'Lỗi: {str(e)}',
                'keywords': [],
                'main_findings': 'N/A',
                'methodology': 'N/A'
            }
    
    def _create_prompt(self, text: str) -> str:
        """
        Tạo prompt cho Claude
        
        Args:
            text: Nội dung bài báo
            
        Returns:
            str: Prompt
        """
        prompt = f"""Bạn là chuyên gia phân tích bài báo khoa học với 10 năm kinh nghiệm.

Hãy phân tích bài báo khoa học sau đây và trả về kết quả dưới dạng JSON với format chính xác như sau:

{{
  "title": "Tiêu đề đầy đủ của bài báo",
  "summary": "Tóm tắt chi tiết 4-5 câu về mục đích, phương pháp, kết quả và ý nghĩa của nghiên cứu",
  "keywords": ["từ khóa 1", "từ khóa 2", "từ khóa 3", "từ khóa 4", "từ khóa 5", "từ khóa 6", "từ khóa 7", "từ khóa 8"],
  "main_findings": "Các phát hiện chính và kết luận quan trọng nhất của nghiên cứu (2-3 câu)",
  "methodology": "Phương pháp nghiên cứu và công cụ được sử dụng (2-3 câu)"
}}

QUAN TRỌNG:
- CHỈ trả về JSON, không thêm bất kỳ text nào khác
- Không sử dụng markdown code blocks (```json hoặc ```)
- Tóm tắt phải chi tiết và có nội dung, không được chung chung
- Trích xuất 8 từ khóa quan trọng nhất
- Phân tích kỹ lưỡng về phương pháp và phát hiện

Nội dung bài báo:

{text[:15000]}
"""
        return prompt
    
    def _parse_response(self, response_text: str) -> dict:
        """
        Parse JSON response từ Claude
        
        Args:
            response_text: Text response
            
        Returns:
            dict: Parsed result
        """
        try:
            # Làm sạch response
            cleaned = response_text.strip()
            cleaned = cleaned.replace('```json', '').replace('```', '')
            cleaned = cleaned.strip()
            
            # Parse JSON
            result = json.loads(cleaned)
            
            # Validate và đặt giá trị mặc định
            return {
                'title': result.get('title', 'Không xác định'),
                'summary': result.get('summary', 'Không có tóm tắt'),
                'keywords': result.get('keywords', [])[:8],
                'main_findings': result.get('main_findings', 'Không có thông tin'),
                'methodology': result.get('methodology', 'Không có thông tin')
            }
            
        except json.JSONDecodeError:
            # Nếu không parse được JSON, trả về response text như tóm tắt
            return {
                'title': 'Không xác định',
                'summary': response_text[:500],
                'keywords': [],
                'main_findings': 'Không thể trích xuất',
                'methodology': 'Không thể trích xuất'
            }
    
    def batch_analyze(self, texts: list, filenames: list) -> list:
        """
        Phân tích nhiều bài báo
        
        Args:
            texts: Danh sách text
            filenames: Danh sách tên file
            
        Returns:
            list: Danh sách kết quả
        """
        results = []
        for text, filename in zip(texts, filenames):
            result = self.analyze(text, filename)
            results.append(result)
        
        return results
