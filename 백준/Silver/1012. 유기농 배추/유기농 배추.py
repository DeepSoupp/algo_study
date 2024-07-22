from collections import deque


search = [(-1,0),(0,1),(1,0),(0,-1)]

T = int(input())
for _ in range(T):
    M, N, k = map(int, input().split())
    # 배추밭을 만들어주어요
    farm = [[0] * M for _ in range(N)]
    for __ in range(k):
        # 배추를 심어주어요
        x, y = map(int, input().split())
        farm[y][x] = 1
        
    baechooWorm = 0
    
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                q = deque([(i,j)])
                farm[i][j] = 0
                while q:
                    x ,y = q.popleft()
                    for sx, sy in search:
                        nx, ny = x + sx, y + sy
                        if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                            farm[nx][ny] = 0
                            q.append((nx,ny))
                            
                baechooWorm += 1
                            
                            
    print(baechooWorm)