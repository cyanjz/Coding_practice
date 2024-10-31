dr_list, dc_list = [1, -1, 0, 0], [0, 0, 1, -1]

def solve(class_room, students):
    
    neigh = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            nei = []
            for k in range(4):
                nr, nc = r + dr_list[k], c + dc_list[k]
                if 0 <= nr < N and 0 <= nc < N:
                    nei.append((nr, nc))
            neigh[r][c] = nei

    students_dict = {}
    
    for student in students:
        st_id = student[0]
        friends = student[1:]
        students_dict[st_id] = friends

        cr, cc = -1, -1
        max_empty, max_friendly = 0, 0
        for r in range(N):
            for c in range(N):
                if not class_room[r][c]:
                    if cr == -1:
                        cr, cc = r, c
                    empty, friendly = 0, 0
                    for nr, nc in neigh[r][c]:
                        nei_type = class_room[nr][nc]
                        if not nei_type:
                            empty += 1
                        elif nei_type in friends:
                            friendly += 1
                    if max_friendly < friendly:
                        max_friendly = friendly
                        max_empty = empty
                        cr, cc = r, c
                    elif max_friendly == friendly:
                        if max_empty < empty:
                            max_empty = empty
                            cr, cc = r, c
        class_room[cr][cc] = st_id
    total_satisfaction = 0
    for r in range(N):
        for c in range(N):
            number_of_friends = 0
            friends = students_dict[class_room[r][c]]
            for nr, nc in neigh[r][c]:
                if class_room[nr][nc] in friends:
                    number_of_friends += 1
            if number_of_friends:
                total_satisfaction += 10**(number_of_friends-1)
    print(total_satisfaction)
    return

if __name__ == '__main__':
    N = int(input())
    # std_id, f_id1, ..
    students = [[int(x) for x in input().split()] for _ in range(N**2)]
    class_room = [[0] * N for _ in range(N)]
    solve(class_room, students)
    