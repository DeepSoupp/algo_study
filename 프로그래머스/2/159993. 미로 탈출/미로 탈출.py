import collections

def bfs(start , target , maps):
    
    search = {(-1,0),(0,1),(1,0),(0,-1)} 
    q = collections.deque([(start[0], start[1], 0)])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[start[0]][start[1]] = True
    
    while q:
        x , y , time = q.popleft()
        if (x,y) == target:
            return time
        for sx , sy in search:
            nx = sx + x
            ny = sy + y
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx,ny,time+1))
    return -1

def solution(maps):
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
            if maps[i][j] == 'E':
                eexxiitt = (i,j)
                
    leverSearch = bfs(start,lever,maps)
    exitSearch = bfs(lever,eexxiitt,maps)
    
    if leverSearch == -1 or exitSearch == -1:
        return -1
    
    return leverSearch+exitSearch