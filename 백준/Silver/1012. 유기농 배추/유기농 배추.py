from collections import deque

# 상하좌우 이동 방향
search = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    # 배추밭 초기화 (행: N, 열: M)
    farm = [[0] * M for _ in range(N)]
    
    # 배추 심기
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    # 배추흰지렁이 수
    baechooWorm = 0
    
    # 배추밭 탐색
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:  # 배추가 심어진 위치 발견
                # BFS 시작
                q = deque([(i, j)])
                farm[i][j] = 0  # 방문한 배추는 0으로 변경
                
                while q:
                    x, y = q.popleft()
                    
                    for sx, sy in search:
                        nx, ny = x + sx, y + sy
                        if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                            farm[nx][ny] = 0  # 방문한 배추는 0으로 변경
                            q.append((nx, ny))
                
                # 하나의 배추흰지렁이로 모든 인접 배추를 처리
                baechooWorm += 1
    
    # 결과 출력
    print(baechooWorm)