# Mini IDE - Professional Code Editor

A modern, lightweight code editor with advanced features, available in both English and Japanese versions.

![Mini IDE](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌍 Available Versions

### 🇺🇸 English Version
- **Location**: [`Mini-IDE-English/`](./Mini-IDE-English/)
- **Main File**: `mini_ide_english.pyw`
- **Documentation**: [README.md](./Mini-IDE-English/README.md)
- **Features**: Full English interface and documentation

### 🇯🇵 Japanese Version  
- **Location**: [`Mini-IDE-Japanese/`](./Mini-IDE-Japanese/)
- **Main File**: `mini_ide_japanese.pyw`
- **Documentation**: [README.md](./Mini-IDE-Japanese/README.md)
- **Features**: Full Japanese interface and documentation

## ✨ Key Features

### 🎯 Core Functionality
- **Multi-language Syntax Highlighting** - Python, JavaScript, HTML, CSS, JSON, XML, Markdown, Java, C#, C/C++, Rust
- **Dual Theme System** - Professional dark and light themes with smooth transitions
- **Smart Auto-save** - Configurable intervals with manual override
- **Advanced Font Control** - Customizable sizes with presets (Small, Medium, Large)
- **Recent Files Management** - Quick access to your workflow

### 🛠️ Advanced Editing Tools
- **Powerful Search & Replace** - Regex support with highlighting
- **Intelligent Code Formatting** - PEP8 standards compliance
- **Real-time Syntax Checking** - Instant error detection
- **Smart Auto-fix** - Common error pattern recognition
- **Line Manipulation** - Delete, duplicate, move operations
- **Comment Management** - Toggle and bracket operations

### 📦 Development Integration
- **Automatic Module Detection** - Install missing dependencies
- **Direct Code Execution** - Run Python code instantly
- **Test Runner Integration** - Unit test execution with timeout
- **Multi-format Export** - Support for 10+ programming languages

## 🚀 Quick Start

### Installation
- Python 3.8 or higher
- Tkinter (usually included with Python)

### Running the Application

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

### Package Installation
```bash
# English Version
pip install mini-ide-english

# Japanese Version
pip install mini-ide-japanese
```

## 📁 Repository Structure

```
mini-ide/
├── Mini-IDE-English/           # English version
│   ├── mini_ide_english.py    # Main application
│   ├── README.md               # English documentation
│   ├── setup.py               # Installation script
│   └── LICENSE                # MIT license
├── Mini-IDE-Japanese/         # Japanese version
│   ├── mini_ide_japanese.py   # Main application
│   ├── README.md               # Japanese documentation
│   ├── setup.py               # Installation script
│   └── LICENSE                # MIT license
├── README_GitHub.md           # This file
├── Professional Mini IDE.py    # Original version
└── Mini IDE1,２.pyw          # Japanese original
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

## 🎨 Customization Options

### Theme System
- **Dark Theme**: VSCode-inspired black interface
- **Light Theme**: Clean, bright workspace
- **Custom Colors**: Professional color schemes

### Font Configuration
- **Text Font**: 8px-32px range
- **UI Font**: 8px-24px range  
- **Presets**: Small (10px), Medium (14px), Large (18px)

### Auto-save Settings
- **Toggle**: Enable/disable functionality
- **Interval**: 10-300 second range
- **Manual Save**: Always available with Ctrl+S

## 📊 Supported Languages

| Category | Extensions | Languages |
|----------|-------------|-----------|
| **Web** | `.html`, `.htm`, `.css`, `.js`, `.ts` | HTML5, CSS3, JavaScript, TypeScript |
| **Data** | `.json`, `.xml`, `.md` | JSON, XML, Markdown |
| **Programming** | `.py`, `.java`, `.cs`, `.c`, `.cpp`, `.rs` | Python, Java, C#, C/C++, Rust |
| **All** | `*.*` | Any file type |

## 🛡️ Configuration Files

Both versions create these configuration files automatically:

- `theme_settings.json` - Theme and appearance preferences
- `font_settings.json` - Font size and style settings  
- `auto_save_settings.json` - Auto-save configuration
- `recent_files.json` - File history management

## 🔧 Development Setup

### For Contributors
1. Fork the appropriate version repository
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
- ✅ Real-time syntax checking and auto-fix

## 🤝 Contributing Guidelines

We welcome contributions! Please focus on:
- Bug fixes and performance improvements
- New language support for syntax highlighting  
- Additional theme options
- Enhanced keyboard shortcuts
- Better error detection patterns
- Documentation improvements

### Code Standards
- Follow PEP8 for Python code
- Use meaningful commit messages
- Test changes in both language versions
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./Mini-IDE-English/LICENSE) file for details.

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

**Mini IDE** - Professional code editing for developers worldwide! 🌍

Choose your language version above and start coding efficiently! 🚀
