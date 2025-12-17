"""
Export Handler Module
Xử lý export kết quả phân tích
"""

import json
import csv
from io import StringIO
import pandas as pd


class ExportHandler:
    """Class xử lý export kết quả"""
    
    def to_json(self, results: dict) -> str:
        """
        Export kết quả ra JSON
        
        Args:
            results: Kết quả phân tích
            
        Returns:
            str: JSON string
        """
        return json.dumps(results, ensure_ascii=False, indent=2)
    
    def to_csv(self, results: dict) -> str:
        """
        Export kết quả ra CSV
        
        Args:
            results: Kết quả phân tích
            
        Returns:
            str: CSV string
        """
        # Tạo list of dicts cho DataFrame
        data = []
        for paper in results['papers']:
            row = {
                'Filename': paper['filename'],
                'Title': paper['title'],
                'Summary': paper['summary'],
                'Keywords': ', '.join(paper['keywords']),
                'Main Findings': paper['main_findings'],
                'Methodology': paper['methodology']
            }
            data.append(row)
        
        # Tạo DataFrame
        df = pd.DataFrame(data)
        
        # Convert to CSV
        return df.to_csv(index=False)
    
    def to_markdown(self, results: dict) -> str:
        """
        Export kết quả ra Markdown
        
        Args:
            results: Kết quả phân tích
            
        Returns:
            str: Markdown string
        """
        md = f"# Kết Quả Phân Tích - {results['type']}\n\n"
        md += f"**Thời gian:** {results['timestamp']}\n\n"
        md += "---\n\n"
        
        for i, paper in enumerate(results['papers'], 1):
            md += f"## {i}. {paper['title']}\n\n"
            md += f"**File:** {paper['filename']}\n\n"
            
            md += "### Tóm Tắt\n\n"
            md += f"{paper['summary']}\n\n"
            
            md += "### Từ Khóa\n\n"
            for kw in paper['keywords']:
                md += f"- {kw}\n"
            md += "\n"
            
            md += "### Phát Hiện Chính\n\n"
            md += f"{paper['main_findings']}\n\n"
            
            md += "### Phương Pháp Nghiên Cứu\n\n"
            md += f"{paper['methodology']}\n\n"
            
            md += "---\n\n"
        
        return md
    
    def to_html(self, results: dict) -> str:
        """
        Export kết quả ra HTML
        
        Args:
            results: Kết quả phân tích
            
        Returns:
            str: HTML string
        """
        html = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kết Quả Phân Tích</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }
        .paper {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            border-left: 5px solid #667eea;
        }
        .keyword {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            margin: 5px;
            font-size: 14px;
        }
        .section {
            margin: 15px 0;
        }
        .section-title {
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
"""
        
        html += f"<h1>Kết Quả Phân Tích - {results['type']}</h1>"
        html += f"<p><strong>Thời gian:</strong> {results['timestamp']}</p>"
        
        for i, paper in enumerate(results['papers'], 1):
            html += f'<div class="paper">'
            html += f'<h2>{i}. {paper["title"]}</h2>'
            html += f'<p><em>File: {paper["filename"]}</em></p>'
            
            html += '<div class="section">'
            html += '<div class="section-title">Tóm Tắt</div>'
            html += f'<p>{paper["summary"]}</p>'
            html += '</div>'
            
            html += '<div class="section">'
            html += '<div class="section-title">Từ Khóa</div>'
            for kw in paper['keywords']:
                html += f'<span class="keyword">{kw}</span>'
            html += '</div>'
            
            html += '<div class="section">'
            html += '<div class="section-title">Phát Hiện Chính</div>'
            html += f'<p>{paper["main_findings"]}</p>'
            html += '</div>'
            
            html += '<div class="section">'
            html += '<div class="section-title">Phương Pháp Nghiên Cứu</div>'
            html += f'<p>{paper["methodology"]}</p>'
            html += '</div>'
            
            html += '</div>'
        
        html += """
    </div>
</body>
</html>
"""
        return html
