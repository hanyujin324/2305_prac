import heapq

def dijkstra(graph, start):
    # 시작 노드에서부터의 최단 거리를 저장하는 딕셔너리
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드의 최단 거리는 0
    queue = [(0, start)]  # 우선순위 큐를 사용하여 처리할 노드들을 저장

    while queue:
        current_distance, current_node = heapq.heappop(queue)  # 최단 거리가 가장 작은 노드 선택

        # 이미 처리된 노드라면 건너뜀
        if current_distance > distances[current_node]:
            continue

        # 현재 노드와 연결된 인접한 노드들을 순회
        for adjacent_node, weight in graph[current_node].items():
            distance = current_distance + weight  # 현재 노드를 거쳐 가는 경로의 거리

            # 더 짧은 경로를 찾았을 때 업데이트
            if distance < distances[adjacent_node]:
                distances[adjacent_node] = distance
                heapq.heappush(queue, (distance, adjacent_node))

    return distances

# 그래프 생성 (인접 리스트로 표현)
graph = {
    'E1': {'E2': 7.7, 'D1': 29.1},
    'E2': {'E1': 7.7, 'E3': 12.9,'D1':32.6},
    'E3': {'E2': 12.9, 'E4': 5.5,'E19':6.8,'D1':24.3},
    'E4': {'E3': 5.5, 'E5': 14.7, 'E12': 19.2,'E19':10.1,'F3':7.1},
    'E5': {'E4':14.7,'E6': 17.5,'E18':20},
    'E6': {'E5':17.5},
    'E12': {'E4':19.2,'F3':14.2},
    'E18': {'E5':20,'E6': 7.3},
    'E19': {'E3':6.8,'E4': 10.1,'F1':10.5,'D1':19.6},
    'F1': {'E19':10.5,'D1': 14.4},
    'F3': {'E4':7.1,'E12': 14.2,'E19':14.2},
    'D1': {'E1': 29.1,'E2':32.6,'E3':24.3,'E19':19.6,'F1':14.4}
}

start_node = 'E4'
distances = dijkstra(graph, start_node)

# F1과 F3 중 D1으로 가는 가장 빠른 방법 찾기
fastest_path = float('inf')
for node in ['F1', 'F3']:
    distance = distances.get(node, float('inf'))
    if distance < fastest_path:
        fastest_path = distance

# D1로 가는 가장 빠른 방법 출력
if fastest_path == float('inf'):
    print("D1로 가는 경로가 없습니다.")
else:
    print(f"D1로 가는 가장 빠른 방법의 최단 거리: {fastest_path:.1f}")