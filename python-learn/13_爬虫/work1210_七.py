from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化浏览器驱动
driver = webdriver.Chrome()  # 初始化 ChromeDriver
driver.get("https://accounts.douban.com/passport/login?source=movie")  # 打开豆瓣登录页面

# 输入手机号
phone_input = driver.find_element(By.NAME, 'phone')  # 定位手机号输入框
phone_input.send_keys('18585595238')  # 输入手机号

# 点击获取验证码
get_code_button = driver.find_element(By.CLASS_NAME, 'get-code')  # 定位获取验证码按钮
get_code_button.click()  # 点击按钮

# 等待验证码加载
time.sleep(3)

# 切换到验证码 iframe
iframe = driver.find_element(By.ID, "tcaptcha_iframe_dy")  # 定位 iframe
driver.switch_to.frame(iframe)  # 切换到 iframe

# 定位滑块和滑块轨迹背景
button = driver.find_element(By.CLASS_NAME, "tc-fg-item")  # 滑块元素
background = driver.find_element(By.ID, "slideBg")  # 滑块背景

# 生成滑块移动轨迹
def get_track(distance):
    """
    根据距离生成移动轨迹
    :param distance: 滑块需要移动的距离
    :return: 轨迹列表
    """
    track = []
    current = 0
    mid = distance * 4 / 5  # 加速距离
    t = 0.2  # 时间间隔
    v = 0  # 初速度

    while current < distance:
        if current < mid:
            a = 2  # 加速
        else:
            a = -3  # 减速
        v0 = v
        v = v0 + a * t
        move = v0 * t + 0.5 * a * t * t
        current += move
        track.append(round(move))
    return track

# 模拟滑块移动
def move_to_gap(slider, tracks):
    """
    拖动滑块到缺口
    :param slider: 滑块元素
    :param tracks: 滑块移动轨迹
    """
    ActionChains(driver).click_and_hold(slider).perform()  # 按住滑块
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()  # 按轨迹移动
        time.sleep(0.05)
    ActionChains(driver).release().perform()  # 松开滑块

# 手动测量滑块需要移动的距离
distance = int(input("请输入滑块需要移动的距离：\n"))
track_list = get_track(distance)  # 获取滑块轨迹
move_to_gap(button, track_list)  # 移动滑块

# 返回主页面
driver.switch_to.default_content()

# 输入短信验证码
sms_code = input("请输入手机短信验证码：\n")  # 输入验证码
driver.find_element(By.ID, 'code').send_keys(sms_code)  # 填写验证码
driver.find_element(By.CLASS_NAME, 'btn-phone').click()  # 点击登录按钮

time.sleep(15)

# 获取书籍信息
driver.get("https://book.douban.com")  # 跳转到豆瓣图书页面
book = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[1]/div[2]/div[1]/div/ul[2]/li[1]/div[2]/div[1]/a')
print("书籍信息：", book.text)  # 输出书籍信息

# 保存网页源码
with open("doubanbook2.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# 关闭浏览器
driver.quit()
