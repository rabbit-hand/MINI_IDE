#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Mini IDE - English Version
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

# Read the license file
def read_license():
    with open("LICENSE", "r", encoding="utf-8") as f:
        return f.read()

setup(
    name="mini-ide-english",
    version="1.0.0",
    author="Mini IDE Team",
    author_email="contact@mini-ide.com",
    description="A modern, lightweight code editor with advanced features - English Version",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/mini-ide-english",
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
    py_modules=["mini_ide_english"],
    entry_points={
        "console_scripts": [
            "mini-ide-english=mini_ide_english:main",
        ],
        "gui_scripts": [
            "mini-ide-english-gui=mini_ide_english:main",
        ],
    },
    include_package_data=True,
    package_data={
        "mini_ide_english": [
            "*.md",
            "*.txt",
            "*.json",
        ],
    },
    keywords=[
        "code editor",
        "IDE",
        "development",
        "Python",
        "syntax highlighting",
        "dark theme",
        "light theme",
        "auto-save",
    ],
    project_urls={
        "Bug Reports": "https://github.com/your-username/mini-ide-english/issues",
        "Source": "https://github.com/your-username/mini-ide-english",
        "Documentation": "https://github.com/your-username/mini-ide-english/blob/main/README.md",
    },
)
