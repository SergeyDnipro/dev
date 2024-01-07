from random import random, choice
import heapq


def find_min_node(costs):
    min_cost = float('infinity')
    min_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < min_cost and node not in processed:
            min_cost = cost
            min_cost_node = node
    return min_cost_node

def rand():
    return choice(range(10))


matr = [[rand() for x in range(5)] for y in range(5)]

max_matr = len(matr) - 1
graph = {}

for i in range(max_matr, -1, -1):
    for j in range(max_matr + 1):
        if i == 0 and j == max_matr:
            graph[f"{i}{j}"] = {}
        elif i == 0:
            graph[f"{i}{j}"] = {f"{i}{j + 1}": matr[i][j + 1]}
        elif j == max_matr:
            graph[f"{i}{j}"] = {f"{i - 1}{j}": matr[i - 1][j]}
        else:
            graph[f"{i}{j}"] = {f"{i - 1}{j}": matr[i - 1][j], f"{i}{j + 1}": matr[i][j + 1]}

costs = {vertex: float('infinity') for vertex in graph}
costs['40'] = matr[4][0]
# costs['01'] = graph['00']['01']
# costs['10'] = graph['00']['10']

parents = {vertex: None for vertex in graph}
parents.pop('40')
parents['30'] = '40'
parents['41'] = '40'

processed = []

# node = find_min_node(costs)
node = [(matr[4][0], '40')]
while node:
    current_cost, peak = heapq.heappop(node)
    if current_cost > costs[peak]:
        continue
    # cost = costs[node]
    # neighbors = graph[node]
    for vertex, weight in graph[peak].items():
        new_cost = current_cost + weight
        if new_cost < costs[vertex]:
            costs[vertex] = new_cost
            parents[vertex] = peak
            heapq.heappush(node, (new_cost, vertex))
    processed.append(node)
    # node = find_min_node(costs)

print(node)
print(graph)
print(*parents.items(), sep='\n')
print(costs)
print(*matr, sep='\n')

start_value = '04'
final_list = []
parents_copy = parents.copy()
while parents_copy:
    for key in parents:
        if key == start_value:
            start_value = parents[key]
            final_list.append(key)
            parents_copy.pop(key)
            if parents[key] not in parents_copy:
                final_list.append(parents[key])
                parents_copy.clear()
print(*final_list[-1::-1])
