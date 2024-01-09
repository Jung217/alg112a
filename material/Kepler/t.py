import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def kepler_conjecture(num_spheres):
    # 生成球體的中心座標
    centers = np.arange(0, num_spheres)

    # 生成三維坐標
    x, y, z = np.meshgrid(centers, centers, centers)

    # 將坐標展平成一維陣列
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()

    # 設定球體半徑
    radius = 500

    # 繪製三維圖形
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=radius, color='b', marker='o', alpha=0.5)

    # 設定坐標軸
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 顯示圖形
    plt.show()

# 模擬堆疊 5 個球體
kepler_conjecture(5)