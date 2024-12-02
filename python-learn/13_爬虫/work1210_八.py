# 导入模块
import pytesseract
from PIL import Image
from random import randint

# 配置 Tesseract-OCR 的路径
pytesseract.pytesseract.tesseract_cmd = r'E:\Python\Tool\tesseract\tesseract.exe'

# 将图像文件转换成 Image 实例
image = Image.open('E:\Python\Code\Study\HM_Study\python-learn\\13_爬虫\img.png')

# 将图像中的文本转换成文本，进行输出
text = pytesseract.image_to_string(image)
print(text)

# 随机获取一个本地验证码图片的名称
picName = 'E:\Python\Code\Study\HM_Study\python-learn\\13_爬虫\img2.png'  # 随机生成图片文件名
image = Image.open(picName)  # 加载图片

# 从图片中识别验证码
text = pytesseract.image_to_string(image)

# 输出图片名称和识别到的验证码文字
print(picName + ": " + text)
