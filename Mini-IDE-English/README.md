# Mini IDE - English Version

A modern, lightweight code editor with advanced features for developers.

![Mini IDE](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

### 🎯 Core Features
- **Syntax Highlighting** - Support for Python, JavaScript, HTML, CSS, JSON, XML, Markdown, Java, C#, C/C++, and Rust
- **Dark/Light Theme** - Eye-friendly themes with smooth transitions
- **Auto-save** - Configurable auto-save with customizable intervals
- **Font Customization** - Adjustable font sizes with presets (Small, Medium, Large)
- **Recent Files** - Quick access to your recently opened files

### 🛠️ Advanced Editing
- **Search & Replace** - Powerful find and replace functionality
- **Code Formatting** - Automatic code formatting to PEP8 standards
- **Syntax Checking** - Real-time syntax error detection
- **Auto-fix** - Intelligent error correction
- **Line Operations** - Delete, duplicate, move lines up/down
- **Comment Toggle** - Quick comment/uncomment functionality
- **Bracket Enclosing** - Wrap selections in various bracket types

### 📦 Development Tools
- **Module Installation** - Automatic detection and installation of missing Python modules
- **Code Execution** - Run Python code directly from the editor
- **Test Runner** - Execute unit tests with timeout settings
- **Multi-language Support** - Save files in various programming languages

### 🎨 User Interface
- **Modern Design** - Clean, professional interface with smooth animations
- **Responsive Layout** - Adjustable window size with maximized startup
- **Status Bar** - Real-time file information, cursor position, and modification status
- **Keyboard Shortcuts** - Comprehensive keyboard shortcuts for productivity
- **Tooltips** - Helpful hints for all functions

## 🚀 Quick Start

### Installation
1. Clone or download the repository
2. Navigate to the project directory
3. Run the application:
   ```bash
   python mini_ide_english.py
   ```

### System Requirements
- **Python 3.8 or higher**
- **tkinter** (usually included with Python)
- **Windows, macOS, or Linux**

## 📋 Supported File Types

| Category | Extensions | Description |
|----------|-------------|-------------|
| **Web** | `.html`, `.htm`, `.css`, `.js`, `.ts` | Web development files |
| **Data** | `.json`, `.xml`, `.md` | Data and documentation |
| **Programming** | `.py`, `.pyw`, `.java`, `.cs`, `.c`, `.cpp`, `.h`, `.hpp`, `.rs` | Programming languages |
| **All Files** | `*.*` | All file types |

## ⌨️ Keyboard Shortcuts

| Category | Shortcut | Action |
|----------|-----------|--------|
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
| | `Ctrl++` | Increase font size |
| | `Ctrl+-` | Decrease font size |
| | `Ctrl+MouseWheel` | Zoom in/out |

## 🎯 Usage

### Basic Operations
1. **Create New File**: Click "New" or press `Ctrl+N`
2. **Open Existing File**: Click "Open" or press `Ctrl+O`
3. **Save File**: Click "Save" or press `Ctrl+S`
4. **Run Code**: Click "Run" or press `F5`

### Advanced Features
1. **Module Installation**: The editor automatically detects missing modules and offers to install them
2. **Code Formatting**: Use "Format Code" to apply PEP8 standards
3. **Syntax Checking**: Real-time syntax validation with error highlighting
4. **Auto-fix**: Intelligent error correction for common issues

## 🔧 Customization

### Theme Settings
- **Dark Theme**: Black background with high contrast text
- **Light Theme**: Clean, bright interface
- **Custom Colors**: VSCode-inspired color scheme

### Font Settings
- **Text Font**: Adjustable from 8px to 32px
- **Button Font**: Adjustable from 8px to 24px
- **Presets**: Small (10px), Medium (14px), Large (18px)

### Auto-save Configuration
- **Enable/Disable**: Toggle auto-save functionality
- **Interval**: Set custom save intervals (10-300 seconds)
- **Manual Override**: Save anytime with `Ctrl+S`

## 📁 File Structure

```
Mini-IDE-English/
├── mini_ide_english.py    # Main application file
├── README.md               # This documentation
├── theme_settings.json     # Theme and font preferences
├── font_settings.json     # Font configuration
├── auto_save_settings.json # Auto-save configuration
└── recent_files.json      # Recent files history
```

## 🐛 Troubleshooting

### Common Issues
1. **Module Import Errors**: Use the "Install Modules" feature to automatically install missing packages
2. **Font Display Issues**: Adjust font settings in the "Font Size" menu
3. **Theme Problems**: Reset theme settings by deleting `theme_settings.json`
4. **Auto-save Not Working**: Check auto-save configuration and file permissions

### Performance Tips
1. **Large Files**: The editor handles large files efficiently
2. **Memory Usage**: Auto-save helps prevent data loss without excessive memory usage
3. **Syntax Highlighting**: Optimized for real-time performance

## 🔄 Updates and Maintenance

### Automatic Updates
- **pip Integration**: Built-in pip update functionality
- **Module Management**: Automatic dependency resolution
- **Settings Migration**: Preserves preferences across updates

### Manual Updates
1. Download the latest version
2. Replace the existing file
3. Settings are automatically preserved

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Report issues and bugs
- Suggest new features
- Submit pull requests
- Improve documentation

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **tkinter** - For the GUI framework
- **Python Community** - For various libraries and modules
- **VS Code** - For color scheme inspiration
- **Open Source Contributors** - For making this project better

## 📞 Support

For support, please:
1. Check the troubleshooting section
2. Search existing issues
3. Create a new issue with detailed information
4. Include system information and error messages

---

**Mini IDE English Version** - Making coding more efficient and enjoyable! 🚀
