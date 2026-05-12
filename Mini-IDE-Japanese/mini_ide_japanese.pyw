#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mini IDE - Modern Japanese Version V2
モダンで軽量なコードエディタ（高度な機能付き）
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading
import sys
import re
import locale
import importlib
import platform
from threading import Thread
import tempfile
import os
import json

# ===== プラットフォーム検出 =====
def detect_platform():
    """現在のプラットフォームを検出"""
    return platform.system().lower()

def get_system_fonts():
    """システムに適したフォントを取得"""
    system = detect_platform()
    
    if system == 'windows':
        return {
            'text_font': 'Consolas',
            'ui_font': 'Segoe UI',
            'default_size': 14
        }
    elif system == 'darwin':  # macOS
        return {
            'text_font': 'Menlo',
            'ui_font': 'SF Pro Text',
            'default_size': 14
        }
    else:  # Linuxとその他
        return {
            'text_font': 'DejaVu Sans Mono',
            'ui_font': 'Ubuntu',
            'default_size': 14
        }

# ===== 言語サポート =====
LANGUAGE = 'ja'  # このバージョンは日本語に固定

def detect_language():
    return 'ja'  # このバージョンは常に日本語を返す

current_language = detect_language()
current_platform = detect_platform()
system_fonts = get_system_fonts()

TRANSLATIONS = {
    'app_title': {'ja': 'Mini IDE', 'en': 'Mini IDE'},
    'new': {'ja': '新規', 'en': 'New'},
    'open': {'ja': '開く', 'en': 'Open'},
    'save': {'ja': '保存', 'en': 'Save'},
    'save_as': {'ja': '名前を付けて保存', 'en': 'Save As'},
    'paste': {'ja': '貼り付け', 'en': 'Paste'},
    'clear': {'ja': 'クリア', 'en': 'Clear'},
    'zoom_in': {'ja': '拡大', 'en': 'Zoom In'},
    'zoom_out': {'ja': '縮小', 'en': 'Zoom Out'},
    'toggle_theme': {'ja': 'テーマ切替', 'en': 'Toggle Theme'},
    'install_modules': {'ja': 'モジュールインストール', 'en': 'Install Modules'},
    'format_code': {'ja': 'コード整形', 'en': 'Format Code'},
    'auto_fix': {'ja': '自動修正', 'en': 'Auto Fix'},
    'syntax_check': {'ja': '構文チェック', 'en': 'Syntax Check'},
    'run': {'ja': '実行', 'en': 'Run'},
    'file': {'ja': 'ファイル', 'en': 'File'},
    'edit': {'ja': '編集', 'en': 'Edit'},
    'view': {'ja': '表示', 'en': 'View'},
    'tools': {'ja': 'ツール', 'en': 'Tools'},
    'search': {'ja': '検索', 'en': 'Search'},
    'replace': {'ja': '置換', 'en': 'Replace'},
    'project': {'ja': 'プロジェクト', 'en': 'Project'},
    'terminal': {'ja': 'ターミナル', 'en': 'Terminal'},
    'settings': {'ja': '設定', 'en': 'Settings'},
    'about': {'ja': 'について', 'en': 'About'},
    'exit': {'ja': '終了', 'en': 'Exit'},
    'undo': {'ja': '元に戻す', 'en': 'Undo'},
    'redo': {'ja': 'やり直し', 'en': 'Redo'},
    'cut': {'ja': '切り取り', 'en': 'Cut'},
    'copy': {'ja': 'コピー', 'en': 'Copy'},
    'select_all': {'ja': 'すべて選択', 'en': 'Select All'},
    'find': {'ja': '検索', 'en': 'Find'},
    'find_next': {'ja': '次を検索', 'en': 'Find Next'},
    'find_previous': {'ja': '前を検索', 'en': 'Find Previous'},
    'replace_all': {'ja': 'すべて置換', 'en': 'Replace All'},
    'close': {'ja': '閉じる', 'en': 'Close'},
    'ok': {'ja': 'OK', 'en': 'OK'},
    'cancel': {'ja': 'キャンセル', 'en': 'Cancel'},
    'yes': {'ja': 'はい', 'en': 'Yes'},
    'no': {'ja': 'いいえ', 'en': 'No'},
    'confirm': {'ja': '確認', 'en': 'Confirm'},
    'warning': {'ja': '警告', 'en': 'Warning'},
    'error': {'ja': 'エラー', 'en': 'Error'},
    'info': {'ja': '情報', 'en': 'Information'},
    'success': {'ja': '成功', 'en': 'Success'},
    'failed': {'ja': '失敗', 'en': 'Failed'},
    'loading': {'ja': '読み込み中', 'en': 'Loading'},
    'ready': {'ja': '準備完了', 'en': 'Ready'},
    'modified': {'ja': '変更済み', 'en': 'Modified'},
    'unsaved': {'ja': '未保存', 'en': 'Unsaved'},
    'line': {'ja': '行', 'en': 'Line'},
    'column': {'ja': '列', 'en': 'Column'},
    'characters': {'ja': '文字数', 'en': 'Characters'},
    'words': {'ja': '単語数', 'en': 'Words'},
    'file_not_found': {'ja': 'ファイルが見つかりません', 'en': 'File not found'},
    'file_saved': {'ja': 'ファイルを保存しました', 'en': 'File saved'},
    'file_not_saved': {'ja': 'ファイルを保存できませんでした', 'en': 'File could not be saved'},
    'no_file_open': {'ja': 'ファイルが開かれていません', 'en': 'No file is open'},
    'confirm_close': {'ja': '変更を保存しますか？', 'en': 'Save changes before closing?'},
    'confirm_clear': {'ja': 'テキストをクリアしますか？ 保存されていない変更は失われます。', 'en': 'Clear the editor content? Unsaved changes will be lost.'},
    'copy_success': {'ja': 'コピーしました', 'en': 'Copied to clipboard'},
    'no_selection': {'ja': 'テキストが選択されていません', 'en': 'No text selected.'},
    'search_not_found': {'ja': '検索文字列が見つかりませんでした', 'en': 'Search string not found'},
    'replace_count': {'ja': '件を置換しました', 'en': 'items replaced'},
    'font_size': {'ja': 'フォントサイズ', 'en': 'Font Size'},
    'theme': {'ja': 'テーマ', 'en': 'Theme'},
    'dark_theme': {'ja': 'ダークテーマ', 'en': 'Dark Theme'},
    'light_theme': {'ja': 'ライトテーマ', 'en': 'Light Theme'},
    'auto_save': {'ja': '自動保存', 'en': 'Auto Save'},
    'auto_save_enabled': {'ja': '自動保存を有効にする', 'en': 'Enable auto save'},
    'auto_save_interval': {'ja': '自動保存間隔（秒）', 'en': 'Auto save interval (seconds)'},
    'recent_files': {'ja': '最近のファイル', 'en': 'Recent Files'},
    'no_recent_files': {'ja': '最近のファイルがありません', 'en': 'No recent files'},
    'python_files': {'ja': 'Pythonファイル', 'en': 'Python Files'},
    'all_files': {'ja': 'すべてのファイル', 'en': 'All Files'},
    'install_start': {'ja': 'モジュールの解析とインストールを開始します。', 'en': 'Starting module analysis and installation.'},
    'install_none': {'ja': 'インストールするモジュールが見つかりませんでした。', 'en': 'No modules found to install.'},
    'install_prompt': {'ja': '以下のモジュールをインストールしますか？', 'en': 'Install the following modules?'},
    'install_complete': {'ja': 'インストールが完了しました。', 'en': 'Installation completed.'},
    'install_failed': {'ja': 'インストールに失敗しました', 'en': 'Installation failed'},
    'format_complete': {'ja': 'コードが整形されました。', 'en': 'Code has been formatted.'},
    'format_failed': {'ja': 'コード整形に失敗しました', 'en': 'Code formatting failed'},
    'syntax_ok': {'ja': '構文エラーは検出されませんでした。', 'en': 'No syntax errors were detected.'},
    'syntax_error': {'ja': '構文エラーが検出されました', 'en': 'Syntax errors were detected'},
    'auto_fix_complete': {'ja': '自動修正が完了しました', 'en': 'Auto-fix completed'},
    'auto_fix_none': {'ja': '修正が必要なエラーは見つかりませんでした。', 'en': 'No fixable errors were found.'},
    'run_complete': {'ja': 'コード実行が完了しました', 'en': 'Code execution completed'},
    'run_failed': {'ja': 'コード実行に失敗しました', 'en': 'Code execution failed'},
    'run_timeout': {'ja': 'コード実行がタイムアウトしました', 'en': 'Code execution timed out'},
    'settings_saved': {'ja': '設定を保存しました', 'en': 'Settings saved'},
    'about_title': {'ja': 'Mini IDE について', 'en': 'About Mini IDE'},
    'about_text': {'ja': 'Mini IDE\n\nモダンで軽量なコードエディタ\n\nバージョン 2.0\n\n© 2025 Mini IDE Team', 'en': 'Mini IDE\n\nA modern, lightweight code editor\n\nVersion 2.0\n\n© 2025 Mini IDE Team'},
}

def t(key):
    return TRANSLATIONS.get(key, {}).get(current_language, TRANSLATIONS.get(key, {}).get('ja', key))

# ===== クロスプラットフォーム設定 =====
def get_config_dir():
    """プラットフォームに適した設定ディレクトリを取得"""
    system = detect_platform()
    if system == 'windows':
        return os.path.join(os.environ.get('APPDATA', ''), 'Mini-IDE')
    elif system == 'darwin':  # macOS
        return os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Mini-IDE')
    else:  # Linuxとその他
        return os.path.join(os.path.expanduser('~'), '.config', 'mini-ide')

# 設定ディレクトリを確保
CONFIG_DIR = get_config_dir()
os.makedirs(CONFIG_DIR, exist_ok=True)

# 設定ファイル
SETTINGS_FILE = os.path.join(CONFIG_DIR, 'settings.json')
RECENT_FILES_FILE = os.path.join(CONFIG_DIR, 'recent_files.json')

# グローバル変数
current_theme = 'dark'
current_font_size = system_fonts['default_size']
auto_save_enabled = True
auto_save_interval = 30000  # 30秒
recent_files = []
open_tabs = []
active_tab = None

# モダンなカラースキーム
THEMES = {
    'dark': {
        'bg': '#1e1e1e',
        'bg_secondary': '#252526',
        'bg_tertiary': '#2d2d2d',
        'fg': '#cccccc',
        'fg_secondary': '#969696',
        'accent': '#007acc',
        'accent_hover': '#1e90ff',
        'success': '#4ec9b0',
        'warning': '#ffa500',
        'error': '#f48771',
        'border': '#3e3e42',
        'text_bg': '#1e1e1e',
        'line_numbers_bg': '#252526',
        'line_numbers_fg': '#858585',
        'selection_bg': '#264f78',
        'cursor': '#aeafad',
        'tab_bg': '#2d2d2d',
        'tab_active_bg': '#1e1e1e',
        'tab_fg': '#cccccc',
        'tab_border': '#3e3e42',
        'toolbar_bg': '#2d2d2d',
        'status_bar_bg': '#1e1e1e',
        'status_bar_fg': '#cccccc',
    },
    'light': {
        'bg': '#ffffff',
        'bg_secondary': '#f3f3f3',
        'bg_tertiary': '#e8e8e8',
        'fg': '#333333',
        'fg_secondary': '#6e6e6e',
        'accent': '#007acc',
        'accent_hover': '#005a9e',
        'success': '#28a745',
        'warning': '#ffc107',
        'error': '#dc3545',
        'border': '#d4d4d4',
        'text_bg': '#ffffff',
        'line_numbers_bg': '#f3f3f3',
        'line_numbers_fg': '#858585',
        'selection_bg': '#add8e6',
        'cursor': '#000000',
        'tab_bg': '#f3f3f3',
        'tab_active_bg': '#ffffff',
        'tab_fg': '#333333',
        'tab_border': '#d4d4d4',
        'toolbar_bg': '#f3f3f3',
        'status_bar_bg': '#333333',
        'status_bar_fg': '#ffffff',
    }
}

class ToolTip:
    """ウィジェットにツールチップを作成"""
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind('<Enter>', self.enter)
        self.widget.bind('<Leave>', self.leave)
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def enter(self, event=None):
        self.show_tooltip()

    def leave(self, event=None):
        self.hide_tooltip()

    def show_tooltip(self):
        """ツールチップを表示"""
        if self.tipwindow or not self.text:
            return
        
        # ウィジェットの位置を取得
        x = self.widget.winfo_rootx() + 25
        y = self.widget.winfo_rooty() + 25
        
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=(system_fonts['ui_font'], 9))
        label.pack(ipadx=1)

    def hide_tooltip(self):
        """ツールチップを非表示"""
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

class ModernTab:
    """ファイル編集用のモダンなタブウィジェット"""
    def __init__(self, parent, file_path=None, content=""):
        self.parent = parent
        self.file_path = file_path
        self.content = content
        self.modified = False
        self.original_content = content
        
        self.create_widgets()
    
    def create_widgets(self):
        theme = THEMES[current_theme]
        
        # テキストウィジェットを作成
        self.text = tk.Text(
            self.parent,
            font=(system_fonts['text_font'], current_font_size),
            bg=theme['text_bg'],
            fg=theme['fg'],
            insertbackground=theme['cursor'],
            selectbackground=theme['selection_bg'],
            undo=True,
            maxundo=-1,
            wrap=tk.NONE,
            padx=5,
            pady=5,
            borderwidth=0,
            highlightthickness=0
        )
        
        # 行番号を作成
        self.line_numbers = tk.Text(
            self.parent,
            width=4,
            padx=3,
            takefocus=0,
            border=0,
            state='disabled',
            wrap='none',
            font=(system_fonts['text_font'], current_font_size),
            bg=theme['line_numbers_bg'],
            fg=theme['line_numbers_fg']
        )
        
        # イベントをバインド
        self.text.bind('<KeyRelease>', self.on_text_change)
        self.text.bind('<Button-1>', self.update_line_numbers)
        self.text.bind('<Key>', self.update_line_numbers)
        
        # 初期行番号
        self.update_line_numbers()
    
    def on_text_change(self, event=None):
        if not self.modified:
            self.modified = True
            self.parent.update_tab_title(self)
        self.update_line_numbers()
    
    def update_line_numbers(self, event=None):
        lines = self.text.get("1.0", "end-1c").split('\n')
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        for i, line in enumerate(lines, 1):
            self.line_numbers.insert('end', f"{i}\n")
        self.line_numbers.config(state='disabled')
    
    def get_content(self):
        return self.text.get("1.0", tk.END)
    
    def set_content(self, content):
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", content)
        self.original_content = content
        self.modified = False
        self.update_line_numbers()

class ModernIDE:
    """モダンなIDEアプリケーション"""
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_ui()
        self.load_settings()
        self.apply_theme()
        
    def setup_window(self):
        self.root.title("Mini IDE - Modern Japanese")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # 起動時にウィンドウを最大化
        self.root.state('zoomed')  # Windows 最大化
        # クロスプラットフォーム対応の代替案：
        # self.root.attributes('-zoomed', True)
    
    def setup_ui(self):
        theme = THEMES[current_theme]
        
        # メインコンテナ
        self.main_frame = tk.Frame(self.root, bg=theme['bg'])
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ツールバーを作成
        self.create_toolbar()
        
        # タブエリアを作成
        self.create_tab_area()
        
        # ステータスバーを作成
        self.create_status_bar()
        
        # メニューを作成
        self.create_menu()
        
        # キーボードショートカットをバインド
        self.bind_shortcuts()
    
    def create_toolbar(self):
        theme = THEMES[current_theme]
        
        self.toolbar = tk.Frame(self.main_frame, bg=theme['toolbar_bg'], height=40)
        self.toolbar.pack(fill=tk.X, padx=0, pady=0)
        self.toolbar.pack_propagate(False)
        
        # ツールバーボタン
        buttons = [
            ("📄", "新規", self.new_file, "Ctrl+N"),
            ("📂", "開く", self.open_file, "Ctrl+O"),
            ("💾", "保存", self.save_file, "Ctrl+S"),
            ("✂️", "切取", self.cut_text, "Ctrl+X"),
            ("📋", "コピー", self.copy_text, "Ctrl+C"),
            ("📋", "貼付", self.paste_text, "Ctrl+V"),
            ("🔍", "検索", self.show_find_dialog, "Ctrl+F"),
            ("🔄", "置換", self.show_replace_dialog, "Ctrl+H"),
            ("🎨", "整形", self.format_code, ""),
            ("✅", "確認", self.check_syntax, ""),
            ("🔧", "修正", self.auto_fix, ""),
            ("📦", "インスト", self.install_module, "Ctrl+I"),
            ("▶️", "実行", self.run_code, "F5"),
            ("🌙", "テーマ", self.toggle_theme, "Ctrl+T"),
            ("⚙️", "設定", self.show_settings, ""),
        ]
        
        for icon, label, command, shortcut in buttons:
            btn = tk.Button(
                self.toolbar,
                text=f"{icon}\n{label}",
                command=command,
                font=(system_fonts['ui_font'], 10),
                bg=theme['toolbar_bg'],
                fg=theme['fg'],
                relief=tk.FLAT,
                borderwidth=0,
                padx=4,
                pady=3,
                cursor='hand2',
                width=8,
                height=2
            )
            btn.pack(side=tk.LEFT, padx=1, pady=3)
            
            # ツールチップを追加（説明とショートカット）
            tooltip_text = f"{label}"
            if shortcut:
                tooltip_text += f" ({shortcut})"
            ToolTip(btn, tooltip_text)
            
            # ホバーエフェクト
            def create_hover_effect(button):
                def on_enter(e):
                    button.configure(bg=theme['bg_secondary'])
                def on_leave(e):
                    button.configure(bg=theme['toolbar_bg'])
                button.bind('<Enter>', on_enter)
                button.bind('<Leave>', on_leave)
            
            create_hover_effect(btn)
    
    def create_tab_area(self):
        theme = THEMES[current_theme]
        
        # タブコンテナ
        self.tab_frame = tk.Frame(self.main_frame, bg=theme['bg'], height=30)
        self.tab_frame.pack(fill=tk.X, padx=0, pady=0)
        self.tab_frame.pack_propagate(False)
        
        # タブボタンコンテナ
        self.tab_buttons_frame = tk.Frame(self.tab_frame, bg=theme['bg'])
        self.tab_buttons_frame.pack(fill=tk.X, side=tk.LEFT)
        
        # 新規タブボタン
        self.new_tab_btn = tk.Button(
            self.tab_frame,
            text="+",
            command=self.new_tab,
            font=(system_fonts['ui_font'], 12, 'bold'),
            bg=theme['tab_bg'],
            fg=theme['tab_fg'],
            relief=tk.FLAT,
            borderwidth=0,
            padx=8,
            pady=2,
            cursor='hand2'
        )
        self.new_tab_btn.pack(side=tk.RIGHT, padx=5, pady=3)
        
        # エディタコンテナ
        self.editor_container = tk.Frame(self.main_frame, bg=theme['bg'])
        self.editor_container.pack(fill=tk.BOTH, expand=True)
        
        # 初期タブを作成
        self.new_tab()
    
    def create_status_bar(self):
        theme = THEMES[current_theme]
        
        self.status_bar = tk.Frame(self.main_frame, bg=theme['status_bar_bg'], height=25)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        self.status_bar.pack_propagate(False)
        
        self.status_label = tk.Label(
            self.status_bar,
            text=t('ready'),
            bg=theme['status_bar_bg'],
            fg=theme['status_bar_fg'],
            font=(system_fonts['ui_font'], 9),
            anchor='w'
        )
        self.status_label.pack(side=tk.LEFT, padx=10, pady=2)
        
        # 位置インジケーター
        self.position_label = tk.Label(
            self.status_bar,
            text="行 1, 列 1",
            bg=theme['status_bar_bg'],
            fg=theme['status_bar_fg'],
            font=(system_fonts['ui_font'], 9),
            anchor='e'
        )
        self.position_label.pack(side=tk.RIGHT, padx=10, pady=2)
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # ファイルメニュー
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label=t('new'), command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label=t('open'), command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label=t('save'), command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label=t('save_as'), command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label=t('exit'), command=self.exit_app)
        menubar.add_cascade(label=t('file'), menu=file_menu)
        
        # 編集メニュー
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label=t('undo'), command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label=t('redo'), command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label=t('cut'), command=self.cut_text, accelerator="Ctrl+X")
        edit_menu.add_command(label=t('copy'), command=self.copy_text, accelerator="Ctrl+C")
        edit_menu.add_command(label=t('paste'), command=self.paste_text, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label=t('find'), command=self.show_find_dialog, accelerator="Ctrl+F")
        edit_menu.add_command(label=t('replace'), command=self.show_replace_dialog, accelerator="Ctrl+H")
        menubar.add_cascade(label=t('edit'), menu=edit_menu)
        
        # 表示メニュー
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label=t('toggle_theme'), command=self.toggle_theme, accelerator="Ctrl+T")
        view_menu.add_command(label=t('zoom_in'), command=self.zoom_in, accelerator="Ctrl++")
        view_menu.add_command(label=t('zoom_out'), command=self.zoom_out, accelerator="Ctrl+-")
        menubar.add_cascade(label=t('view'), menu=view_menu)
        
        # ツールメニュー
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label=t('format_code'), command=self.format_code)
        tools_menu.add_command(label=t('syntax_check'), command=self.check_syntax)
        tools_menu.add_command(label=t('auto_fix'), command=self.auto_fix)
        tools_menu.add_command(label=t('run'), command=self.run_code, accelerator="F5")
        menubar.add_cascade(label=t('tools'), menu=tools_menu)
        
        # ヘルプメニュー
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label=t('about'), command=self.show_about)
        menubar.add_cascade(label="ヘルプ", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def bind_shortcuts(self):
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-x>', lambda e: self.cut_text())
        self.root.bind('<Control-c>', lambda e: self.copy_text())
        self.root.bind('<Control-v>', lambda e: self.paste_text())
        self.root.bind('<Control-z>', lambda e: self.undo())
        self.root.bind('<Control-y>', lambda e: self.redo())
        self.root.bind('<Control-f>', lambda e: self.show_find_dialog())
        self.root.bind('<Control-h>', lambda e: self.show_replace_dialog())
        self.root.bind('<Control-t>', lambda e: self.toggle_theme())
        self.root.bind('<Control-plus>', lambda e: self.zoom_in())
        self.root.bind('<Control-equal>', lambda e: self.zoom_in())
        self.root.bind('<Control-minus>', lambda e: self.zoom_out())
        self.root.bind('<F5>', lambda e: self.run_code())
    
    def new_tab(self, file_path=None, content=""):
        global active_tab
        
        # 新規タブを作成
        tab_id = len(open_tabs)
        tab = ModernTab(self.editor_container, file_path, content)
        open_tabs.append(tab)
        
        # タブボタンを作成
        theme = THEMES[current_theme]
        tab_button = tk.Button(
            self.tab_buttons_frame,
            text=self.get_tab_title(tab),
            command=lambda t=tab: self.switch_to_tab(t),
            font=(system_fonts['ui_font'], 10),
            bg=theme['tab_bg'],
            fg=theme['tab_fg'],
            relief=tk.FLAT,
            borderwidth=1,
            padx=10,
            pady=3,
            cursor='hand2'
        )
        tab_button.pack(side=tk.LEFT, padx=1)
        
        tab.button = tab_button
        
        # 新規タブに切り替え
        self.switch_to_tab(tab)
        
        return tab
    
    def switch_to_tab(self, tab):
        global active_tab
        
        # 現在のタブを非表示
        if active_tab:
            active_tab.text.pack_forget()
            active_tab.line_numbers.pack_forget()
            active_tab.button.configure(
                bg=THEMES[current_theme]['tab_bg'],
                fg=THEMES[current_theme]['tab_fg']
            )
        
        # 新規タブを表示
        tab.line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        tab.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tab.button.configure(
            bg=THEMES[current_theme]['tab_active_bg'],
            fg=THEMES[current_theme]['tab_fg']
        )
        
        active_tab = tab
        self.update_status()
    
    def get_tab_title(self, tab):
        if tab.file_path:
            title = os.path.basename(tab.file_path)
            if tab.modified:
                title += " ●"
            return title
        else:
            return t('unsaved') if tab.modified else "無題"
    
    def update_tab_title(self, tab):
        if tab.button:
            tab.button.configure(text=self.get_tab_title(tab))
    
    def new_file(self):
        self.new_tab()
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            title=t('open'),
            filetypes=[
                (t('python_files'), "*.py *.pyw"),
                ("JavaScriptファイル", "*.js"),
                ("TypeScriptファイル", "*.ts"),
                ("HTMLファイル", "*.html *.htm"),
                ("CSSファイル", "*.css"),
                ("JSONファイル", "*.json"),
                ("XMLファイル", "*.xml"),
                ("Markdownファイル", "*.md"),
                ("すべてのファイル", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # ファイルが既に開かれているかチェック
                for tab in open_tabs:
                    if tab.file_path == file_path:
                        self.switch_to_tab(tab)
                        return
                
                # 最近のファイルに追加
                if file_path in recent_files:
                    recent_files.remove(file_path)
                recent_files.insert(0, file_path)
                self.save_recent_files()
                
                # ファイル内容で新規タブを作成
                self.new_tab(file_path, content)
                
            except Exception as e:
                messagebox.showerror(t('error'), f"{t('file_not_saved')}: {e}")
    
    def save_file(self):
        if not active_tab:
            return
        
        if active_tab.file_path:
            try:
                with open(active_tab.file_path, 'w', encoding='utf-8') as file:
                    file.write(active_tab.get_content())
                
                active_tab.modified = False
                active_tab.original_content = active_tab.get_content()
                self.update_tab_title(active_tab)
                self.update_status()
                messagebox.showinfo(t('success'), t('file_saved'))
                
            except Exception as e:
                messagebox.showerror(t('error'), f"{t('file_not_saved')}: {e}")
        else:
            self.save_as()
    
    def save_as(self):
        if not active_tab:
            return
        
        file_path = filedialog.asksaveasfilename(
            title=t('save_as'),
            defaultextension=".py",
            filetypes=[
                (t('python_files'), "*.py"),
                ("JavaScriptファイル", "*.js"),
                ("TypeScriptファイル", "*.ts"),
                ("HTMLファイル", "*.html"),
                ("CSSファイル", "*.css"),
                ("JSONファイル", "*.json"),
                ("すべてのファイル", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(active_tab.get_content())
                
                active_tab.file_path = file_path
                active_tab.modified = False
                active_tab.original_content = active_tab.get_content()
                self.update_tab_title(active_tab)
                self.update_status()
                
                # 最近のファイルに追加
                if file_path in recent_files:
                    recent_files.remove(file_path)
                recent_files.insert(0, file_path)
                self.save_recent_files()
                
                messagebox.showinfo(t('success'), t('file_saved'))
                
            except Exception as e:
                messagebox.showerror(t('error'), f"{t('file_not_saved')}: {e}")
    
    def cut_text(self):
        if active_tab:
            try:
                selected = active_tab.text.get(tk.SEL_FIRST, tk.SEL_LAST)
                self.root.clipboard_clear()
                self.root.clipboard_append(selected)
                active_tab.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
            except:
                pass
    
    def copy_text(self):
        if active_tab:
            try:
                selected = active_tab.text.get(tk.SEL_FIRST, tk.SEL_LAST)
                self.root.clipboard_clear()
                self.root.clipboard_append(selected)
                messagebox.showinfo(t('success'), t('copy_success'))
            except:
                messagebox.showwarning(t('warning'), t('no_selection'))
    
    def paste_text(self):
        if active_tab:
            try:
                clipboard_content = self.root.clipboard_get()
                active_tab.text.insert(tk.INSERT, clipboard_content)
            except:
                pass
    
    def undo(self):
        if active_tab:
            try:
                active_tab.text.edit_undo()
            except:
                pass
    
    def redo(self):
        if active_tab:
            try:
                active_tab.text.edit_redo()
            except:
                pass
    
    def zoom_in(self):
        global current_font_size
        current_font_size += 2
        self.update_font_size()
    
    def zoom_out(self):
        global current_font_size
        if current_font_size > 8:
            current_font_size -= 2
            self.update_font_size()
    
    def update_font_size(self):
        for tab in open_tabs:
            tab.text.configure(font=(system_fonts['text_font'], current_font_size))
            tab.line_numbers.configure(font=(system_fonts['text_font'], current_font_size))
            tab.update_line_numbers()
    
    def toggle_theme(self):
        global current_theme
        current_theme = 'light' if current_theme == 'dark' else 'dark'
        self.apply_theme()
        self.save_settings()
    
    def apply_theme(self):
        theme = THEMES[current_theme]
        
        # メインウィンドウを更新
        self.root.configure(bg=theme['bg'])
        
        # すべてのフレームを更新
        self.main_frame.configure(bg=theme['bg'])
        self.toolbar.configure(bg=theme['toolbar_bg'])
        self.tab_frame.configure(bg=theme['bg'])
        self.tab_buttons_frame.configure(bg=theme['bg'])
        self.editor_container.configure(bg=theme['bg'])
        self.status_bar.configure(bg=theme['status_bar_bg'])
        
        # ラベルを更新
        self.status_label.configure(bg=theme['status_bar_bg'], fg=theme['status_bar_fg'])
        self.position_label.configure(bg=theme['status_bar_bg'], fg=theme['status_bar_fg'])
        
        # タブを更新
        for tab in open_tabs:
            if tab.text:
                tab.text.configure(bg=theme['text_bg'], fg=theme['fg'])
                tab.line_numbers.configure(bg=theme['line_numbers_bg'], fg=theme['line_numbers_fg'])
            
            if tab.button:
                if tab == active_tab:
                    tab.button.configure(bg=theme['tab_active_bg'], fg=theme['tab_fg'])
                else:
                    tab.button.configure(bg=theme['tab_bg'], fg=theme['tab_fg'])
        
        # 新規タブボタンを更新
        self.new_tab_btn.configure(bg=theme['tab_bg'], fg=theme['tab_fg'])
        
        # ツールバーボタンを更新
        for widget in self.toolbar.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=theme['toolbar_bg'], fg=theme['fg'])
    
    def show_find_dialog(self):
        # 簡単な検索ダイアログ実装
        dialog = tk.Toplevel(self.root)
        dialog.title(t('find'))
        dialog.geometry("400x150")
        dialog.resizable(False, False)
        
        theme = THEMES[current_theme]
        dialog.configure(bg=theme['bg'])
        
        # Main frame with padding
        main_frame = tk.Frame(dialog, bg=theme['bg'])
        main_frame.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text=t('search'), bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10)).pack(pady=5)
        
        entry = tk.Entry(main_frame, font=(system_fonts['ui_font'], 10))
        entry.pack(pady=5, fill=tk.X)
        entry.focus_set()
        
        def find_next():
            search_term = entry.get()
            if search_term and active_tab:
                # 簡単な検索実装
                content = active_tab.text.get("1.0", tk.END)
                pos = active_tab.text.search(search_term, "insert", tk.END)
                if pos:
                    active_tab.text.mark_set(tk.INSERT, pos)
                    active_tab.text.see(pos)
                else:
                    messagebox.showinfo(t('info'), t('search_not_found'))
        
        button_frame = tk.Frame(main_frame, bg=theme['bg'])
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text=t('find_next'), command=find_next, 
                 bg=theme['accent'], fg='white', font=(system_fonts['ui_font'], 9),
                 padx=15, pady=5).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=t('close'), command=dialog.destroy,
                 bg=theme['bg_secondary'], fg=theme['fg'], font=(system_fonts['ui_font'], 9),
                 padx=15, pady=5).pack(side=tk.LEFT, padx=5)
    
    def show_replace_dialog(self):
        # 簡単な置換ダイアログ実装
        dialog = tk.Toplevel(self.root)
        dialog.title(t('replace'))
        dialog.geometry("450x200")
        dialog.resizable(False, False)
        
        theme = THEMES[current_theme]
        dialog.configure(bg=theme['bg'])
        
        # Main frame with padding
        main_frame = tk.Frame(dialog, bg=theme['bg'])
        main_frame.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)
        
        tk.Label(main_frame, text=t('find'), bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10)).pack(pady=5)
        find_entry = tk.Entry(main_frame, font=(system_fonts['ui_font'], 10))
        find_entry.pack(pady=5, fill=tk.X)
        
        tk.Label(main_frame, text=t('replace'), bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10)).pack(pady=5)
        replace_entry = tk.Entry(main_frame, font=(system_fonts['ui_font'], 10))
        replace_entry.pack(pady=5, fill=tk.X)
        
        def replace_all():
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            if find_text and active_tab:
                content = active_tab.text.get("1.0", tk.END)
                new_content = content.replace(find_text, replace_text)
                active_tab.text.delete("1.0", tk.END)
                active_tab.text.insert("1.0", new_content)
                count = content.count(find_text)
                messagebox.showinfo(t('success'), f"{count} {t('replace_count')}")
        
        button_frame = tk.Frame(main_frame, bg=theme['bg'])
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text=t('replace_all'), command=replace_all,
                 bg=theme['accent'], fg='white', font=(system_fonts['ui_font'], 9),
                 padx=15, pady=5).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=t('close'), command=dialog.destroy,
                 bg=theme['bg_secondary'], fg=theme['fg'], font=(system_fonts['ui_font'], 9),
                 padx=15, pady=5).pack(side=tk.LEFT, padx=5)
    
    def format_code(self):
        if not active_tab:
            return
        
        try:
            content = active_tab.get_content()
            # 基本的なPython整形
            lines = content.split('\n')
            formatted_lines = []
            indent_level = 0
            
            for line in lines:
                stripped = line.strip()
                
                if stripped.startswith(('elif ', 'else:', 'except ', 'finally:')):
                    indent_level = max(0, indent_level - 1)
                
                formatted_line = '    ' * indent_level + stripped
                formatted_lines.append(formatted_line)
                
                if stripped.endswith(':') and not stripped.startswith('#'):
                    indent_level += 1
                
                if stripped in ('pass', 'break', 'continue', 'return'):
                    indent_level = max(0, indent_level - 1)
            
            formatted_code = '\n'.join(formatted_lines)
            active_tab.set_content(formatted_code)
            messagebox.showinfo(t('success'), t('format_complete'))
            
        except Exception as e:
            messagebox.showerror(t('error'), f"{t('format_failed')}: {e}")
    
    def check_syntax(self):
        if not active_tab:
            return
        
        try:
            content = active_tab.get_content()
            compile(content, '<string>', 'exec')
            messagebox.showinfo(t('success'), t('syntax_ok'))
        except SyntaxError as e:
            messagebox.showerror(t('error'), f"{t('syntax_error')}: {e}")
    
    def auto_fix(self):
        if not active_tab:
            return
        
        try:
            content = active_tab.get_content()
            original_code = content
            fixed = False
            
            # 一般的な修正
            fixes = [
                (r'print\s*\(', lambda m: "print(", "Print関数の修正"),
                (r':\n(?!\s)', r":\n    ", "インデント修正"),
                (r'(\w+)\s*;\s*$', r"\1", "セミコロンを削除"),
            ]
            
            for pattern, replacement, description in fixes:
                if callable(replacement):
                    new_code = re.sub(pattern, replacement, content, flags=re.MULTILINE)
                else:
                    new_code = re.sub(pattern, replacement, content, flags=re.MULTILINE)
                
                if new_code != content:
                    content = new_code
                    fixed = True
            
            if fixed:
                active_tab.set_content(content)
                messagebox.showinfo(t('success'), t('auto_fix_complete'))
            else:
                messagebox.showinfo(t('info'), t('auto_fix_none'))
                
        except Exception as e:
            messagebox.showerror(t('error'), f"{t('auto_fix_failed')}: {e}")
    
    def run_code(self):
        if not active_tab:
            return
        
        try:
            code = active_tab.get_content()
            
            # 一時ファイルに保存
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8')
            temp_file.write(code)
            temp_file.close()
            
            # 別スレッドで実行
            def run_in_thread():
                try:
                    result = subprocess.run(
                        [sys.executable, temp_file.name],
                        capture_output=True,
                        text=True,
                        timeout=30
                    )
                    
                    # 出力を表示
                    output_window = tk.Toplevel(self.root)
                    output_window.title("出力")
                    output_window.geometry("600x400")
                    
                    theme = THEMES[current_theme]
                    output_window.configure(bg=theme['bg'])
                    
                    text_widget = tk.Text(output_window, bg=theme['text_bg'], fg=theme['fg'],
                                        font=(system_fonts['text_font'], 10))
                    text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                    
                    if result.stdout:
                        text_widget.insert(tk.END, f"出力:\n{result.stdout}\n")
                    if result.stderr:
                        text_widget.insert(tk.END, f"エラー:\n{result.stderr}\n")
                        # エラー解析ダイアログを表示
                        self.show_error_dialog(result.stderr, active_tab.get_content(), active_tab)
                    
                    # 自動終了機能
                    auto_close_setting = getattr(self, 'auto_close_setting', 'never')
                    if auto_close_setting != 'never':
                        close_delay = int(auto_close_setting) * 1000  # ミリ秒に変換
                        output_window.after(close_delay, output_window.destroy)
                    
                    # 一時ファイルをクリーンアップ
                    os.unlink(temp_file.name)
                    
                except Exception as e:
                    messagebox.showerror(t('error'), f"{t('run_failed')}: {e}")
            
            Thread(target=run_in_thread, daemon=True).start()
            
        except Exception as e:
            messagebox.showerror(t('error'), f"{t('run_failed')}: {e}")
    
    def parse_imports(self, code):
        """Pythonコードを解析してimport文を抽出"""
        imports = set()
        
        # 異なるimportパターンの正規表現
        patterns = [
            r'^import\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)',  # import module
            r'^from\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)\s+import',  # from module import
        ]
        
        for line in code.split('\n'):
            line = line.strip()
            if line.startswith('#') or not line:
                continue
                
            for pattern in patterns:
                match = re.match(pattern, line)
                if match:
                    module_name = match.group(1)
                    # トップレベルパッケージ名を取得
                    top_level = module_name.split('.')[0]
                    # 標準ライブラリモジュールをスキップ
                    if top_level not in self.get_stdlib_modules():
                        imports.add(top_level)
                    break
        
        return list(imports)
    
    def get_stdlib_modules(self):
        """スキップする標準ライブラリモジュールのリスト"""
        return {
            'os', 'sys', 're', 'json', 'time', 'datetime', 'math', 'random',
            'collections', 'itertools', 'functools', 'operator', 'pathlib',
            'urllib', 'http', 'email', 'html', 'xml', 'sqlite3', 'csv',
            'configparser', 'logging', 'unittest', 'argparse', 'subprocess',
            'threading', 'multiprocessing', 'socket', 'ssl', 'hashlib',
            'hmac', 'base64', 'uuid', 'tempfile', 'shutil', 'glob',
            'fnmatch', 'pickle', 'struct', 'array', 'bisect', 'heapq',
            'queue', 'weakref', 'copy', 'pprint', 'repr', 'stringio',
            'io', 'fractions', 'decimal', 'statistics', 'enum',
            'typing', 'contextlib', 'abc', 'inspect', 'dis', 'importlib',
            'pkgutil', 'modulefinder', 'runpy', 'site', 'user',
            'platform', 'locale', 'codecs', 'encodings', 'textwrap',
            'unicodedata', 'stringprep', 'readline', 'rlcompleter',
            'cmd', 'shlex', 'tokenize', 'keyword', 'token', 'ast',
            'symbol', 'parser', 'py_compile', 'compileall', 'distutils',
            'ensurepip', 'venv', 'zipapp', 'msvcrt', 'winsound',
            'posix', 'pwd', 'spwd', 'grp', 'crypt', 'termios', 'tty',
            'pty', 'fcntl', 'pipes', 'resource', 'nis', 'syslog',
            'select', 'selectors', 'signal', 'mmap', 'ctypes',
            'curses', 'turtle', 'tkinter', 'idlelib', 'test',
            'webbrowser', 'mailcap', 'mailbox', 'mimetypes', 'uu',
            'xdrlib', 'imaplib', 'poplib', 'smtplib', 'nntplib',
            'telnetlib', 'ftplib', 'gzip', 'bz2', 'lzma', 'zipfile',
            'tarfile', 'shelve', 'dbm', 'sqlite3', 'decimal',
            'fractions', 'statistics', 'queue', 'asyncio',
            'concurrent', 'multiprocessing', 'socketserver',
            'http', 'urllib', 'email', 'xml', 'html', 'websockets',
            'wsgiref', 'xmlrpc', 'ipaddress', 'ssl', 'hashlib',
            'hmac', 'secrets', 'uuid', 'base64', 'binascii',
            'quopri', 'uu', 'xdrlib', 'struct', 'code', 'codeop',
            'dis', 'pickletools', 'marshal', 'importlib', 'pkgutil',
            'modulefinder', 'runpy', 'parser', 'ast', 'symbol',
            'token', 'keyword', 'tokenize', 'tabnanny', 'pyclbr',
            'py_compile', 'compileall', 'distutils', 'ensurepip',
            'venv', 'zipapp', 'site', 'user', 'pydoc', 'doctest',
            'unittest', 'test', 'bdb', 'pdb', 'profile', 'pstats',
            'timeit', 'trace', 'tracemalloc', 'gc', 'weakref',
            'copy', 'copyreg', 'pprint', 'repr', 'enum', 'types',
            'dataclasses', 'typing', 'contextlib', 'abc', 'atexit',
            'traceback', 'faulthandler', 'sysconfig', 'platform',
            'errno', 'stat', 'filecmp', 'fileinput', 'glob',
            'fnmatch', 'linecache', 'shutil', 'tempfile', 'glob',
            'os', 'os.path', 'time', 'argparse', 'getopt', 'logging',
            'getpass', 'curses', 'platform', 'errno', 'ctypes'
        }
    
    def install_module(self):
        """コードから自動的にPythonモジュールをインストール"""
        dialog = tk.Toplevel(self.root)
        dialog.title("自動モジュールインストーラー")
        dialog.geometry("600x500")
        dialog.transient(self.root)
        dialog.grab_set()
        
        theme = THEMES[current_theme]
        dialog.configure(bg=theme['bg'])
        
        # Main frame with padding
        main_frame = tk.Frame(dialog, bg=theme['bg'])
        main_frame.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)
        
        # Title
        tk.Label(main_frame, text="🔍 自動モジュール検出とインストール", 
                bg=theme['bg'], fg=theme['fg'], 
                font=(system_fonts['ui_font'], 14, 'bold')).pack(pady=10)
        
        tk.Label(main_frame, text="コード内の不足モジュールをスキャン中...", 
                bg=theme['bg'], fg=theme['fg'], 
                font=(system_fonts['ui_font'], 12)).pack(pady=5)
        
        # 自動モード - 検出されたモジュールリスト
        auto_frame = tk.Frame(main_frame, bg=theme['bg'])
        auto_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        tk.Label(auto_frame, text="📦 インストール対象モジュール:", bg=theme['bg'], fg=theme['fg'], 
                font=(system_fonts['ui_font'], 12, 'bold')).pack(anchor=tk.W)
        
        # 検出されたモジュールのリストボックス
        list_frame = tk.Frame(auto_frame, bg=theme['bg'])
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        modules_listbox = tk.Listbox(list_frame, font=(system_fonts['ui_font'], 11),
                                    bg=theme['bg_secondary'], fg=theme['fg'],
                                    yscrollcommand=scrollbar.set, selectmode=tk.MULTIPLE)
        modules_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=modules_listbox.yview)
        
        # 保存済み仮想環境設定を読み込み
        venv_settings = self.load_venv_settings()
        
        # 仮想環境設定
        venv_frame = tk.Frame(main_frame, bg=theme['bg'])
        venv_frame.pack(pady=10, padx=15, fill=tk.X)
        
        use_venv = tk.BooleanVar(value=True)
        venv_check = tk.Checkbutton(venv_frame, text="🐍 仮想環境を使用", 
                                   variable=use_venv, bg=theme['bg'], fg=theme['fg'],
                                   font=(system_fonts['ui_font'], 11))
        venv_check.pack(anchor=tk.W, pady=5)
        
        # 仮想環境パス設定
        path_frame = tk.Frame(venv_frame, bg=theme['bg'])
        path_frame.pack(fill=tk.X, pady=8)
        
        use_custom_path = tk.BooleanVar(value=venv_settings.get('use_custom_path', False))
        custom_check = tk.Checkbutton(path_frame, text="📁 カスタムパス:", 
                                     variable=use_custom_path, bg=theme['bg'], fg=theme['fg'],
                                     font=(system_fonts['ui_font'], 10))
        custom_check.pack(side=tk.LEFT, padx=(0, 10))
        
        venv_path_var = tk.StringVar(value=venv_settings.get('venv_path', '.venv'))
        venv_path_entry = tk.Entry(path_frame, textvariable=venv_path_var, 
                                  font=(system_fonts['ui_font'], 10),
                                  bg=theme['bg_secondary'], fg=theme['fg'])
        venv_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        browse_btn = tk.Button(path_frame, text="📂 参照", 
                             command=lambda: self.browse_venv_path(venv_path_var),
                             bg=theme['bg_secondary'], fg=theme['fg'],
                             font=(system_fonts['ui_font'], 9))
        browse_btn.pack(side=tk.RIGHT)
        
        # ステータスラベル
        status_label = tk.Label(main_frame, text="", bg=theme['bg'], fg=theme['fg_secondary'],
                               font=(system_fonts['ui_font'], 11), wraplength=500)
        status_label.pack(pady=8, padx=15, fill=tk.X)
        
        def detect_modules():
            if not active_tab:
                modules_listbox.delete(0, tk.END)
                status_label.configure(text="📄 解析するコードファイルがありません")
                return
            
            code = active_tab.get_content()
            modules = self.parse_imports(code)
            modules_listbox.delete(0, tk.END)
            
            if modules:
                for module in modules:
                    modules_listbox.insert(tk.END, module)
                status_label.configure(text=f"✅ {len(modules)}個のモジュールを検出しました")
            else:
                status_label.configure(text="ℹ️ 外部モジュールは検出されませんでした")
        
        def install():
            selected_indices = modules_listbox.curselection()
            if not selected_indices:
                status_label.configure(text="⚠️ インストールするモジュールを選択してください")
                return
            
            modules_to_install = [modules_listbox.get(i) for i in selected_indices]
            status_label.configure(text="🔄 インストール中...")
            dialog.update()
            
            def install_in_thread():
                try:
                    if use_venv.get():
                        # 仮想環境パスを取得
                        if use_custom_path.get():
                            venv_path = venv_path_var.get()
                            if not os.path.isabs(venv_path):
                                venv_path = os.path.join(os.getcwd(), venv_path)
                        else:
                            venv_path = os.path.join(os.getcwd(), ".venv")
                        
                        # 設定を保存
                        self.save_venv_settings(venv_path_var.get(), use_custom_path.get())
                        
                        # 仮想環境が存在しない場合は作成
                        if not os.path.exists(venv_path):
                            status_label.configure(text=f"{venv_path} に仮想環境を作成中...")
                            dialog.update()
                            subprocess.run([sys.executable, "-m", "venv", venv_path], 
                                         check=True, capture_output=True)
                        
                        # 仮想環境のpipパスを取得
                        if os.name == 'nt':  # Windows
                            pip_path = os.path.join(venv_path, "Scripts", "pip")
                        else:  # Unix
                            pip_path = os.path.join(venv_path, "bin", "pip")
                        
                        # 仮想環境にモジュールをインストール
                        for module in modules_to_install:
                            status_label.configure(text=f"{module} を {venv_path} にインストール中...")
                            dialog.update()
                            result = subprocess.run([pip_path, "install", module], 
                                                  capture_output=True, text=True, timeout=300)
                            if result.returncode != 0:
                                error_msg = f"❌ {module} のインストール失敗: {result.stderr}"
                                status_label.configure(text=error_msg)
                                # エラー用コピーを追加
                                error_frame = tk.Frame(dialog, bg=theme['bg'])
                                error_frame.pack(pady=5, padx=20, fill=tk.X)
                                
                                tk.Label(error_frame, text="エラーが発生:", 
                                        bg=theme['bg'], fg=theme['fg'],
                                        font=(system_fonts['ui_font'], 9)).pack(side=tk.LEFT)
                                
                                copy_btn = tk.Button(error_frame, text="📋 コピー", 
                                                  command=lambda: self.copy_to_clipboard(error_msg),
                                                  bg=theme['bg_secondary'], fg=theme['fg'],
                                                  font=(system_fonts['ui_font'], 10))
                                copy_btn.pack(side=tk.RIGHT, padx=5)
                                return
                    else:
                        # 現在の環境にインストール
                        for module in modules_to_install:
                            status_label.configure(text=f"{module} をインストール中...")
                            dialog.update()
                            result = subprocess.run([sys.executable, "-m", "pip", "install", module], 
                                                  capture_output=True, text=True, timeout=300)
                            if result.returncode != 0:
                                error_msg = f"❌ {module} のインストール失敗: {result.stderr}"
                                status_label.configure(text=error_msg)
                                # エラー用コピーを追加
                                error_frame = tk.Frame(dialog, bg=theme['bg'])
                                error_frame.pack(pady=5, padx=20, fill=tk.X)
                                
                                tk.Label(error_frame, text="エラーが発生:", 
                                        bg=theme['bg'], fg=theme['fg'],
                                        font=(system_fonts['ui_font'], 9)).pack(side=tk.LEFT)
                                
                                copy_btn = tk.Button(error_frame, text="📋 コピー", 
                                                  command=lambda: self.copy_to_clipboard(error_msg),
                                                  bg=theme['bg_secondary'], fg=theme['fg'],
                                                  font=(system_fonts['ui_font'], 10))
                                copy_btn.pack(side=tk.RIGHT, padx=5)
                                return
                    
                    status_label.configure(text=f"✅ 正常にインストール完了: {', '.join(modules_to_install)}")
                        
                except subprocess.TimeoutExpired:
                    error_msg = "❌ インストールがタイムアウトしました"
                    status_label.configure(text=error_msg)
                    # タイムアウトエラー用コピーを追加
                    error_frame = tk.Frame(dialog, bg=theme['bg'])
                    error_frame.pack(pady=5, padx=20, fill=tk.X)
                    
                    tk.Label(error_frame, text="タイムアウト:", 
                            bg=theme['bg'], fg=theme['fg'],
                            font=(system_fonts['ui_font'], 9)).pack(side=tk.LEFT)
                    
                    copy_btn = tk.Button(error_frame, text="📋 コピー", 
                                      command=lambda: self.copy_to_clipboard(error_msg),
                                      bg=theme['bg_secondary'], fg=theme['fg'],
                                      font=(system_fonts['ui_font'], 10))
                    copy_btn.pack(side=tk.RIGHT, padx=5)
                except Exception as e:
                    error_msg = f"❌ エラー: {str(e)}"
                    status_label.configure(text=error_msg)
                    # 一般エラー用コピーを追加
                    error_frame = tk.Frame(dialog, bg=theme['bg'])
                    error_frame.pack(pady=5, padx=20, fill=tk.X)
                    
                    tk.Label(error_frame, text="一般エラー:", 
                            bg=theme['bg'], fg=theme['fg'],
                            font=(system_fonts['ui_font'], 9)).pack(side=tk.LEFT)
                    
                    copy_btn = tk.Button(error_frame, text="📋 コピー", 
                                      command=lambda: self.copy_to_clipboard(error_msg),
                                      bg=theme['bg_secondary'], fg=theme['fg'],
                                      font=(system_fonts['ui_font'], 10))
                    copy_btn.pack(side=tk.RIGHT, padx=5)
            
            # 別スレッドでインストールを実行
            threading.Thread(target=install_in_thread, daemon=True).start()
        
        # 自動的にモジュールを検出
        detect_modules()
        
        # ボタン
        button_frame = tk.Frame(main_frame, bg=theme['bg'])
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="🚀 選択したものをインストール", command=install,
                 bg=theme['accent'], fg='white', font=(system_fonts['ui_font'], 11, 'bold'),
                 padx=20, pady=8).pack(side=tk.LEFT, padx=8)
        
        tk.Button(button_frame, text="🔄 更新", command=detect_modules,
                 bg=theme['bg_secondary'], fg=theme['fg'], font=(system_fonts['ui_font'], 11),
                 padx=20, pady=8).pack(side=tk.LEFT, padx=8)
        
        tk.Button(button_frame, text="❌ 閉じる", command=dialog.destroy,
                 bg=theme['bg_secondary'], fg=theme['fg'], font=(system_fonts['ui_font'], 11),
                 padx=20, pady=8).pack(side=tk.LEFT, padx=8)
        
        # Enterキーをインストールにバインド
        dialog.bind('<Return>', lambda e: install())
    
    def show_settings(self):
        # 設定ダイアログ実装
        dialog = tk.Toplevel(self.root)
        dialog.title(t('settings'))
        dialog.geometry("450x400")
        dialog.resizable(False, False)
        
        theme = THEMES[current_theme]
        dialog.configure(bg=theme['bg'])
        
        # Main frame with padding
        main_frame = tk.Frame(dialog, bg=theme['bg'])
        main_frame.pack(pady=10, padx=15, fill=tk.BOTH, expand=True)
        
        # テーマ選択
        tk.Label(main_frame, text=t('theme'), bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10)).pack(pady=10)
        
        theme_var = tk.StringVar(value=current_theme)
        tk.Radiobutton(main_frame, text=t('dark_theme'), variable=theme_var, value='dark',
                     bg=theme['bg'], fg=theme['fg'], selectcolor=theme['fg']).pack()
        tk.Radiobutton(main_frame, text=t('light_theme'), variable=theme_var, value='light',
                     bg=theme['bg'], fg=theme['fg'], selectcolor=theme['fg']).pack()
        
        # フォントサイズ
        tk.Label(main_frame, text=t('font_size'), bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10)).pack(pady=10)
        
        font_var = tk.IntVar(value=current_font_size)
        tk.Spinbox(main_frame, from_=8, to=32, textvariable=font_var,
                  font=(system_fonts['ui_font'], 10)).pack()
        
        # 実行後自動終了
        tk.Label(main_frame, text="実行後自動終了", bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10)).pack(pady=10)
        
        auto_close_var = tk.StringVar(value=getattr(self, 'auto_close_setting', 'never'))
        
        tk.Radiobutton(main_frame, text="閉じない", variable=auto_close_var, value='never',
                     bg=theme['bg'], fg=theme['fg'], selectcolor=theme['fg']).pack()
        tk.Radiobutton(main_frame, text="5秒後に閉じる", variable=auto_close_var, value='5',
                     bg=theme['bg'], fg=theme['fg'], selectcolor=theme['fg']).pack()
        tk.Radiobutton(main_frame, text="10秒後に閉じる", variable=auto_close_var, value='10',
                     bg=theme['bg'], fg=theme['fg'], selectcolor=theme['fg']).pack()
        
        def apply_settings():
            global current_theme, current_font_size
            current_theme = theme_var.get()
            current_font_size = font_var.get()
            self.auto_close_setting = auto_close_var.get()
            self.apply_theme()
            self.update_font_size()
            self.save_settings()
            dialog.destroy()
            messagebox.showinfo(t('success'), t('settings_saved'))
        
        button_frame = tk.Frame(main_frame, bg=theme['bg'])
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text=t('ok'), command=apply_settings,
                 bg=theme['accent'], fg='white', font=(system_fonts['ui_font'], 9),
                 padx=15, pady=5).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=t('cancel'), command=dialog.destroy,
                 bg=theme['bg_secondary'], fg=theme['fg'], font=(system_fonts['ui_font'], 9),
                 padx=15, pady=5).pack(side=tk.LEFT, padx=5)
    
    def show_about(self):
        messagebox.showinfo(t('about_title'), t('about_text'))
    
    def update_status(self):
        if active_tab:
            # 位置を更新
            try:
                cursor_pos = active_tab.text.index(tk.INSERT)
                line, col = cursor_pos.split('.')
                if hasattr(self, 'position_label'):
                    self.position_label.configure(text=f"行 {line}, 列 {col}")
            except:
                if hasattr(self, 'position_label'):
                    self.position_label.configure(text="行 1, 列 1")
            
            # ステータスを更新
            if hasattr(self, 'status_label'):
                if active_tab.modified:
                    self.status_label.configure(text=f"{t('modified')} - {self.get_tab_title(active_tab)}")
                else:
                    self.status_label.configure(text=self.get_tab_title(active_tab))
        else:
            if hasattr(self, 'status_label'):
                self.status_label.configure(text=t('ready'))
            if hasattr(self, 'position_label'):
                self.position_label.configure(text="行 1, 列 1")
    
    def exit_app(self):
        # 保存されていない変更をチェック
        unsaved_tabs = [tab for tab in open_tabs if tab.modified]
        if unsaved_tabs:
            response = messagebox.askyesnocancel(t('confirm'), t('confirm_close'))
            if response is None:  # キャンセル
                return
            elif response:  # はい
                for tab in unsaved_tabs:
                    if tab.file_path:
                        try:
                            with open(tab.file_path, 'w', encoding='utf-8') as file:
                                file.write(tab.get_content())
                        except:
                            pass
        
        self.save_settings()
        self.root.quit()
    
    def load_settings(self):
        global current_theme, current_font_size, recent_files
        
        try:
            if os.path.exists(SETTINGS_FILE):
                with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    current_theme = settings.get('theme', 'dark')
                    current_font_size = settings.get('font_size', system_fonts['default_size'])
                    self.auto_close_setting = settings.get('auto_close', 'never')
            
            if os.path.exists(RECENT_FILES_FILE):
                with open(RECENT_FILES_FILE, 'r', encoding='utf-8') as f:
                    recent_files = json.load(f)
        except:
            pass
    
    def save_settings(self):
        try:
            settings = {
                'theme': current_theme,
                'font_size': current_font_size,
                'auto_close': getattr(self, 'auto_close_setting', 'never')
            }
            with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2)
            
            with open(RECENT_FILES_FILE, 'w', encoding='utf-8') as f:
                json.dump(recent_files[:10], f, indent=2)
        except:
            pass
    
    def load_venv_settings(self):
        """仮想環境設定を読み込み"""
        try:
            if os.path.exists('venv_settings.json'):
                with open('venv_settings.json', 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"仮想環境設定の読み込みエラー: {e}")
        return {'venv_path': '.venv', 'use_custom_path': False}
    
    def save_venv_settings(self, venv_path, use_custom_path):
        """仮想環境設定を保存"""
        try:
            settings = {
                'venv_path': venv_path,
                'use_custom_path': use_custom_path
            }
            with open('venv_settings.json', 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2)
        except Exception as e:
            print(f"仮想環境設定の保存エラー: {e}")
    
    def browse_venv_path(self, path_var):
        """仮想環境ディレクトリを選択"""
        from tkinter import filedialog
        initial_dir = path_var.get()
        if not os.path.isabs(initial_dir):
            initial_dir = os.getcwd()
        
        folder_path = filedialog.askdirectory(
            title="仮想環境ディレクトリを選択",
            initialdir=initial_dir
        )
        
        if folder_path:
            path_var.set(folder_path)
    
    def copy_to_clipboard(self, text):
        """テキストをクリップボードにコピー"""
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            # 一時的なフィードバックを表示
            temp_label = tk.Label(self.root, text="✓ クリップボードにコピーしました", 
                               bg=theme['accent'], fg='white',
                               font=(system_fonts['ui_font'], 10))
            temp_label.place(x=10, y=10)
            self.root.after(2000, temp_label.destroy)
        except Exception as e:
            messagebox.showerror("エラー", f"クリップボードへのコピーに失敗しました: {e}")
    
    def parse_error(self, error_output, code_content):
        """エラー出力を解析して行番号とエラー種別を抽出"""
        error_info = {
            'line_number': None,
            'error_type': None,
            'error_message': error_output,
            'suggestions': []
        }
        
        # 一般的なPythonエラーパターン
        patterns = [
            # 構文エラー
            r'SyntaxError: (.+) at line (\d+)',
            r'File ".*", line (\d+)',
            r'.*line (\d+).*SyntaxError: (.+)',
            
            # インデントエラー
            r'IndentationError: (.+) at line (\d+)',
            r'.*line (\d+).*IndentationError: (.+)',
            
            # 名前エラー
            r'NameError: name \'(.+)\' is not defined',
            r'.*line (\d+).*NameError: name \'(.+)\' is not defined',
            
            # 型エラー
            r'TypeError: (.+)',
            r'.*line (\d+).*TypeError: (.+)',
            
            # 属性エラー
            r'AttributeError: (.+)',
            r'.*line (\d+).*AttributeError: (.+)',
            
            # インポートエラー
            r'ImportError: (.+)',
            r'ModuleNotFoundError: No module named \'(.+)\'',
            
            # ゼロ除算エラー
            r'ZeroDivisionError: (.+)',
            r'.*line (\d+).*ZeroDivisionError: (.+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, error_output, re.IGNORECASE)
            if match:
                if 'line' in pattern.lower():
                    # 行番号を抽出
                    if len(match.groups()) >= 2:
                        if match.group(1).isdigit():
                            error_info['line_number'] = int(match.group(1))
                            error_info['error_type'] = match.group(2)
                        else:
                            error_info['line_number'] = int(match.group(2))
                            error_info['error_type'] = match.group(1)
                    else:
                        error_info['line_number'] = int(match.group(1))
                        error_info['error_type'] = '構文エラー'
                else:
                    # モジュール未検出エラー
                    if 'ModuleNotFoundError' in pattern or 'ImportError' in pattern:
                        error_info['error_type'] = 'インポートエラー'
                        error_info['suggestions'].append(f"インストールを試してください: pip install {match.group(1)}")
                break
        
        # エラー種別に基づいて提案を生成
        if error_info['error_type']:
            error_type = error_info['error_type'].lower()
            
            if 'syntax' in error_type or '構文' in error_type:
                error_info['suggestions'].extend([
                    "コロン、括弧、引用符の欠落を確認",
                    "適切なインデントを確認",
                    "不一致な括弧を確認"
                ])
            elif 'indentation' in error_type or 'インデント' in error_type:
                error_info['suggestions'].extend([
                    "一貫したインデントを使用（4スペース推奨）",
                    "タブとスペースの混在を確認",
                    "適切なインデントレベルを確認"
                ])
            elif 'name' in error_type or '名前' in error_type:
                error_info['suggestions'].extend([
                    "変数名のスペルを確認",
                    "使用前に変数が定義されていることを確認",
                    "インポート文を確認"
                ])
            elif 'type' in error_type or '型' in error_type:
                error_info['suggestions'].extend([
                    "変数のデータ型を確認",
                    "型変換関数を使用（int(), str()など）",
                    "関数の引数を確認"
                ])
            elif 'attribute' in error_type or '属性' in error_type:
                error_info['suggestions'].extend([
                    "オブジェクト属性名のスペルを確認",
                    "オブジェクトの型と利用可能なメソッドを確認",
                    "必要なモジュールのインポート文を確認"
                ])
        
        return error_info
    
    def fix_common_errors(self, code_content, error_info):
        """一般的なエラーを自動修正"""
        if not error_info['line_number'] or not error_info['error_type']:
            return code_content, False
        
        lines = code_content.split('\n')
        line_num = error_info['line_number'] - 1  # 0ベースに変換
        
        if line_num < 0 or line_num >= len(lines):
            return code_content, False
        
        original_line = lines[line_num]
        fixed_line = original_line
        fixed = False
        
        error_type = error_info['error_type'].lower()
        
        # 一般的な構文エラーを修正
        if 'syntax' in error_type or 'indentation' in error_type or '構文' in error_type or 'インデント' in error_type:
            # if/for/while/def/class文の末尾に欠落したコロンを追加
            if any(keyword in original_line for keyword in ['if ', 'for ', 'while ', 'def ', 'class ']) and not original_line.rstrip().endswith(':'):
                fixed_line = original_line.rstrip() + ':'
                fixed = True
            
            # 欠落した引用符を修正
            if original_line.count('"') % 2 != 0 or original_line.count("'") % 2 != 0:
                if original_line.count('"') % 2 != 0:
                    fixed_line = original_line.rstrip() + '"'
                elif original_line.count("'") % 2 != 0:
                    fixed_line = original_line.rstrip() + "'"
                fixed = True
            
            # 不一致な括弧を修正
            if original_line.count('(') != original_line.count(')'):
                missing = original_line.count('(') - original_line.count(')')
                if missing > 0:
                    fixed_line = original_line.rstrip() + ')' * missing
                else:
                    fixed_line = original_line.rstrip() + '(' * (-missing)
                fixed = True
        
        # インデントエラーを修正
        if 'indentation' in error_type or 'インデント' in error_type:
            # 不一貫なインデントを修正
            if line_num > 0:
                prev_line = lines[line_num - 1]
                if prev_line.endswith(':') and not original_line.startswith('    '):
                    fixed_line = '    ' + original_line
                    fixed = True
                elif original_line.startswith('    ') and not prev_line.endswith(':'):
                    # この行がインデントされるべきでないかを確認
                    if any(keyword in original_line for keyword in ['def ', 'class ', 'if ', 'for ', 'while ']):
                        fixed_line = original_line[4:]  # インデントを削除
                        fixed = True
        
        # 修正があった場合は適用
        if fixed:
            lines[line_num] = fixed_line
            return '\n'.join(lines), True
        
        return code_content, False
    
    def show_error_dialog(self, error_output, code_content, tab=None):
        """詳細なエラーダイアログと修正オプションを表示"""
        error_info = self.parse_error(error_output, code_content)
        
        dialog = tk.Toplevel(self.root)
        dialog.title("エラー解析と修正")
        dialog.geometry("600x500")
        dialog.transient(self.root)
        dialog.grab_set()
        
        theme = THEMES[current_theme]
        dialog.configure(bg=theme['bg'])
        
        # エラー情報フレーム
        info_frame = tk.Frame(dialog, bg=theme['bg'])
        info_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(info_frame, text="エラー解析:", bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 10, 'bold')).pack(anchor=tk.W)
        
        # 行番号
        if error_info['line_number']:
            tk.Label(info_frame, text=f"行: {error_info['line_number']}", 
                    bg=theme['bg'], fg=theme['fg_secondary'],
                    font=(system_fonts['ui_font'], 9)).pack(anchor=tk.W, pady=2)
        
        # エラー種別
        if error_info['error_type']:
            tk.Label(info_frame, text=f"種別: {error_info['error_type']}", 
                    bg=theme['bg'], fg=theme['fg_secondary'],
                    font=(system_fonts['ui_font'], 9)).pack(anchor=tk.W, pady=2)
        
        # エラーメッセージ
        msg_frame = tk.Frame(info_frame, bg=theme['bg'])
        msg_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(msg_frame, text="メッセージ:", bg=theme['bg'], fg=theme['fg'],
                font=(system_fonts['ui_font'], 9)).pack(side=tk.LEFT)
        
        copy_btn = tk.Button(msg_frame, text="📋 コピー", 
                           command=lambda: self.copy_to_clipboard(error_output),
                           bg=theme['bg_secondary'], fg=theme['fg'],
                           font=(system_fonts['ui_font'], 9))
        copy_btn.pack(side=tk.RIGHT, padx=5)
        
        # エラーメッセージ表示
        error_text = tk.Text(info_frame, height=4, font=(system_fonts['ui_font'], 10),
                           bg=theme['bg_secondary'], fg=theme['fg'], wrap=tk.WORD)
        error_text.pack(fill=tk.X, pady=5)
        error_text.insert('1.0', error_output)
        error_text.config(state=tk.DISABLED)
        
        # 提案
        if error_info['suggestions']:
            tk.Label(info_frame, text="提案:", bg=theme['bg'], fg=theme['fg'],
                    font=(system_fonts['ui_font'], 9, 'bold')).pack(anchor=tk.W, pady=(10, 2))
            
            for suggestion in error_info['suggestions']:
                tk.Label(info_frame, text=f"• {suggestion}", 
                        bg=theme['bg'], fg=theme['fg_secondary'],
                        font=(system_fonts['ui_font'], 10)).pack(anchor=tk.W, padx=10)
        
        # コードプレビュー
        if error_info['line_number']:
            tk.Label(info_frame, text="コードプレビュー (行 {}):".format(error_info['line_number']), 
                    bg=theme['bg'], fg=theme['fg'],
                    font=(system_fonts['ui_font'], 9, 'bold')).pack(anchor=tk.W, pady=(10, 2))
            
            code_lines = code_content.split('\n')
            start_line = max(0, error_info['line_number'] - 3)
            end_line = min(len(code_lines), error_info['line_number'] + 2)
            
            code_text = tk.Text(info_frame, height=6, font=(system_fonts['ui_font'], 10),
                               bg=theme['bg_secondary'], fg=theme['fg'])
            code_text.pack(fill=tk.X, pady=5)
            
            for i in range(start_line, end_line):
                line_num = i + 1
                prefix = ">>> " if line_num == error_info['line_number'] else "    "
                code_text.insert(tk.END, f"{prefix}{line_num:3d}: {code_lines[i]}\n")
            
            code_text.config(state=tk.DISABLED)
        
        # アクションボタン
        button_frame = tk.Frame(dialog, bg=theme['bg'])
        button_frame.pack(pady=20, padx=20, fill=tk.X)
        
        # 自動修正を試行
        if error_info['line_number'] and tab:
            try:
                fixed_code, was_fixed = self.fix_common_errors(code_content, error_info)
                if was_fixed:
                    fix_btn = tk.Button(button_frame, text="🔧 自動修正", 
                                     command=lambda: self.apply_fix(tab, fixed_code, dialog),
                                     bg=theme['accent'], fg='white',
                                     font=(system_fonts['ui_font'], 9))
                    fix_btn.pack(side=tk.LEFT, padx=5)
            except:
                pass
        
        # 行に移動
        if error_info['line_number'] and tab:
            goto_btn = tk.Button(button_frame, text="📍 行に移動", 
                               command=lambda: self.go_to_line(tab, error_info['line_number'], dialog),
                               bg=theme['bg_secondary'], fg=theme['fg'],
                               font=(system_fonts['ui_font'], 9))
            goto_btn.pack(side=tk.LEFT, padx=5)
        
        # 閉じる
        close_btn = tk.Button(button_frame, text="閉じる", command=dialog.destroy,
                            bg=theme['bg_secondary'], fg=theme['fg'],
                            font=(system_fonts['ui_font'], 9))
        close_btn.pack(side=tk.RIGHT, padx=5)
    
    def apply_fix(self, tab, fixed_code, dialog):
        """自動修正をコードに適用"""
        try:
            tab.text.delete('1.0', tk.END)
            tab.text.insert('1.0', fixed_code)
            dialog.destroy()
            messagebox.showinfo("成功", "エラーが自動的に修正されました！")
        except Exception as e:
            messagebox.showerror("エラー", f"修正の適用に失敗しました: {e}")
    
    def go_to_line(self, tab, line_number, dialog):
        """コードの特定の行に移動"""
        try:
            # 最初にダイアログを閉じる
            dialog.destroy()
            
            # アクティブでない場合はタブを切り替え
            global active_tab
            if tab != active_tab:
                self.notebook.select(self.tabs.index(tab))
                active_tab = tab
            
            # 行に移動
            line_start = f"{line_number}.0"
            tab.text.mark_set(tk.INSERT, line_start)
            tab.text.see(line_start)
            tab.text.focus_set()
            
            # 行を一時的にハイライト
            tab.text.tag_add('error_line', line_start, f"{line_number}.end")
            tab.text.tag_config('error_line', background='#ffcccc')
            
            # 3秒後にハイライトを削除
            self.root.after(3000, lambda: tab.text.tag_remove('error_line', line_start, f"{line_number}.end"))
            
        except Exception as e:
            messagebox.showerror("エラー", f"行への移動に失敗しました: {e}")
    
    def save_recent_files(self):
        try:
            with open(RECENT_FILES_FILE, 'w', encoding='utf-8') as f:
                json.dump(recent_files[:10], f, indent=2)
        except:
            pass
    
    def run(self):
        self.root.mainloop()

# メイン実行
if __name__ == "__main__":
    app = ModernIDE()
    app.run()
