# 🚀 Day 94 - Space Invaders

A classic-style **2D Space Shooter Game** built using **Python and PyGame**. The player controls a yellow spaceship and must survive waves of alien enemies while dodging lasers and shooting back.

---

## 🧠 Concepts Practised

- 🎮 **Making a 2D Game with PyGame**
  - Built a fully playable 2D game with moving enemies, player, lasers, and health mechanics.

- 🖼️ **Drawing (Blitting) Game Assets**
  - Loaded images and rendered them on screen with `blit()` for ships, lasers, and background.

- 🔧 **Organized Use of Classes**
  - Created modular classes:
    - `Ship`: Base class
    - `Player`: Inherits from `Ship`, handles user input and health bar
    - `Enemy`: Inherits from `Ship`, moves and shoots
    - `Laser`: Represents bullets from ships

- 🕹️ **Handling User Input**
  - Listened to keyboard events to move the player (arrow keys) and shoot (spacebar).

- 🔁 **Implementing Event Loops**
  - Built the main game loop with proper FPS control, event detection, and game updates.

---

## 🖥️ How to Play

- 🟡 **Move** your yellow ship using the arrow keys.
- 🔫 **Shoot** lasers using the spacebar.
- 🚀 **Dodge** enemy lasers and destroy enemies before they reach the bottom.
- 💀 You lose when all lives or your health reach zero.

---

## 🔧 Requirements

- Python 3.x
- [PyGame](https://pypi.org/project/pygame/)

Install with:

```bash
pip install pygame
