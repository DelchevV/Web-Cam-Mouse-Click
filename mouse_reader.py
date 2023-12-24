import pyautogui

def get_mouse_coordinates():
    return pyautogui.position()

def is_left_mouse_button_pressed():
    return pyautogui.mouseInfo().get('left')

