# def print(txt):
#     fp.write(f'{txt}\n')
#     return

# def input():
#     return fp_in.readline().rstrip()

class Node:
    def __init__(self, cmd):
        self.m_id, self.p_id, self.color, self.max_depth = cmd
        self.child = []

class Tree:
    def __init__(self, cmd):
        self.root = Node(cmd)
        self.node_info = {self.root.m_id : self.root}

    def add_node(self, cmd):
        self.updated = 0
        new_node = Node(cmd)
        if new_node.p_id == self.root.m_id:
            if self.root.max_depth != 1:
                if new_node.max_depth >= self.root.max_depth:
                    new_node.max_depth = self.root.max_depth - 1
                    self.root.child.append(new_node.m_id)
                    self.node_info[new_node.m_id] = new_node
                    self.updated = 1
                elif new_node.max_depth < self.root.max_depth:
                    self.root.child.append(new_node.m_id)
                    self.node_info[new_node.m_id] = new_node
                    self.updated = 1
        else:
            q = [self.root.m_id]
            found = 0
            while q:
                cur_node = self.node_info[q.pop()]
                if found:
                    break
                if cur_node.max_depth == 1:
                    continue
                for c_id in cur_node.child:
                    if c_id == new_node.p_id:
                        found = 1
                        if self.node_info[c_id].max_depth != 1:
                            if new_node.max_depth >= self.node_info[c_id].max_depth:
                                new_node.max_depth = self.node_info[c_id].max_depth - 1
                                self.node_info[c_id].child.append(new_node.m_id)
                                self.node_info[new_node.m_id] = new_node
                                self.updated = 1
                            elif new_node.max_depth < self.node_info[c_id].max_depth:
                                self.node_info[c_id].child.append(new_node.m_id)
                                self.node_info[new_node.m_id] = new_node
                                self.updated = 1
                    else:
                        q.append(c_id)

    def change_color(self, cmd):
        m_id, color = cmd
        # bfs find m_id
        if self.root.m_id == m_id:
            target = self.root.m_id
        else:
            found = 0
            q = [self.root.m_id]
            while q:
                cur_node = self.node_info[q.pop()]
                if found:
                    break
                for c_id in cur_node.child:
                    if c_id == m_id:
                        found = 1
                        target = c_id
                    else:
                        q.append(c_id)
        # bfs to change colors
        q = [target]
        while q:
            cur_id = q.pop()
            try:
                cur_node = self.node_info[cur_id]
            except:
                breakpoint()
            cur_node.color = color
            for c_id in cur_node.child:
                q.append(c_id)
    def search_color(self, cmd):
        m_id = cmd[0]
        print(self.node_info[m_id].color)
    def calc_score(self):
        ans = 0
        def dfs_scoring(m_id):
            nonlocal ans
            colors = [self.node_info[m_id].color]
            if self.node_info[m_id].child:
                for c_id in self.node_info[m_id].child:
                    colors.extend(dfs_scoring(c_id))
                    colors = list(set(colors))
            ans += len(colors)**2
            return colors
        dfs_scoring(self.root.m_id)
        self.score = ans
            


if __name__ == '__main__':
    # fp = open('output.txt', 'w')
    # fp_in = open('input.txt', 'r')
    Q = int(input())
    tree_list = []
    change_log = []
    for _ in range(Q):
        cmd = list(map(int, input().split()))
        if cmd[0] == 100:
            if cmd[2] == -1:
                new_Tree = Tree(cmd[1:])
                tree_list.append(new_Tree)
                change_log.append(1)
            else:
                for i, tree in enumerate(tree_list):
                    if cmd[2] in tree.node_info.keys():
                        tree.add_node(cmd[1:])
                        change_log[i] = 1
                        break
        elif cmd[0] == 200:
            for i, tree in enumerate(tree_list):
                if cmd[1] in tree.node_info.keys():
                    tree.change_color(cmd[1:])
                    change_log[i] = 1
                    break
        elif cmd[0] == 300:
            for tree in tree_list:
                target_node = tree.node_info.get(cmd[1])
                if target_node:
                    print(target_node.color)
                    break
        elif cmd[0] == 400:
            ans = 0
            for i, tree in enumerate(tree_list):
                if change_log[i]:
                    tree.calc_score()
                ans += tree.score
            print(ans)
    # for node in tree.node_info.values():
    #     print(node.m_id, node.p_id, node.color, node.max_depth, node.child)