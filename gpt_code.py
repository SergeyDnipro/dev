import heapq


def dijkstra(graph, start):
    # Инициализация расстояний до всех вершин как бесконечность, кроме начальной
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Расстояние до начальной вершины равно 0
    # Создание очереди с приоритетом для хранения вершин и их расстояний
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)  # Извлечение вершины с наименьшим расстоянием
        # Если расстояние до текущей вершины больше, чем сохраненное в distances, пропускаем её
        if current_distance > distances[current_vertex]:
            continue
        # Обходим соседей текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # Рассчитываем новое расстояние до соседа
            # Если новое расстояние меньше, чем сохраненное в distances, обновляем его
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))  # Добавляем соседа в очередь с приоритетом
    return distances


# Пример графа в виде словаря с весами ребер
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {}
}

start_vertex = 'A'
result = dijkstra(graph, start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex}:")
for vertex, distance in result.items():
    print(f"До вершины {vertex}: {distance}")
