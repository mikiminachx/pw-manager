#!/bin/sh

create-dmg \
    --volname "PWM Installer" \
    --volicon "ding.icns" \
    --window-pos 200 120 \
    --window-size 800 400 \
    --icon-size 100 \
    --icon "PWM.app" 200 190 \
    --hide-extention "PWM.app" \
    "dist/PWM.dmg" \
    "dist/dmg/"