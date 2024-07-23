from collections import deque

search = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def bfs(x,y):
    q = deque([(x,y)])
    island[x][y] = 0
    while q:
        x,y = q.popleft()
        for sx , sy in search:
            nx , ny = x + sx , y + sy
            if 0 <= nx < h and 0 <= ny < w:
                if island[nx][ny] == 1:
                    island[nx][ny] = 0
                    q.append((nx,ny))
while True:
    w, h = map(int, input().split())
    if w== 0 and h == 0:
        break
    count = 0
    island = []

    for _ in range(h):
        island.append(list(map(int,input().split())))

    for x in range(h):
        for y in range(w):
            if island[x][y] ==1:
                bfs(x,y)
                count += 1

    print(count)