# class 없이 함수로 정의해보자.
# def print(txt):
#     fp_out.write(f'{txt}\n')
#     return

# def input():
#     return fp_in.readline().rstrip()

# fp_in = open('input.txt', 'r')
# fp_out = open('output.txt', 'w')

# node 구성 : [m_id, p_id, color, max_depth, childrens]
# list에 넣고, index = m_id가 되도록 관리.
# node를 제거하는 경우는 없음!
def add_node(cmd, cur_m_id):
    global nodes, roots, m_id_dict
    m_id, p_id, color, max_depth = cmd[1:]
    p_id = m_id_dict[p_id]
    if p_id == -1:
        nodes.append([cur_m_id, p_id, color, max_depth, []])
        roots.append(cur_m_id)
        m_id_dict[m_id] = cur_m_id
        return 1
    else:
        try:
            p_max_depth = nodes[p_id][3]
        except:
            breakpoint()
        if p_max_depth != 1:
            if p_max_depth > max_depth:
                nodes[p_id][4].append(cur_m_id)
                nodes.append([cur_m_id, p_id, color, max_depth, []])
                m_id_dict[m_id] = cur_m_id
                return 1
            else:
                nodes[p_id][4].append(cur_m_id)
                nodes.append([cur_m_id, p_id, color, p_max_depth-1, []])
                m_id_dict[m_id] = cur_m_id
                return 1
    return 0

def change_colors(cmd):
    global nodes
    m_id, color = cmd[1:]
    q = [m_id_dict[m_id]]
    while q:
        cur_idx = q.pop(0)
        nodes[cur_idx][2] = color
        q.extend(nodes[cur_idx][4])
    return

def search_color(cmd):
    m_id = cmd[1]
    print(nodes[m_id_dict[m_id]][2])
    return

def score(cmd):
    ans = 0
    
    def dfs(cur_idx):
        nonlocal ans
        cur_node = nodes[cur_idx]
        colors = [cur_node[2]]
        if cur_node[4]:
            for c_id in cur_node[4]:
                colors.extend(dfs(c_id))
                colors = list(set(colors))
        ans += len(colors)**2
        return colors
        
    for m_idx in roots:
        dfs(m_idx)
    print(ans)
    return

Q = int(input())
cur_m_id = 0
roots = []
nodes = []
m_id_dict = dict()
m_id_dict[-1] = -1
for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 100:
        # add node
        # 100 m_id p_id color max_depth
        update = add_node(cmd, cur_m_id)
        if update:
            cur_m_id += 1
        pass
    elif cmd[0] == 200:
        # change color
        # 200 m_id color
        change_colors(cmd)
        pass
    elif cmd[0] == 300:
        # search color
        # 300 m_id
        search_color(cmd)
        pass
    elif cmd[0] == 400:
        # calculate score for each sub trees
        # 400
        score(cmd)
        pass


# fp_in.close()
# fp_out.close()