import cv2
from windows_capture import WindowsCapture, Frame, InternalCaptureControl
import configparser
import sys
import os


def get_base_path():
    # Works both in dev and when frozen by PyInstaller
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


def get_exe_path(filename):
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(__file__)
    return os.path.join(base, filename)


config = configparser.ConfigParser()
config_path = os.path.join(get_base_path(), 'config.ini')
config.read(config_path)

window_name = config.get('settings', 'window_name', fallback='World')
ult_pixel = config.get('settings', 'ult_pixel', fallback='0,0')
frame_interval = config.getint('settings', 'frame_interval', fallback='16')
heal_pixel = config.get('settings', 'heal_pixel', fallback='0,0')

ult_x, ult_y = map(int, ult_pixel.split(','))
heal_x, heal_y = map(int,heal_pixel.split(','))


capture = WindowsCapture(
    window_name=window_name,
    minimum_update_interval=frame_interval,
    cursor_capture=False,
    draw_border=False,
)


@capture.event
def on_frame_arrived(frame: Frame, capture_control: InternalCaptureControl):
    bgra = frame.frame_buffer.copy()
    bgr = cv2.cvtColor(bgra, cv2.COLOR_BGRA2BGR)

    pixel = bgr[ult_y, ult_x]
    b, g, r = pixel
    is_ulting = (b, g, r) == (255, 199, 228)

    if is_ulting != on_frame_arrived.last_ult_state:
        on_frame_arrived.last_ult_state = is_ulting
        with open(get_exe_path('ult_state.txt'), 'w') as f:
            f.write('true' if is_ulting else 'false')

    pixel = bgr[heal_y, heal_x]
    b, g, r = pixel
    is_healing = (b, g, r) == (255, 199, 228)
    if is_healing != on_frame_arrived.last_heal_state:
        on_frame_arrived.last_heal_state = is_healing
        with open(get_exe_path('heal_state.txt'), 'w') as f:
            f.write('true' if is_healing else 'false')


@capture.event
def on_closed():
    print("Capture session closed")

on_frame_arrived.last_ult_state = None
on_frame_arrived.last_heal_state = None
capture.start()
