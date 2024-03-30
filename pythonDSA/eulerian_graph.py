import networkx as nx

graph = nx.Graph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
eulerian_path = list(nx.eulerian_path(graph))
print(eulerian_path)


# grid = nx.MultiGraph(nx.grid_2d_graph(m=4, n=4))
# grid = nx.eulerian_path(grid)
# cycle = nx.eulerian_circuit(grid, source=(0, 0))
# print('->'.join(str(edge[0]) for edge in cycle))


# Create a 7x7 grid graph
grid = nx.grid_2d_graph(m=7, n=7)

# Identify nodes with odd degree
odd_degree_nodes = [node for node, degree in grid.degree() if degree % 2 == 1]

# Add additional edges to make odd-degree nodes even-degree
for node in odd_degree_nodes:
    grid.add_edge(node, 'extra_node')

# Compute an Eulerian circuit on the modified grid graph
circuit = nx.eulerian_circuit(grid)

# Print the nodes of the Eulerian circuit
for node, _ in circuit:
    print(node)
