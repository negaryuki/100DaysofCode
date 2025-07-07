# 🦖 Day 93 - Google Dinosaur Game Bot

This Python script automates gameplay for the offline **Google Chrome Dinosaur Game** using pixel detection and simulated keypresses.

## 🎯 Concepts Practised

- 🎯 **Pixel Detection with PyAutoGUI**
  - Use of `pyautogui.pixel()` to read RGB values at specific screen coordinates.
  - Detect obstacles like tall/short cacti and flying pterodactyls by comparing pixel colors.

- ⌨️ **Keyboard Simulation with PyWin32**
  - Fast, low-level key presses (`Up` for jumping, `Down` for ducking) using `win32api` and `win32con`.
  - Realistic keypress timing for better accuracy.

- ⚡ **Adaptive Obstacle Detection**
  - After a few jumps, the game's speed increases.
  - The bot adjusts pixel positions to react faster and catch obstacles earlier.

## 🔧 How It Works

1. **Pixel Checking**:
   - Detects specific RGB values on the game screen at known obstacle positions.
2. **Jump/Duck Simulation**:
   - Simulates keyboard events to jump over or duck under obstacles.
3. **Adaptive Speed**:
   - As jump count increases, the bot checks closer pixels to react faster to obstacles.

## 🖥️ Requirements

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/pyautogui/)
- [PyWin32](https://pypi.org/project/pywin32/)
- [keyboard](https://pypi.org/project/keyboard/)

```bash
pip install pyautogui pywin32 keyboard
