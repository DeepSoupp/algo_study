def solution(tickets):
    from collections import defaultdict, deque
    
    # 1. 그래프 생성
    routes = defaultdict(list)
    for start, end in tickets:
        routes[start].append(end)
    
    # 2. 각 출발 공항의 도착지 리스트를 역순으로 정렬
    for key in routes:
        routes[key].sort(reverse=True)
    
    # 3. DFS 알고리즘으로 경로를 생성
    stack = ["ICN"]
    path = []
    
    while stack:
        airport = stack[-1]
        
        if airport not in routes or not routes[airport]:
            path.append(stack.pop())
        else:
            stack.append(routes[airport].pop())
    
    return path[::-1]



코드 설명
그래프 구성:

defaultdict를 사용하여 출발지에서 도착지로 가는 항공권을 저장합니다.
각 공항에서 도착지 목록을 역순으로 정렬하여 BFS에서 먼저 방문할 수 있도록 합니다.
DFS 탐색:

스택을 사용하여 DFS를 구현합니다.
현재 공항에서 도착할 수 있는 공항이 없으면 현재 공항을 경로에 추가하고, 스택에서 제거합니다.
도착할 수 있는 공항이 있으면 해당 공항을 스택에 추가하고, 그래프에서 제거합니다.
경로 생성:

DFS 탐색이 완료된 후, 경로를 역순으로 반환합니다.
이 개선된 코드는 BFS 대신 DFS를 사용하여 문제를 해결하며, 각 단계에서 가장 사전 순으로 앞서는 경로를 보장합니다.
