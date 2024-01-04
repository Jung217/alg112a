# 引入VPython套件
from vpython import *

# 設定球的半徑和顏色
r = 0.5
c = color.red

# 建立一個空的列表，用來儲存球的物件
balls = []

# 用雙層迴圈來產生球的位置
for i in range(-3, 4):
    for j in range(-3, 4):
        # 計算球的x座標和y座標，讓球與球之間有一定的間隙
        x = i * (2 * r + 0.01)
        y = j * (2 * r + 0.01)
        # 如果i和j的和是偶數，則球的z座標為0
        # 如果i和j的和是奇數，則球的z座標為根號2乘以半徑，讓球與下層的球相切
        if (i + j) % 2 == 0:
            z = 0
        else:
            z = sqrt(2) * r
        # 用sphere函數來產生球的物件，並指定位置、半徑和顏色
        ball = sphere(pos=vector(x, y, z), radius=r, color=c)
        # 把球的物件加入到列表中
        balls.append(ball)