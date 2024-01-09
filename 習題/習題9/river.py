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