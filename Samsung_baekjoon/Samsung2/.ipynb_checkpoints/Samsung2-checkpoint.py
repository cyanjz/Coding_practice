from collections import deque
# row, reverse
# up, down, left, right
squeeze_directions = ((0, 0), (0, 1), (1, 0), (1, 1))

order_dict = {i : f'{i}' for i in range(10)}
for j in range(100):
    order_dict[10 + j] = chr(ord('A') + j)
r_order_dict = {v : k for k, v in order_dict.items()}


# squeeze begins at the start of the line.
# line should be ordered in the correct order
def squeeze_line(line, N):
    nums = []
    num = 0
    num_init = 1
    for c in line:
        if c != '0':
            if num == c:
                num = f'{order_dict[int(r_order_dict[num]) + 1]}'
                nums.pop(-1)
                nums.append(num)
                num = 0
            else:
                nums.append(c)
                num = c
    if nums:
        max_num = max([int(r_order_dict[x]) for x in nums])
    else:
        max_num = 0
    t = len(nums)
    new_line =  ''.join(nums) + '0' * (N-t)
    return (new_line, max_num)
    
def squeeze_board(b, d, N):
    lines = []
    if d[0]:
        for i in range(N):
            line = b[i * N: (i+1) * N]
            lines.append(line)
    else:
        for i in range(N):
            line = b[i::N]
            lines.append(line)
    if d[1]:
        lines_reverse = [x[::-1] for x in lines]
        lines = lines_reverse
    temp = [squeeze_line(x, N) for x in lines]
    squeezed_lines = [x[0] for x in temp]
    max_num = max([x[1] for x in temp])
    if d[1]:
        squeezed_lines = [x[::-1] for x in squeezed_lines]
    if d[0]:
        return ''.join(squeezed_lines), max_num
    else:
        rows = []
        for i in range(N):
            row = ''
            for col in squeezed_lines:
                row += col[i]
            rows.append(row)
        return ''.join(rows), max_num

def mod2(num):
    order = 0
    while num//2:
        num //= 2
        order += 1
    return order

def pb(b, N):
    for i in range(N):
        print(b[i * N : (i+1)*N])
    return 'print completed'

def sol():
    N = int(input())
    b = ''
    total_sum = 0
    for i in range(N):
        line = [int(x) for x in input().split()]
        total_sum += sum(line)
        line = [order_dict[mod2(num)] for num in line]
        b += ''.join(line)
    q = deque([(b, 0)])
    max_block = 0
    while q:
        cur_board, depth = q.popleft()
        for squeeze_direction in squeeze_directions:
            next_board, max_block_ = squeeze_board(cur_board, squeeze_direction, N)
            if depth + 1 <= 5:
                q.append((next_board, depth+1))
                if max_block < max_block_:
                    max_block = max_block_
            if 2**(max_block) == total_sum:
                print(total_sum)
                return 1
    print(2**(max_block))
    return 1

success = sol()