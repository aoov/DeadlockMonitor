# Deadlock Monitor

A lightweight Python program that monitors your Deadlock game window in real time, detecting when your character is channeling their ultimate (4) or 3 ability.

## How It Works

Deadlock Monitor captures the game window and checks specific pixel colors on screen to determine ability states. When a channeling ability is detected, the corresponding text file is updated — making it easy for external tools like stream overlays or macros to react to in-game ability usage.

> ⚠️ Deadlock must be running before this program!

## How To Use

1. Take a screenshot of the game
2. Use a pixel inspector like [PixSpy](https://pixspy.com/) (or any other tool) to find the coordinates of a point on the ability circle around the edges — this area wobbles when channeling
3. Update the corresponding coordinates in `config.ini`
4. Run the program (make sure Deadlock is open) — the text files will generate and update automatically

## Output Files

| File | Ability | Value |
|------|---------|-------|
| `ult_state.txt` | Ultimate (4) | `true` while channeling, `false` when not |
| `heal_state.txt` | 3 Ability | `true` while channeling, `false` when not |

## Configuration

Edit `config.ini` to set your pixel coordinates and window name. `frame_interval` is milliseconds per capture — `16` equals ~62.5 FPS.

```ini
[settings]
window_name = Deadlock
frame_interval = 16
ult_pixel = 1382,1021
heal_pixel = 1293,1009
```

## Character Support

Primarily made for **Dynamo**, but should work for any character with channeling abilities provided the pixel coordinates are configured correctly.
