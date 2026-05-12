# Mini IDE v2.0 - Professional Code Editor

A modern, intelligent code editor with advanced error analysis, auto-fix capabilities, and virtual environment management. Available in both English and Japanese versions.

![Mini IDE](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Features](https://img.shields.io/badge/error_analysis-auto_fix-ff69b4.svg)
![Languages](https://img.shields.io/badge/languages-15%2B-orange.svg)

## 🌍 Available Versions

### 🇺🇸 English Version
- **Location**: [`Mini-IDE-English/`](./Mini-IDE-English/)
- **Main File**: `mini_ide_english.pyw`
- **Executable**: `Mini IDE English.exe`
- **Documentation**: [README.md](./Mini-IDE-English/README.md)
- **Features**: Full English interface and documentation

### 🇯🇵 Japanese Version  
- **Location**: [`Mini-IDE-Japanese/`](./Mini-IDE-Japanese/)
- **Main File**: `mini_ide_japanese.pyw`
- **Executable**: `Mini IDE Japanese.exe`
- **Documentation**: [README.md](./Mini-IDE-Japanese/README.md)
- **Features**: Full Japanese interface and documentation

## ✨ Key Features

### 🎯 Core Functionality
- **Multi-language Syntax Highlighting** - 15+ languages: Python, JavaScript, HTML, CSS, JSON, XML, Markdown, Java, C#, C/C++, Rust, PHP, Ruby, Go, Swift, Kotlin
- **Dual Theme System** - Professional dark and light themes with smooth transitions
- **Smart Auto-save** - Configurable intervals with manual override
- **Advanced Font Control** - Customizable sizes with presets (Small, Medium, Large)
- **Recent Files Management** - Quick access to your workflow
- **Optimized UI Layout** - No text truncation, proper button visibility

### 🛠️ Advanced Editing Tools
- **Powerful Search & Replace** - Regex support with highlighting
- **Intelligent Code Formatting** - PEP8 standards compliance
- **Line Manipulation** - Delete, duplicate, move operations
- **Comment Management** - Toggle and bracket operations
- **Clipboard Error Copy** - One-click error message copying

### 🤖 Intelligent Error Analysis & Auto-Fix
- **Smart Error Detection** - Automatic line number and error type identification
- **Visual Error Navigation** - Jump to error lines with highlighting
- **Auto-Fix Capabilities** - One-click fixes for common syntax errors
- **Error Suggestions** - Context-aware recommendations for complex issues
- **Multi-language Error Support** - Syntax, Indentation, Name, Type, Attribute, Import errors

### 📦 Development Integration
- **Enhanced Module Installation** - Auto-detect dependencies from code with virtual environment support
- **Virtual Environment Management** - Custom venv paths with persistent settings
- **Direct Code Execution** - Run Python code instantly with automatic error analysis
- **Package Installation** - Install modules in virtual or global environments
- **Error-to-Fix Workflow** - Seamless transition from error detection to resolution

## 🚀 Quick Start

### Installation
- Python 3.8 or higher
- Tkinter (usually included with Python)

### Running Application

#### Windows (Recommended)
```bash
# English Version - Double-click batch file
cd Mini-IDE-English
start_ide.bat

# Japanese Version - Double-click batch file
cd Mini-IDE-Japanese
start_ide.bat
```

#### Alternative Windows Method
```bash
# English Version
cd Mini-IDE-English
pythonw.exe mini_ide_english.pyw

# Japanese Version
cd Mini-IDE-Japanese
pythonw.exe mini_ide_japanese.pyw
```

#### macOS/Linux
```bash
# English Version
cd Mini-IDE-English
python mini_ide_english.pyw

# Japanese Version
cd Mini-IDE-Japanese
python mini_ide_japanese.pyw
```

### 🎯 First Steps with Error Analysis
1. **Write Code** - Create or open a Python file
2. **Run Code** - Press F5 or click Run button
3. **Error Detection** - If errors occur, analysis dialog appears automatically
4. **Auto-Fix** - Click "🔧 Auto Fix" for common syntax errors
5. **Navigate** - Use "📍 Go to Line" to jump to error locations

### 📦 Virtual Environment Setup
1. **Open Module Installer** - Click 📦 Install button
2. **Configure Venv** - Enable "Use Virtual Environment" and set custom path
3. **Auto-Detect Modules** - Choose "Auto-detect from code" to find required packages
4. **Install** - Select modules and install with one click

## 📁 Repository Structure

```
mini-ide/
├── Mini-IDE-English/           # English version
│   ├── mini_ide_english.pyw    # Main application
│   ├── README.md               # English documentation
│   ├── setup.py               # Installation script
│   ├── LICENSE                # MIT license
│   ├── dist/                  # Built executable
│   │   └── Mini IDE English.exe
│   └── [config files]        # Settings files
├── Mini-IDE-Japanese/         # Japanese version
│   ├── mini_ide_japanese.pyw  # Main application
│   ├── README.md               # Japanese documentation
│   ├── setup.py               # Installation script
│   ├── LICENSE                # MIT license
│   ├── dist/                  # Built executable
│   │   └── Mini IDE Japanese.exe
│   └── [config files]        # Settings files
├── README.md                  # This file
├── README_GitHub.md          # GitHub main README
└── [legacy files]            # Original versions
```

## ⌨️ Universal Shortcuts

| Category | Shortcut | Action |
|----------|-----------|---------|
| **File** | `Ctrl+N` | New file |
| | `Ctrl+O` | Open file |
| | `Ctrl+S` | Save file |
| | `F5` | Run code |
| **Edit** | `Ctrl+Z` | Undo |
| | `Ctrl+Y` | Redo |
| | `Ctrl+X` | Cut |
| | `Ctrl+C` | Copy |
| | `Ctrl+V` | Paste |
| | `Ctrl+A` | Select all |
| | `Ctrl+F` | Find |
| | `Ctrl+H` | Replace |
| | `Ctrl+D` | Delete line |
| | `Ctrl+Shift+D` | Duplicate line |
| | `Alt+↑` | Move line up |
| | `Alt+↓` | Move line down |
| | `Ctrl+/` | Toggle comment |
| **View** | `Ctrl+T` | Toggle theme |
| | `Ctrl++` | Increase font |
| | `Ctrl+-` | Decrease font |

## 📊 Supported Languages

| Category | Extensions | Languages |
|----------|-------------|-----------|
| **Web** | `.html`, `.htm`, `.css`, `.js`, `.ts`, `.php` | HTML5, CSS3, JavaScript, TypeScript, PHP |
| **Data** | `.json`, `.xml`, `.md`, `.yaml`, `.yml` | JSON, XML, Markdown, YAML |
| **Programming** | `.py`, `.java`, `.cs`, `.c`, `.cpp`, `.rs`, `.go`, `.swift`, `.kt`, `.rb` | Python, Java, C#, C/C++, Rust, Go, Swift, Kotlin, Ruby |
| **Mobile** | `.swift`, `.kt`, `.dart` | Swift (iOS), Kotlin (Android), Dart (Flutter) |
| **All** | `*.*` | Any file type with syntax highlighting |

## 🛡️ Configuration Files

Both versions create these configuration files automatically:

- `theme_settings.json` - Theme and appearance preferences
- `font_settings.json` - Font size and style settings  
- `auto_save_settings.json` - Auto-save configuration
- `recent_files.json` - File history management
- `venv_settings.json` - Virtual environment path and usage settings

## 🔧 Development Setup

### For Contributors
1. Fork appropriate version repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly in both versions
5. Submit pull requests

### Testing
```bash
# Test English version
cd Mini-IDE-English
python mini_ide_english.py

# Test Japanese version  
cd Mini-IDE-Japanese
python mini_ide_japanese.py
```

## 📝 Release Notes

### Version 2.0.0
- ✅ **Intelligent Error Analysis** - Automatic line number and error type detection
- ✅ **Auto-Fix Capabilities** - One-click fixes for common syntax errors
- ✅ **Visual Error Navigation** - Jump to error lines with highlighting
- ✅ **Virtual Environment Management** - Custom venv paths with persistent settings
- ✅ **Enhanced Module Installation** - Auto-detect dependencies from code
- ✅ **Clipboard Error Copy** - One-click error message copying
- ✅ **Optimized UI Layout** - No text truncation, proper button visibility
- ✅ **Extended Language Support** - 15+ programming languages
- ✅ **Error Suggestions System** - Context-aware recommendations
- ✅ **Improved User Experience** - Better error handling and feedback

### Version 1.0.0
- ✅ Initial release of both English and Japanese versions
- ✅ Complete feature parity between versions
- ✅ Modern dark/light theme system
- ✅ Advanced syntax highlighting for 10+ languages
- ✅ Intelligent auto-save with customization
- ✅ Professional font management
- ✅ Comprehensive keyboard shortcuts
- ✅ Module installation and code execution
- ✅ Search, replace, and code formatting

## 🤝 Contributing Guidelines

We welcome contributions! Please focus on:
- Bug fixes and performance improvements
- New language support for syntax highlighting  
- Additional theme options
- Enhanced keyboard shortcuts
- **Better error detection patterns** - Add regex patterns for new error types
- **Auto-fix algorithms** - Improve automatic error correction
- **Virtual environment features** - Enhanced venv management
- **UI/UX improvements** - Better layout and user experience
- **Documentation improvements** - Update for new features

### Code Standards
- Follow PEP8 for Python code
- Use meaningful commit messages
- Test changes in both language versions
- Update documentation for new features
- Test error analysis and auto-fix functionality

## 📄 License

This project is licensed under MIT License - see the [LICENSE](./Mini-IDE-English/LICENSE) file for details.

## 🙏 Acknowledgments

- **tkinter** - GUI framework foundation
- **Python Community** - Libraries and modules
- **VS Code Team** - Color scheme inspiration  
- **Open Source Contributors** - Feature improvements
- **International Community** - Translation and localization support

## 📞 Support & Contact

### Getting Help
1. Check version-specific README files
2. Search existing issues
3. Create detailed bug reports
4. Include system information

### Issue Reporting
When reporting issues, please include:
- Version (English/Japanese)
- Operating system
- Python version
- Steps to reproduce
- Error messages and screenshots

---

**Mini IDE v2.0** - Professional code editing with intelligent error analysis! 🌍

Choose your language version above and start coding efficiently! 🚀

## 🎯 Error Analysis Workflow

1. **Code Execution** → Error Detection
2. **Error Analysis** → Line Number & Type Identification  
3. **Auto-Fix** → One-Click Correction
4. **Navigation** → Jump to Error Location
5. **Learning** → Understand Error Patterns

## 📦 Virtual Environment Features

- **Custom Paths** - Set your preferred venv location
- **Persistent Settings** - Remember your configuration
- **Auto-Detection** - Find required modules automatically
- **Flexible Installation** - Choose venv or global environment
