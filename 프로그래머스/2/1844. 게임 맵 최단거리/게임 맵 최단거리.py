import collections

def bfs(start , target , maps):
    
    search = {(-1,0),(0,1),(1,0),(0,-1)}
    q = collections.deque([(start[0], start[1], 1)])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[start[0]][start[1]] = True
    
    while q:
        x , y , num = q.popleft()
        if (x,y) == target:
            return num
        for sx , sy in search:
            nx = sx + x
            ny = sy + y
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx,ny,num+1))
    return -1

def solution(maps):
    start = (0,0)
    enemy = (len(maps)-1,len(maps[0])-1)
                
    enemySearch = bfs(start,enemy,maps)
    if enemySearch == -1:
        return -1
    return enemySearch
            