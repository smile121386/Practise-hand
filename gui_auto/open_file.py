import pyautogui
import win32con
import win32gui
import win32api
import time

file_name = r'D:\test.docx'
pyautogui.hotkey('win', 'r')
run_hwnd = win32gui.FindWindow('#32770', '运行')
print(run_hwnd)
edit_hwnd = win32gui.FindWindowEx(run_hwnd, None, 'ComboBox', None)
edit_hwnd_ex = win32gui.FindWindowEx(edit_hwnd, None, 'Edit', None)
if edit_hwnd_ex:
    win32api.SendMessage(edit_hwnd_ex, win32con.WM_SETTEXT, 0, file_name)
else:
    print('none')
time.sleep(1)
btn_hwnd = win32gui.FindWindowEx(run_hwnd, None, 'Button', '确定')
win32gui.PostMessage(btn_hwnd, win32con.WM_LBUTTONDOWN, 0, 0)
win32gui.PostMessage(btn_hwnd, win32con.WM_LBUTTONUP, 0, 0)
