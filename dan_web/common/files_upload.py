import win32gui
import win32con
import time
from selenium.webdriver import Chrome


class FilesUpload():

    def __init__(self, dirver:Chrome):
        self.driver = dirver

    def files_up(self):
        """本地文件上传"""
        time.sleep(1)
        dialog = win32gui.FindWindow('#32770', '打开')  # 一级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)  # 二级窗口
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)  # 三级窗口
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级窗口
        button = win32gui.FindWindowEx(dialog, 0, 'button', None)  # 一级窗口
        time.sleep(2)  # 必须等到，js需要时间反应过来
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r'C:\Users\HP\Desktop\test.xlsx')  # 发送文件路径
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)   # 点击打开按钮
        time.sleep(2)


"""
第一种方式：input标签，type='file'
先定位上传框，在send_keys
ele = wait_find_element((By.XPATH, '//input[@accept="undefined"]'))
ele.send_keys('此处输入绝对路径')

文件上传
第二种方式：非input标签：python pywin32库+winspy：识别对话框句柄，进而操作
1、定位上传窗口：#32770,打开
2、子窗口：ComboBoxEx32，button
3、子窗口：ComboBox
3、子窗口（文件路径输入区域）：Edit
"""