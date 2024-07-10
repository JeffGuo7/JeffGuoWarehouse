import cv2
from pyzbar.pyzbar import decode

# 读取支付二维码
img = cv2.imread('23ff92d905addaf48be18997d0cd532.jpg')

# 解析二维码信息
data = decode(img)

# 打印二维码信息
print(data[0].data.decode('utf-8'))
