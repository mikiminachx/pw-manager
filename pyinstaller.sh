#!/bin/sh

pyinstaller --onedir --noconfirm \
            --contents-directory '$HOME/Desktop/pw-manager:.' \
            --icon 'ding.icns' \
            --windowed
            main.py