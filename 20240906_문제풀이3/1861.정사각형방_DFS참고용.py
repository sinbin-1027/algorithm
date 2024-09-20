# 접근방법1
# 주석달기

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def DFS(sy, sx):
    global board, cnt
    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] == board[sy][sx] + 1:
                cnt += 1
                DFS(ny, nx)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_cnt, resulty, resultx = 0, 0, 0
    for y in range(N):
        for x in range(N):
            cnt = 1
            DFS(y, x)
            if max_cnt < cnt:
                max_cnt = cnt
                resulty = y
                resultx = x
            elif max_cnt == cnt and board[y][x] < board[resulty][resultx]:
                resulty = y
                resultx = x

    print(f'#{tc} {board[resulty][resultx]} {max_cnt}')