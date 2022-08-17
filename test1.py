# python基础
# 题目
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for a in range(1, 5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#             if a != b and a != c and b != c:
#                 print(a, b, c)


# print(10 % 3) # 判断奇偶数，0为偶数，1为奇数
# print(10//3) # 取整数
# a = 3.14 * 1.57
# print(round(a, 2)) # round是取两位小数
import time, os
from appium import webdriver

# os.startfile(r'D:\Program Files\Nox\bin\Nox.exe') # 启动模拟器
# time.sleep(20)
# os.system('adb connect 127.0.0.1:62001') # 连接模拟器
desired_caps = {
  "platformName": "Android",
  "deviceName": "夜神模拟器端的新雳",
  "appPackage": "com.newpowerf1.app.android",
  "appActivity": "com.newpowerf1.mall.ui.LoginActivity",
  "automationName": "UiAutomator2",
  "noReset": True,
  "newCommandTimeout": 6000
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element('id', 'com.newpowerf1.app.android:id/number_edit').send_keys('13763910426')
driver.find_element('id', 'com.newpowerf1.app.android:id/code_edit').send_keys('000000')
driver.find_element('id', 'com.newpowerf1.app.android:id/select_image').click()
driver.find_element('id', 'com.newpowerf1.app.android:id/login_button').click()

time.sleep(1)
print(111)
