## 習題
> 各題原創或參考均標於程式開頭
### 習題一
> 寫出費氏數列的迴圈版

```python
# 原創

fib = [None]*1000
fib[0] = fib[1] = 1
n = int(input("Enter n : "))

if n==0:
    print(f'fibonacci({n}) = {0}')
else:
    for i in range(n-2):
        tn = 2 + i  # 從2開始
        fib[tn] = fib[tn-1] + fib[tn-2]
    print(f'fibonacci({n}) = {fib[n-1]}')
```
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題1> python .\fibonacci_loop.py
Enter n : 10
fibonacci(10) = 55
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題1> python .\fibonacci_loop.py
Enter n : 60
fibonacci(60) = 1548008755920
```
### 習題二
> 完成這個程式未寫的部分（記得加上測試程式）

```python
# 方法3 參考 : https://github.com/ccc112a/py2cs/blob/master/02-%E6%BC%94%E7%AE%97%E6%B3%95/02-%E6%96%B9%E6%B3%95/01-%E6%9F%A5%E8%A1%A8%E6%B3%95/fiboanacci/fibonacci_lookup.py
# 其餘原創

# 方法 1
def power2n_0(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_1(n):
    if n==0 or n==1: return n+1
    return power2n_1(n-1)+power2n_1(n-1)

# 方法 2b：用遞迴
def power2n_2(n):
    if n==0 or n==1: return n+1
    return 2*power2n_2(n-1)

# 方法 3：用遞迴+查表
def power2n_3(n):
    pow2 = [None]*1000
    pow2[0] = 1
    pow2[1] = 2
    if pow2[n] == None: return power2n_3(n-1)+power2n_3(n-1)
    else: return pow2[n]

n = int(input('Enter n : '))
print(f'power2n_0({n}) = {power2n_0(n)}')
print(f'power2n_1({n}) = {power2n_1(n)}')
print(f'power2n_2({n}) = {power2n_2(n)}')
print(f'power2n_3({n}) = {power2n_3(n)}')
```
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題2> python .\power2n.py
Enter n : 3
power2n_0(3) = 8
power2n_1(3) = 8
power2n_2(3) = 8
power2n_3(3) = 8
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題2> python .\power2n.py
Enter n : 16
power2n_0(16) = 65536
power2n_1(16) = 65536
power2n_2(16) = 65536
power2n_3(16) = 65536
```
### 習題三
> 寫出可以列舉所有排列的程式

```python
# 參考老師上課範例

def permutation(n):
    p = []
    return permNext(n, p)

def permNext(n, p):
    if len(p) == n:
        print(p)
        return
    for x in range(n):
        if x not in p:
            p.append(x)
            permNext(n, p)
            p.pop()

permutation(3)
```
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題3> python .\permutation.py
[0, 1, 2]
[0, 2, 1]
[1, 0, 2]
[1, 2, 0]
[2, 0, 1]
[2, 1, 0]
```
```python
# 原創

def truthtable(n, Curtable=[]):
    if n == 0:
        print(Curtable) 
    else:
        for value in [0, 1]:
            truthtable(n - 1, Curtable + [value])

truthtable(3)
```
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題3> python .\truthtable.py
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
```
### 習題四 : 求解方程式
> 求解方程式 x^2 - 3x + 1 = 0
> 暴力法、迭代法（至少寫三個迭代式，其中至少有一個收斂）

* 暴力法
    ```python
    # 參考老師上課範例

    # x^2 - 3x + 1 = 0
    from numpy import arange
    import math

    def f(x) :
        return x**2/3 - x + 1/3
        #return math.sin(x*x+2*x)/x*x*x 

    for x in arange(-100, 100, 0.001):
        if abs(f(x)) < 0.001:
            print("x=", x, " f(x)=", f(x)) 
    ```
    ```
    PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題4> python .\force.py
    x= 0.38100000047930394  f(x)= 0.0007203329757725641
    x= 0.3820000004793087  f(x)= -2.5333690578110968e-05
    x= 0.3830000004793135  f(x)= -0.0007703336902621372
    x= 2.6170000004899805  f(x)= -0.0007703329684611293
    x= 2.6180000004899853  f(x)= -2.5332968130953315e-05
    x= 2.61900000048999  f(x)= 0.0007203336988659825
    ```
* 迭代法
    ```python
    # f1-f3 原創 ， for 參考老師範例

    # x^2 - 3x + 1 = 0

    # x^2 = 3x -1 >>> x = 3 - 1/x
    # x^2 - 2x + 1 = x >>> x = (x-1)^2
    # x^2 + 1 = 3x >>> x = (x ^ 2 + 1) / 3 

    f1 = lambda x: 3 - 1 / x # 收斂 (3+5^-1)/2
    f2 = lambda x: (x - 1) ** 2 # 震盪(?
    f3 = lambda x: (x ** 2 + 1) / 3 # 收斂 (3-5^-1)/2

    x1 = x2 = x3 = 1.0

    for i in range(20):
        x1, x2, x3 = f1(x1), f2(x2), f3(x3)
        print('x1:', x1, '   x2:', x2, '   x3:', x3)
    ```
    ```
    PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題4> python .\iteration.py
    x1: 2.0    x2: 0.0    x3: 0.6666666666666666
    x1: 2.5    x2: 1.0    x3: 0.48148148148148145
    x1: 2.6    x2: 0.0    x3: 0.41060813900320076
    x1: 2.6153846153846154    x2: 1.0    x3: 0.389533014605224
    x1: 2.6176470588235294    x2: 0.0    x3: 0.3839119898224779
    x1: 2.6179775280898876    x2: 1.0    x3: 0.3824628053098181
    x1: 2.6180257510729614    x2: 0.0    x3: 0.3820925991484853
    x1: 2.6180327868852458    x2: 1.0    x3: 0.3819982514413483
    x1: 2.618033813400125    x2: 0.0    x3: 0.3819742213680825
    x1: 2.6180339631667064    x2: 1.0    x3: 0.38196810192991765
    x1: 2.618033985017358    x2: 0.0    x3: 0.381966543630648
    x1: 2.618033988205325    x2: 1.0    x3: 0.3819661468177146
    x1: 2.6180339886704433    x2: 0.0    x3: 0.3819660457715906
    x1: 2.618033988738303    x2: 1.0    x3: 0.381966020040795
    x1: 2.618033988748204    x2: 0.0    x3: 0.38196601348860165
    x1: 2.618033988749648    x2: 1.0    x3: 0.38196601182012485
    x1: 2.618033988749859    x2: 0.0    x3: 0.38196601139525727
    x1: 2.6180339887498896    x2: 1.0    x3: 0.38196601128706725
    x1: 2.618033988749894    x2: 0.0    x3: 0.38196601125951735
    x1: 2.618033988749895    x2: 1.0    x3: 0.3819660112525019
    ```
    
### 習題五:找任何向量函數的最高點
> 請寫一個爬山演算法程式可以找任何向量函數的最高點

```python
# 參考老師上課範例

import random

def hillClimbing(f, p, h=0.01):
    failCount = 0                      # 失敗次數歸零
    while (failCount < 10000):         # 如果失敗次數小於一萬次就繼續執行
        fnow = f(*p)                   # fxy 為目前高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:                 # 如果移動後高度比現在高
            fnow = f1                  # 就移過去
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0              # 失敗次數歸零
        else:                          # 若沒有更高
            failCount = failCount + 1  # 那就又失敗一次
    return (p, fnow)                   # 結束傳回 （已經失敗超過一萬次了）

def neighbor(f, p, h=0.01):
    p1 = p.copy()
    for i in range(len(p)): p1[i] += random.uniform(-h, h)
    f1 = f(*p1)
    return p1, f1

def f(x, y, z):
    return -1*(x**2+y**2+z**2)

print('\n', hillClimbing(f, [2,1,3]))
```
[result.txt](https://github.com/Jung217/alg112a/blob/master/%E7%BF%92%E9%A1%8C/%E7%BF%92%E9%A1%8C5/result.txt)
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題5> python .\hill.py
p= [2.0061222001008456, 0.9978834085457507, 2.9927393845117902] f(p)= -13.976786602396352
p= [2.0031026002754655, 0.9944344313605313, 2.988420705760097] f(p)= -13.931978180121352
p= [2.005726327550884, 0.9957941192482683, 2.9814565622684697] f(p)= -13.903627261653911
......
p= [-0.0003619797388151923, -0.0003829822759142355, -7.226271919820535e-05] f(p)= -2.8292665556308113e-07
p= [0.00033171994854868953, -0.00019450653005792257, -0.00032029498236213396] f(p)= -2.5045979022667847e-07
p= [0.0002444137977818924, 0.00020793127377092494, -2.7088546966082434e-05] f(p)= -1.0370730853490077e-07
p= [6.753990180640313e-05, 0.00020746960649199644, -2.5881103985881705e-05] f(p)= -4.8275107497490447e-08

([6.753990180640313e-05, 0.00020746960649199644, -2.5881103985881705e-05], -4.8275107497490447e-08)
```
### 習題六
> 寫一個梯度下降法程式可以找任何向量函數的谷底

```python
# 參考老師上課範例

import numpy as np
from numpy.linalg import norm

# 偏微分
def df(f, p, k ,step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

# 梯度下降
def gradDescendent(f, p0, step=0.01, max=100000, dp=10):
    p = p0.copy()
    fp0 = f(p)
    for i in range(max):
        fp = f(p)
        gp = grad(f, p) 
        glen = norm(gp) 
        if i % dp == 0: 
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
        if glen < 0.00001:
            break
        gstep = np.multiply(gp, -1*step) 
        p +=  gstep 
        fp0 = fp
    print('\n{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}\n'.format(i, fp, str(p), str(gp), glen))
    return p

def f(p):
    [x, y, z] = p
    return (x-5)**2+(y-1)**2+(z-3)**2

gradDescendent(f, [0.0, 0.0, 0.0])
```
[result.txt](https://github.com/Jung217/alg112a/blob/master/%E7%BF%92%E9%A1%8C/%E7%BF%92%E9%A1%8C6/result.txt)
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題6> python .\grad.py
00000:f(p)=35.000 p=[0.0, 0.0, 0.0] gp=[-9.98999999999981, -1.9899999999999807, -5.989999999999895] glen=11.81695
00010:f(p)=23.380 p=[0.91372133 0.18201256 0.54786694] gp=[-8.16255734 -1.62597489 -4.89426611] glen=9.65531
00020:f(p)=15.619 p=[1.66029818 0.33073007 0.99551412] gp=[-6.66940364 -1.32853986 -3.99897175] glen=7.88909
......
00670:f(p)=0.000 p=[4.99499339 0.99499868 2.99499604] gp=[-1.32140578e-05 -2.63222973e-06 -7.92314377e-06] glen=0.00002
00680:f(p)=0.000 p=[4.9949946  0.99499892 2.99499676] gp=[-1.07968473e-05 -2.15072334e-06 -6.47378532e-06] glen=0.00001
00690:f(p)=0.000 p=[4.99499559 0.99499912 2.99499736] gp=[-8.82181032e-06 -1.75729755e-06 -5.28955394e-06] glen=0.00001

00693:f(p)=0.000 p=[4.99499585 0.99499917 2.99499751] gp=[-8.30301730e-06 -1.65395440e-06 -4.97848585e-06] glen=0.00001
```
### 習題七
> 根據習題六的程式，改用 micrograd 的反傳遞算法算梯度

```py
#參考:https://github.com/ccc-py/micrograd/?tab=readme-ov-file#example-usage

from micrograd.engine import Value

a = Value(2.0)
b = Value(1.0)
c = Value(3.0)

for i in range(100000):
    step = 0.01
    f = a**2 + b**2 + c**2

    print('f(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))

    f.backward()
    if(a.grad < 0.001): break
    
    a -= a.grad * step
    b -= b.grad * step
    c -= c.grad * step
    
print('\nf(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))
```
[result.txt](https://github.com/Jung217/alg112a/blob/master/%E7%BF%92%E9%A1%8C/%E7%BF%92%E9%A1%8C7/result.txt)
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題7> python .\micro.py
f(p) = 14.0, p = [2.0, 1.0, 3.0]
f(p) = 13.445599999999999, p = [1.96, 0.98, 2.94]
f(p) = 12.91315424, p = [1.9208, 0.9604, 2.8811999999999998]
......
f(p) = 9.31232130542771e-07, p = [0.0005158161717242102, 0.0002579080858621051, 0.0007737242575863163]
f(p) = 8.943553381732774e-07, p = [0.000505499848289726, 0.000252749924144863, 0.0007582497724345899]
f(p) = 8.589388667816155e-07, p = [0.0004953898513239314, 0.0002476949256619657, 0.0007430847769858981]

f(p) = 8.589388667816155e-07, p = [0.0004953898513239314, 0.0002476949256619657, 0.0007430847769858981]
```
### 習題八
> 請選一位圖靈獎得主，詳細說明他的得獎原因

[HW8.md](https://github.com/Jung217/alg112a/blob/master/%E7%BF%92%E9%A1%8C/%E7%BF%92%E9%A1%8C8/HW8.md)
```
# 提姆·柏內茲-李
## 2016圖靈獎得主
> 發明了全球資訊網、第一個瀏覽器和使得全球資訊網得以擴充的基礎協定及演算法
## 背景
他的父母都是電腦科學家，且均參與過全球第一台商業電腦曼切斯特1型的研發。提姆在童年時期是個鐵道迷，他從焊接鐵道模型中學到了不少電子學知識。1973年至1976年間，他就讀於牛津大學王后學院，並獲得一級榮譽物理學士學位。在大學期間，購買了一台舊電視機製造了一台電腦。

## 困難與挑戰
伯納茲的發明背景涉及到他在歐洲核子研究中心（CERN）工作的經歷以及當時計算機科學和互聯網技術的背景。以下是一些關鍵方面：
* CERN的背景：在1989至1990間，伯納茲在日內瓦的CERN工作。CERN是一個國際性的高能物理研究機構，研究人員使用大型粒子加速器進行實驗，在這個環境中，資訊共享和交流是相當重要的。

* 資訊管理的挑戰：在工作中，研究者們通常使用各種不同的電腦系統和文件格式，使得資訊交流和協作變得相當困難，伯納茲意識到研究人員需要一種更有效的方式來管理和共享日益龐大的研究資料。
* 分布式系統的構想：面對這些挑戰，伯納茲開始構想一種分布式資訊系統，其中文件和資源可以通過超文本鏈接相互連接，形成一個網路。這就是後來成為全球資訊網的基本概念。
* 超文本和互聯網標準：伯納茲的構想包括了超文本（hypertext）的概念，使得文件能夠通過鏈接相互關聯。他還制定了用於創建網頁的標準，如HTML（超文本標記語言）和URL（統一資源定位器），這些標準成為後來互聯網上傳遞資訊的基石。
* 第一個網頁瀏覽器和服務器： 在構思了全球資訊網的概念後，伯納茲實際上創建了第一個網頁瀏覽器（WorldWideWeb）和服務器，使得用戶能夠瀏覽、搜尋和共享文件。

## 得獎原因 & 貢獻
1989年3月12日提出了資訊管理系統，並於11月中旬透過網際網路實現了超文本傳輸協定（HTTP）用戶端和伺服器之間的首次成功通信。1990年他在瑞士CERN的工作期間編寫了第一個網頁瀏覽器。網頁瀏覽器於1991年1月向其他研究機構發行，並於同年8月向大眾開放。他設計並實現了第一個網頁瀏覽器和Web伺服器，並幫助促進了Web隨後的爆炸性發展。他是全球資訊網協會(W3C)的創始人和董事。

## 參考
> **困難與挑戰**使用ChatGPT，其餘資訊來自下方連結 

[Tim_Berners-Lee - wiki](https://en.wikipedia.org/wiki/Tim_Berners-Lee)

[W3C - wiki](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium)

[The original proposal of the WWW, HTMLized](https://www.w3.org/History/1989/proposal.html)
```
### 習題九
> 用搜尋法求解下列問題 : 《狼、羊、甘藍菜》過河的問題

```py
# 參考改寫自:https://github.com/ccc112a/py2cs/blob/master/02-%E6%BC%94%E7%AE%97%E6%B3%95/02-%E6%96%B9%E6%B3%95/06-%E6%90%9C%E5%B0%8B%E6%B3%95/Q2-river/%E7%BF%92%E9%A1%8C%EF%BC%9A%E3%80%8A%E7%8B%BC%E3%80%81%E7%BE%8A%E3%80%81%E7%94%98%E8%97%8D%E8%8F%9C%E3%80%8B%E9%81%8E%E6%B2%B3%E7%9A%84%E5%95%8F%E9%A1%8C.md#%E7%BF%92%E9%A1%8C%E7%8B%BC%E7%BE%8A%E7%94%98%E8%97%8D%E8%8F%9C%E9%81%8E%E6%B2%B3%E7%9A%84%E5%95%8F%E9%A1%8C

objs = ["人", "狼", "羊", "菜"]
start = [0, 0, 0, 0]
goal = [1, 1, 1, 1]

visited_map = {}

def neighbors(s):
    side = s[0]
    next_states = [move(s, 0)]
    for i in range(1, len(s)):
        if s[i] == side: 
            if not is_dead(move(s, i)): next_states.append(move(s, i))
    return next_states

def is_dead(s):
    if s[1] == s[2] and s[1] != s[0]: return True # 狼吃羊
    if s[2] == s[3] and s[2] != s[0]: return True # 羊吃菜
    return False

def move(s, obj): # 人帶著物移到另一邊
    new_s = s.copy()
    side = s[0]
    another_side = 1 - side
    new_s[0] = another_side
    new_s[obj] = another_side
    return new_s

def visited(s):
    str_s = ''.join(map(str, s))
    return visited_map.get(str_s, False)

def dfs(s, path):
    if is_dead(s) or visited(s): return

    path.append(s)
    if s == goal:
        print("\nsuccess!", end="\n\n")
        for state in path: print('人{}  狼{}  羊{}  菜{}'.format(state[0], state[1], state[2], state[3]))
        print()
        return
    visited_map[''.join(map(str, s))] = True
    neighbors_list = neighbors(s)
    for neighbor in neighbors_list:
        dfs(neighbor, path.copy())
    path.pop()

dfs(start, [])
```
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題9> python .\river.py

success!

人0  狼0  羊0  菜0
人1  狼0  羊1  菜0
人0  狼0  羊1  菜0
人1  狼1  羊1  菜0
人0  狼1  羊0  菜0
人1  狼1  羊0  菜1
人0  狼1  羊0  菜1
人1  狼1  羊1  菜1

```
### 習題十
> 寫一個程式可以求解 n 次多項式

```py
# 改自習題五，if判斷參考:https://github.com/LeeYi-user/alg112a/blob/master/homework/10/homework.py
import random

def hillClimbing(f, init, h=0.01):
    p = init
    failCount = 0
    while failCount < 10000:
        fnow = f(p)
        neighbor = p.copy()

        for i in range(len(neighbor)): neighbor[i] += random.uniform(-h, h)
        f1 = f(neighbor)

        if f1 < fnow: # 參考
            if f1 <= 0 : break
            fnow = f1
            p = neighbor.copy()
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1
        
        if fnow < 0.001: break
    return p, fnow

def f(x):
    return x[0]**5 + 1

print('\n', hillClimbing(f, [0.0]))
```
[result.txt](https://github.com/Jung217/alg112a/blob/master/%E7%BF%92%E9%A1%8C/%E7%BF%92%E9%A1%8C10/result.txt)
```
PS C:\Users\alex2\Desktop\NQU\alg112a\習題\習題10> python .\Npoly.py
p= [-0.0038678122680304346] f(p)= 0.9999999999991344
p= [-0.008560028726282446] f(p)= 0.9999999999540404
p= [-0.009054236947401706] f(p)= 0.9999999999391502
...
p= [-0.9980717565364994] f(p)= 0.009604107714323185
p= [-0.9998929070815205] f(p)= 0.0005353499157475516

 ([-0.9998929070815205], 0.0005353499157475516)
```
### 習題十一
> 把從希爾伯特經圖靈到 NP-Complete 的故事寫下來

```
## User

請把從希爾伯特經圖靈到 NP-Complete 的故事，依時間順序寫成故事

希爾伯特第 2 問題
哥德爾完備，不完備定理
Church 與 Lambda Calculus
圖靈，圖靈機與停止問題
喬姆斯基階層與機器的關係
Steven Cook , SAT 與 NP-Complete

<br/>

## 來自 ChatGPT

當希爾伯特在二十世紀初提出他的第二問題，試圖建立一個完備的數學體系時，數學家們開始深入思考這個問題所牽涉到的基礎論問題。然而，哥德爾於 1931 年提出的不完備定理卻揭示了一個驚人的事實：任何包含基本算數的公理體系都無法同時是完備和一致的。這樣的發現震撼了數學界，並導致對數學基礎的重新思考。

在這個思考的背後，數學家和邏輯學家們逐漸將注意力轉向計算理論。Alonzo Church提出了Lambda Calculus，一個用來描述計算過程的抽象形式，而Alan Turing提出了圖靈機，這是一種理論上能模擬任何計算過程的抽象機器。這兩者的類似性表明，數學運算和計算過程可以以相似的方式進行，同時也揭示了一些問題是無法通過算法解決的，這正是圖靈提出的停止問題所探討的。

在計算理論的發展中，這些理論與語言學的交叉點逐漸浮現。語言學家Noam Chomsky提出了喬姆斯基階層，將語言分為多個層次，從有限的文法到無限的生成能力，同時探討了機器與語言的關係。這樣的理論連結了計算理論和語言學，為兩者之間的交互影響提供了基礎。

然後，斯蒂芬·庫克在 1971 年提出了著名的 SAT 問題，這是一個判斷布林表達式是否有解的問題。他進一步提出了 NP-Complete 的概念，這是一類問題，如果你能夠有效地解決其中一個，就能有效地解決所有 NP 問題。這開啟了計算理論中 P 與 NP 問題的研究方向，也深刻影響了計算機科學領域，特別是在算法效率和問題可解性方面的研究。

這條故事以希爾伯特的問題為起點，通過哥德爾的不完備定理、Lambda Calculus、圖靈機、喬姆斯基階層，最終引導到NP-Complete 的提出，串聯了數學基礎論、計算理論、語言學和計算機科學的發展。這一系列的理論探索不僅豐富了我們對數學和計算的理解，也深刻影響了現代計算機科學的發展脈絡。
```
