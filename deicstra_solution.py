def find_min_node(costs):
    min_cost = float('infinity')
    min_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < min_cost and node not in processed:
            min_cost = cost
            min_cost_node = node
    return min_cost_node


graph = {}

graph['A'] = {'B': 5, 'C': 2}
graph['B'] = {'D': 4, 'E': 2}
graph['C'] = {'B': 8, 'E': 7}
graph['D'] = {'E': 6, 'F': 3}
graph['E'] = {'F': 1}
graph['F'] = {}



print(graph)

inf = float('infinity')
costs = {}
costs['B'] = 5
costs['C'] = 2
costs['D'] = inf
costs['E'] = inf
costs['F'] = inf


parents = {}
parents['B'] = 'A'
parents['C'] = 'A'
parents['D'] = None
parents['E'] = None
parents['F'] = None


processed = []

node = find_min_node(costs)
print(node)
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

print(parents)
print(costs)
start_value = 'F'
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

