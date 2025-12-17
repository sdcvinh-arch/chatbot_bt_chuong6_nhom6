"""
Chatbot Module
Trả lời câu hỏi dựa trên dữ liệu đã upload (PDF, Excel, CSV)
"""

import os
import pandas as pd
from groq import Groq


class DataChatbot:
    """Chatbot trả lời câu hỏi từ dữ liệu"""
    
    def __init__(self):
        api_key = os.environ.get('GROQ_API_KEY')
        if not api_key:
            raise ValueError("GROQ_API_KEY không được thiết lập")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"
        self.conversation_history = []
        self.data_context = ""
    
    def load_data_context(self, data_text: str, source_name: str):
        """
        Load dữ liệu làm context cho chatbot
        
        Args:
            data_text: Nội dung dữ liệu
            source_name: Tên nguồn dữ liệu
        """
        self.data_context = f"""Dữ liệu từ: {source_name}

{data_text[:30000]}

---
Trên đây là toàn bộ dữ liệu có sẵn. Hãy trả lời câu hỏi dựa trên dữ liệu này.
"""
        self.conversation_history = []
    
    def ask(self, question: str) -> str:
        """
        Đặt câu hỏi cho chatbot
        
        Args:
            question: Câu hỏi của người dùng
            
        Returns:
            str: Câu trả lời
        """
        try:
            # Thêm câu hỏi vào lịch sử
            self.conversation_history.append({
                "role": "user",
                "content": question
            })
            
            # Tạo messages cho API
            messages = [
                {
                    "role": "system",
                    "content": f"""Bạn là một trợ lý AI thông minh, chuyên phân tích và trả lời câu hỏi dựa trên dữ liệu được cung cấp.

QUAN TRỌNG:
- Chỉ trả lời dựa trên dữ liệu đã cho
- Nếu không tìm thấy thông tin trong dữ liệu, hãy nói rõ "Không tìm thấy thông tin này trong dữ liệu"
- Trả lời ngắn gọn, súc tích, dễ hiểu
- Trích dẫn số liệu cụ thể nếu có
- Trả lời bằng tiếng Việt

DỮ LIỆU:
{self.data_context}"""
                }
            ]
            
            # Thêm lịch sử hội thoại (giới hạn 10 tin nhắn gần nhất)
            recent_history = self.conversation_history[-10:]
            messages.extend(recent_history)
            
            # Gọi API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            
            # Lấy câu trả lời
            answer = response.choices[0].message.content
            
            # Thêm câu trả lời vào lịch sử
            self.conversation_history.append({
                "role": "assistant",
                "content": answer
            })
            
            return answer
            
        except Exception as e:
            return f"Lỗi: {str(e)}"
    
    def clear_history(self):
        """Xóa lịch sử hội thoại"""
        self.conversation_history = []
    
    def get_conversation_history(self) -> list:
        """Lấy lịch sử hội thoại"""
        return self.conversation_history


class DataProcessor:
    """Xử lý các loại file dữ liệu"""
    
    @staticmethod
    def process_excel(file) -> str:
        """
        Xử lý file Excel
        
        Args:
            file: File Excel đã upload
            
        Returns:
            str: Nội dung dạng text
        """
        try:
            # Đọc Excel
            df = pd.read_excel(file, sheet_name=None)  # Đọc tất cả sheets
            
            text = "THÔNG TIN TỪ FILE EXCEL:\n\n"
            
            # Xử lý từng sheet
            for sheet_name, sheet_df in df.items():
                text += f"--- Sheet: {sheet_name} ---\n"
                text += f"Số hàng: {len(sheet_df)}\n"
                text += f"Các cột: {', '.join(sheet_df.columns.tolist())}\n\n"
                
                # Thêm dữ liệu (giới hạn 1000 hàng)
                text += sheet_df.head(1000).to_string(index=False)
                text += "\n\n"
            
            return text
            
        except Exception as e:
            return f"Lỗi đọc Excel: {str(e)}"
    
    @staticmethod
    def process_csv(file) -> str:
        """
        Xử lý file CSV
        
        Args:
            file: File CSV đã upload
            
        Returns:
            str: Nội dung dạng text
        """
        try:
            # Đọc CSV
            df = pd.read_csv(file)
            
            text = "THÔNG TIN TỪ FILE CSV:\n\n"
            text += f"Số hàng: {len(df)}\n"
            text += f"Các cột: {', '.join(df.columns.tolist())}\n\n"
            
            # Thêm dữ liệu (giới hạn 1000 hàng)
            text += df.head(1000).to_string(index=False)
            
            return text
            
        except Exception as e:
            return f"Lỗi đọc CSV: {str(e)}"
    
    @staticmethod
    def process_pdf(file, pdf_processor) -> str:
        """
        Xử lý file PDF
        
        Args:
            file: File PDF đã upload
            pdf_processor: Instance của PDFProcessor
            
        Returns:
            str: Nội dung dạng text
        """
        try:
            text = pdf_processor.extract_text(file)
            return f"THÔNG TIN TỪ FILE PDF:\n\n{text}"
        except Exception as e:
            return f"Lỗi đọc PDF: {str(e)}"
