# 在 Python 中從 0 開始進行 *光線追踪*

> 全篇整理自 [Omar Aflak-Ray Tracing From Scratch in Python](https://omaraflak.medium.com/ray-tracing-from-scratch-in-python-41670e6a96f9)
> 
> 圖片、程式也來自上方出處，其他來源另標註

## 前言
讀完這篇文章將會了解電腦圖形演算法、光線追蹤演算法，並有一個簡單的 Python 實作，寫一個只要需 NumPy 的程式來生成下方圖片

![image](https://github.com/Jung217/alg112a/assets/99934895/f3021710-9f19-410d-8b2d-1364df24aa99)

## 先決條件
* 基本的向量幾何
* 如果有 2 個點 A 和 B (無論維數是多少：1、2、3、…、n)，可以透過計算找到從 A 到 B 的向量
* 向量的長度可以透過計算平方分量總和的平方根來找到。向量的長度 v 表示為 `||v||`
* 單位向量是長度為 1 的向量 (||v|| = 1)
* 給定一個向量，透過將第一個向量的每個分量除以其長度可以找到指向相同方向而長度為 1 的向量，稱為正歸化 (u = v / ||v||)
* 向量的點積 (<v, v> = ||v||²)
* 求解二次方程式

## 光追演算法
光線追蹤是一種模擬光路和與物體相交的渲染技術，能夠產生高度真實的影像。

* 設定一個場景：
  * 一個 3D 空間（使用 3 維座標在空間中定位物件）
  * 一些空間中的物體
  * 一個光源（一個向各個方向發射光的單點(一個點)）
  * 一隻「眼睛」 or 一台相機（觀察場景(一個點)）；
  * 一個螢幕 (因為相機可以觀察任何地方，相機將透過螢幕觀察物體（矩形螢幕的四個角落的 4 個位置）)
* 光追演算法
  ```
  對於螢幕的每個像素 p (x,y,z)：
      將黑色連結 p
      如果起始於相機的射線朝向 p 並與場景中的任何物件相交：
          計算最近物體交點
          如果射點和光之間沒有物體(相交)：
              計算交點顏色
              連結 p 的顏色交點
  ```
  ![image](https://github.com/Jung217/alg112a/assets/99934895/83b1653b-f906-4f0a-92ba-f902fc05ba9d)
  
> 這個過程實際上是現實中照明的相反過程；實際上，光線從光源向各個方向射出，在物體上反射並射入眼睛。
> 
> 但並非所有發出的光線都會進入眼睛，因此光線追蹤會執行**相反**的過程以**節省計算時間**

## 設定場景
在寫程式前，需要設定一個場景。為了達成目的，透過將它們與單位軸對齊來使事情變得簡單。相機位於 (0, 0, 1)，螢幕是 xy 平面的一部分。
```py
import numpy as np
import matplotlib.pyplot as plt

# 圖像寬高
width = 300
height = 200

# 相機位置
camera = np.array([0, 0, 1])

# 圖像寬高比
ratio = float(width) / height

# 螢幕邊界 (left, top, right, bottom)
screen = (-1, 1 / ratio, 1, -1 / ratio)

# 初始化圖像數據
image = np.zeros((height, width, 3))

# 迭代每個像素
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
        # 在這裡填入根據需求設置像素顏色的程式碼
        # image[i, j] = ...

        # 顯示進度
        print("progress: %d/%d" % (i + 1, height))

# 將圖像保存為 PNG 檔案
plt.imsave('image.png', image)
```

## 射線相交
### 射線定義
> 射線實際上該說是向量。當編寫幾何圖形時，應該使用向量，它們更容易使用，並且更不容易出現除零等錯誤。
由於光線從相機開始並向當前目標像素的方向前進，因此我們可以定義一個指向相似方向的單位向量。

將「從相機開始朝向像素的光線」定義為以下等式：

![image](https://github.com/Jung217/alg112a/assets/99934895/47455479-5f7e-4be0-a98c-9ef54a5f3b77)

**相機和像素都是 3D 點**。因為 t=0 最終會到相機的位置，並且增加的越多，在像素方向上 t 與相機的距離就越遠。
這個參數函式對於給定的 t 產生沿直線的點。(定義一條從原點（O）開始並朝向目的地（D）的射線，d 定義為方向向量)：

![image](https://github.com/Jung217/alg112a/assets/99934895/27f42986-1c6d-4573-81ab-abda13ce246e)

(添加 origin 和 direction 的計算，兩者定義了一條射線。像素的 z=0，因為它在螢幕上 (螢幕在 xy平面中))
```py
import numpy as np
import matplotlib.pyplot as plt

# 正規化向量(單位向量)
def normalize(vector):
    return vector / np.linalg.norm(vector)

# 圖像寬高
width = 300
height = 200

# 相機位置
camera = np.array([0, 0, 1])

# 圖像寬高比
ratio = float(width) / height

# 螢幕邊界 (left, top, right, bottom)
screen = (-1, 1 / ratio, 1, -1 / ratio)

# 初始化圖像數據
image = np.zeros((height, width, 3))

# 迭代每個像素
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
        # 當前像素的三維坐標
        pixel = np.array([x, y, 0])

        # 相機到像素的方向向量（歸一化）
        origin = camera
        direction = normalize(pixel - origin)

        # 在這裡填入根據需求設置像素顏色的程式碼
        # image[i, j] = ...

    # 顯示進度
    print("progress: %d/%d" % (i + 1, height))

# 將圖像保存為 PNG 檔案
plt.imsave('image.png', image)
```

### 球體定義
> 球體其實是一個定義起來非常簡單的物件。球體被定義為距中心點的距離 r（半徑）相同的點的集合。

給定球體的中心C及其半徑r，任意點X位於球體上若且唯若：

![image](https://github.com/Jung217/alg112a/assets/99934895/60a446e1-0c2b-482e-9638-6f94f9a93124)

為了方便，將兩邊平方，以消除由 X — C 的大小引起的平方根

![image](https://github.com/Jung217/alg112a/assets/99934895/4950239c-7cd4-4d7f-a157-6cb62f1bdda9)

```py
# 定義一些球體物件
objects = [
    { 'center': np.array([-0.2, 0, -1]), 'radius': 0.7 },
    { 'center': np.array([0.1, -0.3, 0]), 'radius': 0.1 },
    { 'center': np.array([-0.3, 0, 0]), 'radius': 0.15 }
]
```

### 球體交點
我們知道射線函式，也知道一個點必須滿足什麼條件才能位於球體上。

現在所要做的就是插入 `eq. 2` 並 `eq. 4` 求解 `t` 這意代表：哪些 t、ray(t) 位於球體上

![image](https://github.com/Jung217/alg112a/assets/99934895/e9508b57-d432-42fa-9b89-d8b99b09b684)

這是可以求解的普通二次方程式 t。t², t¹, t⁰ 將分別呼叫與 a、b 和 c 相關的係數。計算方程式的判別式：

![image](https://github.com/Jung217/alg112a/assets/99934895/baee7a61-e4d1-4662-807d-a8f97a839025)

由於 d（方向）是單位向量，因此我們有 a=1。一旦計算出方程式的判別式，就有 3 種可能性：

![image](https://github.com/Jung217/alg112a/assets/99934895/ab4999e5-00fe-4a13-b58f-8bb4ecc90f7f)

這裡只會使用**第三種**情況來偵測交叉點。這是一個可以偵測射線和球體之間相交的函數。如果射線與球體相交，它將從射線返原點回到最近交點 t 的距離，否則返回 None。

(僅當 t1 和 t2 均為正數時，才會傳回最近的交集。因為求解方程式的 a 可能為負，這意味著與球體相交的光線沒有 d 作為方向向量，而是-d（E.g.球體位於相機和螢幕後面）)

```py
# 相交判斷
def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None
```

### 最近相交對象
可以建立一個函數，用於 `sphere_intersect()` 尋找光線相交的最近的物件。只需遍歷所有球體，搜尋交叉點，並保留最近的球體。

呼叫函數時，如果 `nearest_object` 是 **None** 則表示沒有與射線相交的物體，否則其值為最近的相交物體從射線原點到交點 `min_distance` 的距離。

```py
# 最近相交判斷
def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None
```

### 交點
為了計算交點，使用前面的函數
```
nearest_object, distance = nearest_intersected_object(objects, o, d)
if nearest_object:
    intersection_point = o + d * distance
```

### 光交點
想知道從相交點開始並向光發出的光線在穿過光之前是否與場景中的物體相交，這只需要更改光線原點和方向。

首先，需要定義一盞燈(光源)：
```
light = { 'position': np.array([5, 5, 5]) }
```
要檢查物體是否遮擋交點，必須傳遞從交點開始並向光源發出的光線，查看返回的最近物體是否實際上比光源更接近交點（介於兩者之間）。


