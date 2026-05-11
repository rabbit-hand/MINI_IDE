#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini IDE - 日本語版 セットアップスクリプト
"""

from setuptools import setup, find_packages
import os

# READMEファイルを読み込む
def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

# ライセンスファイルを読み込む
def read_license():
    with open("LICENSE", "r", encoding="utf-8") as f:
        return f.read()

setup(
    name="mini-ide-japanese",
    version="1.0.0",
    author="Mini IDE Team",
    author_email="contact@mini-ide.com",
    description="高度な機能を備えたモダンで軽量なコードエディタ - 日本語版",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/mini-ide-japanese",
    license="MIT",
    license_content=read_license(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications :: Qt",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Code Editors",
        "Topic :: Text Editors",
    ],
    python_requires=">=3.8",
    install_requires=[
        "tkinter",
    ],
    py_modules=["mini_ide_japanese"],
    entry_points={
        "console_scripts": [
            "mini-ide-japanese=mini_ide_japanese:main",
        ],
        "gui_scripts": [
            "mini-ide-japanese-gui=mini_ide_japanese:main",
        ],
    },
    include_package_data=True,
    package_data={
        "mini_ide_japanese": [
            "*.md",
            "*.txt",
            "*.json",
        ],
    },
    keywords=[
        "コードエディタ",
        "IDE",
        "開発",
        "Python",
        "シンタックスハイライト",
        "ダークテーマ",
        "ライトテーマ",
        "自動保存",
    ],
    project_urls={
        "Bug Reports": "https://github.com/your-username/mini-ide-japanese/issues",
        "Source": "https://github.com/your-username/mini-ide-japanese",
        "Documentation": "https://github.com/your-username/mini-ide-japanese/blob/main/README.md",
    },
)
