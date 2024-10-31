s_colors = ['w', 'y', 'r', 'o', 'g', 'b']
# U, D, F, B, L, R
# clockwise order
adjs = [['B', 'R', 'F', 'L'], ['L', 'F', 'R', 'B'], ['U', 'R', 'D', 'L'], ['L', 'D', 'R', 'U'], ['U', 'B', 'D', 'F'], ['F', 'D', 'B', 'U']]
# d 5 * 5 * 5 size의 matrix -> 회전 -> 답.
# cube는 위에서 부터 만들기.
class Cube:
    # build 5 * 5 * 5 matrix
    def __init__(self, sc):
        self.c = [[row[:] for row in slice] for slice in sc]
        
    def U(self, direction):
        self.c[0] = [list(x) for x in zip(*self.c[0])]
        self.c[1] = [list(x) for x in zip(*self.c[1])]
        if direction:
            for row in self.c[0]:
                row.reverse()
            for row in self.c[1]:
                row.reverse()
        else:
            self.c[0].reverse()
            self.c[1].reverse()
    def D(self, direction):
        self.c[4] = [list(x) for x in zip(*self.c[4])]
        self.c[3] = [list(x) for x in zip(*self.c[3])]
        if not direction:
            for row in self.c[4]:
                row.reverse()
            for row in self.c[3]:
                row.reverse()
        else:
            self.c[4].reverse()
            self.c[3].reverse()
    def R(self, direction):
        temp1 = [[self.c[i][j][4]  for j in range(5)] for i in range(5)]
        temp2 = [[self.c[i][j][3]  for j in range(5)] for i in range(5)]
        temp1 = [list(x) for x in zip(*temp1)]
        temp2 = [list(x) for x in zip(*temp2)]
        if not direction:
            for row in temp1:
                row.reverse()
            for row in temp2:
                row.reverse()
        else:
            temp1.reverse()
            temp2.reverse()
        for i in range(5):
            for j in range(5):
                self.c[i][j][4] = temp1[i][j]
                self.c[i][j][3] = temp2[i][j]
    def L(self, direction):
        temp1 = [[self.c[i][j][0]  for j in range(5)] for i in range(5)]
        temp2 = [[self.c[i][j][1]  for j in range(5)] for i in range(5)]
        temp1 = [list(x) for x in zip(*temp1)]
        temp2 = [list(x) for x in zip(*temp2)]
        if direction:
            for row in temp1:
                row.reverse()
            for row in temp2:
                row.reverse()
        else:
            temp1.reverse()
            temp2.reverse()
        for i in range(5):
            for j in range(5):
                self.c[i][j][0] = temp1[i][j]
                self.c[i][j][1] = temp2[i][j]
    def F(self, direction):
        temp1 = [self.c[i][4] for i in range(5)]
        temp2 = [self.c[i][3] for i in range(5)]
        temp1 = [list(x) for x in zip(*temp1)]
        temp2 = [list(x) for x in zip(*temp2)]
        if direction:
            for row in temp1:
                row.reverse()
            for row in temp2:
                row.reverse()
        else:
            temp1.reverse()
            temp2.reverse()
        for i in range(5):
            self.c[i][4] = temp1[i]
            self.c[i][3] = temp2[i]
    def B(self, direction):
        temp1 = [self.c[i][0] for i in range(5)]
        temp2 = [self.c[i][1] for i in range(5)]
        temp1 = [list(x) for x in zip(*temp1)]
        temp2 = [list(x) for x in zip(*temp2)]
        if not direction:
            for row in temp1:
                row.reverse()
            for row in temp2:
                row.reverse()
        else:
            temp1.reverse()
            temp2.reverse()
        for i in range(5):
            self.c[i][0] = temp1[i]
            self.c[i][1] = temp2[i]
    def rotate(self, r):
        d = 1 if r[1] == '+' else 0
        if r[0] == 'U':
            self.U(d)
        elif r[0] == 'D':
            self.D(d)
        elif r[0] == 'F':
            self.F(d)
        elif r[0] == 'B':
            self.B(d)
        elif r[0] == 'R':
            self.R(d)
        elif r[0] == 'L':
            self.L(d)
sc = []
sc.append([['0', '0', '0', '0', '0']] + [['0', 'w', 'w', 'w', '0'] for _ in range(3)] + [['0', '0', '0', '0', '0']])
for __ in range(3):
    sc.append([['0', 'o', 'o', 'o', '0']]+[['g','0','0','0','b'] for _ in range(3)]+[['0', 'r', 'r', 'r', '0']])
sc.append([['0', '0', '0', '0', '0']] + [['0', 'y', 'y', 'y', '0'] for _ in range(3)] + [['0', '0', '0', '0', '0']])

def solve():
    us = []
    T = int(input())
    for _ in range(T):
        cube = Cube(sc)
        N = int(input())
        rs = input().split()
        for r in rs:
            cube.rotate(r)
        us.append(cube.c[0])
        del cube
    for u in us:
        for row in u[1:4]:
            print(''.join(row[1:4]))
solve()