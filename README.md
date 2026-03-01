# Deadlock Monitor

A lightweight Python program that monitors your Deadlock game window in real time, detecting when your character is channeling their ultimate (4) or 3 ability.

## How It Works

Deadlock Monitor captures the game window and checks specific pixel colors on screen to determine ability states. When a channeling ability is detected, the corresponding text file is updated — making it easy for external tools like stream overlays or macros to react to in-game ability usage.


Deadlock must be running before this program!
## Output Files

| File | Ability | Value |
|------|---------|-------|
| `ult_state.txt` | Ultimate (4) | `true` while channeling, `false` when not |
| `heal_state.txt` | 3 Ability | `true` while channeling, `false` when not |

## Character Support

Primarily made for **Dynamo**, but should work for any character with channeling abilities provided the pixel coordinates are configured correctly.

## Configuration

Edit `config.ini` to set your pixel coordinates and window name:
Frame interval is miliseconds per capture, 16 = 62.5 FPS

```ini
[settings]
window_name = Deadlock
frame_interval = 16
ult_pixel = 1382,1021
heal_pixel = 1293,1009
```
