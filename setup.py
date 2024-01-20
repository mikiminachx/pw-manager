"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['sqlite3', 'cryptography', 'tkinter', 'cffi'],
    'includes': ['ctypes', '_ctypes'],
    'frameworks': ['/opt/homebrew/opt/libffi/lib/libffi.8.dylib']
}

setup(
    app=APP,
    name="PasswordManager",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
