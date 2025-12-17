"""
Setup configuration for Scientific Paper Analyzer
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="scientific-paper-analyzer",
    version="1.0.0",
    author="Nhóm 6 - Công nghệ số nâng cao",
    author_email="nhom6@example.com",
    description="Ứng dụng phân tích bài báo khoa học sử dụng GPT và BERT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/scientific-paper-analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "paper-analyzer=app:main",
        ],
    },
    include_package_data=True,
    keywords=[
        "scientific paper",
        "paper analysis",
        "NLP",
        "BERT",
        "GPT",
        "Claude",
        "text analysis",
        "keyword extraction",
        "summarization"
    ],
)
