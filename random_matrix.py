from random import random, choice
import pprint


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


matr = [[rand() for x in range(4)] for y in range(4)]

max_matr = len(matr) - 1
graph = {}

for i in range(max_matr + 1):
    for j in range(max_matr + 1):
        if i == max_matr and j == max_matr:
            graph[f"{i}{j}"] = {}
        elif i == max_matr:
            graph[f"{i}{j}"] = {f"{i}{j + 1}": matr[i][j + 1]}
        elif j == max_matr:
            graph[f"{i}{j}"] = {f"{i + 1}{j}": matr[i + 1][j]}
        else:
            graph[f"{i}{j}"] = {f"{i + 1}{j}": matr[i + 1][j], f"{i}{j + 1}": matr[i][j + 1]}

costs = {vertex: float('infinity') for vertex in graph}
costs['01'] = graph['00']['01']
costs['10'] = graph['00']['10']

parents = {vertex: None for vertex in graph}
parents.pop('00')
parents['10'] = '00'
parents['01'] = '00'

processed = []

node = find_min_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for vertex in neighbors.keys():
        new_cost = cost + neighbors[vertex]
        if new_cost < costs[vertex]:
            costs[vertex] = new_cost
            parents[vertex] = node
    processed.append(node)
    node = find_min_node(costs)

print(node)
print(graph)
print(*parents.items(), sep='\n')
print(costs)
print(*matr, sep='\n')

start_value = '33'
start_key = ''
parents_copy = parents.copy()
while parents_copy:
    for key in parents:
        if key == start_value:
            start_value = parents[key]
            print(key, end=' ')
            parents_copy.pop(key)
            if parents[key] not in parents_copy:
                print(parents[key])
                parents_copy.clear()