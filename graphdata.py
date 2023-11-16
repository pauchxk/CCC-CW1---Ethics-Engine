import dijkstra

#example 1 - small scale graph#
'''g = Graph()
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addNode('F')

g.addEdge('A', 'B', 15)
g.addEdge('A', 'C', 15)
g.addEdge('B', 'C', 16)
g.addEdge('B', 'D', 14)
g.addEdge('C', 'D', 7)
g.addEdge('C', 'E', 14)
g.addEdge('D', 'E', 10)
g.addEdge('D', 'F', 11)
g.addEdge('E', 'F', 12)'''

#example 2 - large scale town graph#
town = dijkstra.Graph()
# Adding nodes
town.addNode('A')
town.addNode('A1')
town.addNode('A2')
town.addNode('A3')
town.addNode('A4')
town.addNode('A5')
town.addNode('A6')
town.addNode('A7')
town.addNode('A8')
town.addNode('A9')
town.addNode('A10')
town.addNode('A11')
town.addNode('A12')
town.addNode('A13')
town.addNode('A14')
town.addNode('A15')
town.addNode('A16')
town.addNode('A17')
town.addNode('A18')
town.addNode('A19')
town.addNode('A20')
town.addNode('A21')
town.addNode('A22')
town.addNode('A23')
town.addNode('A24')
town.addNode('A25')
town.addNode('A26')
town.addNode('A27')
town.addNode('A28')
town.addNode('A29')
town.addNode('A30')
town.addNode('A31')
town.addNode('B')

# Adding edges (risk data)
'''town.addEdge('A', 'A1', 5)
town.addEdge('A1', 'A', 5)
town.addEdge('A1', 'A2', 9)
town.addEdge('A1', 'A10', 22)
town.addEdge('A1', 'A4', 13)
town.addEdge('A1', 'A9', 24)
town.addEdge('A1', 'A8', 20)

town.addEdge('A2', 'A1', 9)
town.addEdge('A2', 'A3', 5)
town.addEdge('A2', 'A11', 9)

town.addEdge('A3', 'A2', 5)
town.addEdge('A3', 'A12', 5)

town.addEdge('A4', 'A1', 13)
town.addEdge('A4', 'A5', 5)
town.addEdge('A4', 'A7', 5)

town.addEdge('A5', 'A4', 5)
town.addEdge('A5', 'A6', 5)
town.addEdge('A6', 'A5', 5)
town.addEdge('A6', 'A7', 7)
town.addEdge('A6', 'A13', 5)

town.addEdge('A7', 'A6', 7)
town.addEdge('A7', 'A4', 5)
town.addEdge('A7', 'A8', 11)
town.addEdge('A7', 'A14', 12)

town.addEdge('A8', 'A7', 11)
town.addEdge('A8', 'A1', 20)
town.addEdge('A8', 'A9', 20)
town.addEdge('A8', 'A15', 22)

town.addEdge('A9', 'A8', 20)
town.addEdge('A9', 'A16', 28)
town.addEdge('A9', 'A10', 20)
town.addEdge('A9', 'A1', 24)

town.addEdge('A10', 'A9', 20)
town.addEdge('A10', 'A11', 7)
town.addEdge('A10', 'A1', 22)
town.addEdge('A10', 'A17', 24)

town.addEdge('A11', 'A10', 7)
town.addEdge('A11', 'A18', 10)
town.addEdge('A11', 'A2', 9)
town.addEdge('A11', 'A12', 5)
town.addEdge('A11', 'A17', 12)

town.addEdge('A12', 'A11', 5)
town.addEdge('A12', 'A3', 5)
town.addEdge('A12', 'A19', 7)

town.addEdge('A13', 'A6', 5)
town.addEdge('A13', 'A14', 7)
town.addEdge('A13', 'A21', 5)

town.addEdge('A14', 'A13', 7)
town.addEdge('A14', 'A7', 12)
town.addEdge('A14', 'A15', 14)
town.addEdge('A14', 'A24', 12)
town.addEdge('A14', 'A21', 10)

town.addEdge('A15', 'A14', 14)
town.addEdge('A15', 'A16', 20)
town.addEdge('A15', 'A8', 22)
town.addEdge('A15', 'A24', 24)

town.addEdge('A16', 'A15', 20)
town.addEdge('A16', 'A17', 20)
town.addEdge('A16', 'A9', 28)
town.addEdge('A16', 'A25', 28)

town.addEdge('A17', 'A16', 20)
town.addEdge('A17', 'A10', 24)
town.addEdge('A17', 'A11', 12)
town.addEdge('A17', 'A18', 10)
town.addEdge('A17', 'A26', 22)

town.addEdge('A18', 'A17', 10)
town.addEdge('A18', 'A19', 5)
town.addEdge('A18', 'A20', 12)
town.addEdge('A18', 'A11', 10)

town.addEdge('A19', 'A18', 5)
town.addEdge('A19', 'A12', 7)
town.addEdge('A19', 'A20', 5)

town.addEdge('A20', 'A19', 5)
town.addEdge('A20', 'A18', 12)
town.addEdge('A20', 'A27', 14)
town.addEdge('A20', 'A28', 5)

town.addEdge('A21', 'A22', 5)
town.addEdge('A21', 'A23', 10)
town.addEdge('A21', 'A13', 5)
town.addEdge('A21', 'A14', 10)

town.addEdge('A22', 'A21', 5)
town.addEdge('A22', 'A23', 5)

town.addEdge('A23', 'A22', 5)
town.addEdge('A23', 'A21', 10)
town.addEdge('A23', 'A24', 12)
town.addEdge('A23', 'A31', 10)

town.addEdge('A24', 'A23', 12)
town.addEdge('A24', 'A31', 22)
town.addEdge('A24', 'A25', 24)
town.addEdge('A24', 'A14', 12)
town.addEdge('A24', 'A15', 24)

town.addEdge('A25', 'A24', 24)
town.addEdge('A25', 'A16', 28)
town.addEdge('A25', 'A26', 20)
town.addEdge('A25', 'A30', 26)

town.addEdge('A26', 'A25', 20)
town.addEdge('A26', 'A27', 12)
town.addEdge('A26', 'A30', 26)
town.addEdge('A26', 'A17', 22)

town.addEdge('A27', 'A26', 12)
town.addEdge('A27', 'A28', 5)
town.addEdge('A27', 'A29', 12)
town.addEdge('A27', 'A20', 14)

town.addEdge('A28', 'A27', 5)
town.addEdge('A28', 'A20', 5)
town.addEdge('A28', 'A29', 5)

town.addEdge('A29', 'A28', 5)
town.addEdge('A29', 'A27', 12)
town.addEdge('A29', 'A30', 10)

town.addEdge('A30', 'A29', 10)
town.addEdge('A30', 'A26', 22)
town.addEdge('A30', 'A25', 26)
town.addEdge('A30', 'A31', 22)
town.addEdge('A30', 'B', 5)

town.addEdge('A31', 'A30', 22)
town.addEdge('A31', 'A24', 22)
town.addEdge('A31', 'A23', 10)

town.addEdge('B', 'A30', 5)'''

# Adding edges (distance data)
'''town.addEdge('A', 'A1', 5)
town.addEdge('A1', 'A', 5)
town.addEdge('A1', 'A2', 17)
town.addEdge('A1', 'A10', 4)
town.addEdge('A1', 'A4', 19)
town.addEdge('A1', 'A9', 3)
town.addEdge('A1', 'A8', 5)

town.addEdge('A2', 'A1', 17)
town.addEdge('A2', 'A3', 4)
town.addEdge('A2', 'A11', 4)

town.addEdge('A3', 'A2', 4)
town.addEdge('A3', 'A12', 3)

town.addEdge('A4', 'A1', 19)
town.addEdge('A4', 'A5', 3)
town.addEdge('A4', 'A7', 5)

town.addEdge('A5', 'A4', 3)
town.addEdge('A5', 'A6', 3)
town.addEdge('A6', 'A5', 3)
town.addEdge('A6', 'A7', 8)
town.addEdge('A6', 'A13', 3)

town.addEdge('A7', 'A6', 8)
town.addEdge('A7', 'A4', 5)
town.addEdge('A7', 'A8', 7)
town.addEdge('A7', 'A14', 3)

town.addEdge('A8', 'A7', 7)
town.addEdge('A8', 'A1', 5)
town.addEdge('A8', 'A9', 3)
town.addEdge('A8', 'A15', 3)

town.addEdge('A9', 'A8', 3)
town.addEdge('A9', 'A16', 3)
town.addEdge('A9', 'A10', 3)
town.addEdge('A9', 'A1', 3)

town.addEdge('A10', 'A9', 4)
town.addEdge('A10', 'A11', 9)
town.addEdge('A10', 'A1', 4)
town.addEdge('A10', 'A17', 4)

town.addEdge('A11', 'A10', 9)
town.addEdge('A11', 'A18', 5)
town.addEdge('A11', 'A2', 4)
town.addEdge('A11', 'A12', 6)
town.addEdge('A11', 'A17', 5)

town.addEdge('A12', 'A11', 6)
town.addEdge('A12', 'A3', 3)
town.addEdge('A12', 'A19', 3)

town.addEdge('A13', 'A6', 3)
town.addEdge('A13', 'A14', 8)
town.addEdge('A13', 'A21', 5)

town.addEdge('A14', 'A13', 8)
town.addEdge('A14', 'A7', 3)
town.addEdge('A14', 'A15', 4)
town.addEdge('A14', 'A24', 11)
town.addEdge('A14', 'A21', 7)

town.addEdge('A15', 'A14', 4)
town.addEdge('A15', 'A16', 6)
town.addEdge('A15', 'A8', 3)
town.addEdge('A15', 'A24', 11)

town.addEdge('A16', 'A15', 6)
town.addEdge('A16', 'A17', 8)
town.addEdge('A16', 'A9', 3)
town.addEdge('A16', 'A25', 11)

town.addEdge('A17', 'A16', 8)
town.addEdge('A17', 'A10', 4)
town.addEdge('A17', 'A11', 5)
town.addEdge('A17', 'A18', 10)
town.addEdge('A17', 'A26', 11)

town.addEdge('A18', 'A17', 7)
town.addEdge('A18', 'A19', 3)
town.addEdge('A18', 'A20', 2)
town.addEdge('A18', 'A11', 5)

town.addEdge('A19', 'A18', 3)
town.addEdge('A19', 'A12', 3)
town.addEdge('A19', 'A20', 2)

town.addEdge('A20', 'A19', 2)
town.addEdge('A20', 'A18', 2)
town.addEdge('A20', 'A27', 6)
town.addEdge('A20', 'A28', 6)

town.addEdge('A21', 'A22', 3)
town.addEdge('A21', 'A23', 3)
town.addEdge('A21', 'A13', 3)
town.addEdge('A21', 'A14', 7)

town.addEdge('A22', 'A21', 3)
town.addEdge('A22', 'A23', 3)

town.addEdge('A23', 'A22', 3)
town.addEdge('A23', 'A21', 3)
town.addEdge('A23', 'A24', 5)
town.addEdge('A23', 'A31', 10)

town.addEdge('A24', 'A23', 5)
town.addEdge('A24', 'A31', 10)
town.addEdge('A24', 'A25', 9)
town.addEdge('A24', 'A14', 11)
town.addEdge('A24', 'A15', 11)

town.addEdge('A25', 'A24', 9)
town.addEdge('A25', 'A16', 11)
town.addEdge('A25', 'A26', 3)
town.addEdge('A25', 'A30', 9)

town.addEdge('A26', 'A25', 3)
town.addEdge('A26', 'A27', 6)
town.addEdge('A26', 'A30', 10)
town.addEdge('A26', 'A17', 11)

town.addEdge('A27', 'A26', 6)
town.addEdge('A27', 'A28', 7)
town.addEdge('A27', 'A29', 4)
town.addEdge('A27', 'A20', 6)

town.addEdge('A28', 'A27', 7)
town.addEdge('A28', 'A20', 6)
town.addEdge('A28', 'A29', 5)

town.addEdge('A29', 'A28', 15)
town.addEdge('A29', 'A27', 4)
town.addEdge('A29', 'A30', 11)

town.addEdge('A30', 'A29', 11)
town.addEdge('A30', 'A26', 10)
town.addEdge('A30', 'A25', 9)
town.addEdge('A30', 'A31', 13)
town.addEdge('A30', 'B', 5)

town.addEdge('A31', 'A30', 13)
town.addEdge('A31', 'A24', 10)
town.addEdge('A31', 'A23', 10)

town.addEdge('B', 'A30', 5)'''

# Adding edges (average of distance and risk weightings)
edges_data_1 = [
    ('A', 'A1', 5), ('A1', 'A', 5), ('A1', 'A2', 9), ('A1', 'A10', 22),
    ('A1', 'A4', 13), ('A1', 'A9', 24), ('A1', 'A8', 20), ('A2', 'A1', 9),
    ('A2', 'A3', 5), ('A2', 'A11', 9), ('A3', 'A2', 5), ('A3', 'A12', 5),
    ('A4', 'A1', 13), ('A4', 'A5', 5), ('A4', 'A7', 5), ('A5', 'A4', 5),
    ('A5', 'A6', 5), ('A6', 'A5', 5), ('A6', 'A7', 7), ('A6', 'A13', 5),
    ('A7', 'A6', 7), ('A7', 'A4', 5), ('A7', 'A8', 11), ('A7', 'A14', 12),
    ('A8', 'A7', 11), ('A8', 'A1', 20), ('A8', 'A9', 20), ('A8', 'A15', 22),
    ('A9', 'A8', 20), ('A9', 'A16', 28), ('A9', 'A10', 20), ('A9', 'A1', 24),
    ('A10', 'A9', 20), ('A10', 'A11', 7), ('A10', 'A1', 22), ('A10', 'A17', 24),
    ('A11', 'A10', 7), ('A11', 'A18', 10), ('A11', 'A2', 9), ('A11', 'A12', 5),
    ('A11', 'A17', 12), ('A12', 'A11', 5), ('A12', 'A3', 5), ('A12', 'A19', 7),
    ('A13', 'A6', 5), ('A13', 'A14', 7), ('A13', 'A21', 5), ('A14', 'A13', 7),
    ('A14', 'A7', 12), ('A14', 'A15', 14), ('A14', 'A24', 12), ('A14', 'A21', 10),
    ('A15', 'A14', 14), ('A15', 'A16', 20), ('A15', 'A8', 22), ('A15', 'A24', 24),
    ('A16', 'A15', 20), ('A16', 'A17', 20), ('A16', 'A9', 28), ('A16', 'A25', 28),
    ('A17', 'A16', 20), ('A17', 'A10', 24), ('A17', 'A11', 12), ('A17', 'A18', 10),
    ('A17', 'A26', 22), ('A18', 'A17', 10), ('A18', 'A19', 5), ('A18', 'A20', 12),
    ('A18', 'A11', 10), ('A19', 'A18', 5), ('A19', 'A12', 7), ('A19', 'A20', 5),
    ('A20', 'A19', 5), ('A20', 'A18', 12), ('A20', 'A27', 14), ('A20', 'A28', 5),
    ('A21', 'A22', 5), ('A21', 'A23', 10), ('A21', 'A13', 5), ('A21', 'A14', 10),
    ('A22', 'A21', 5), ('A22', 'A23', 5), ('A23', 'A22', 5), ('A23', 'A21', 10),
    ('A23', 'A24', 12), ('A23', 'A31', 10), ('A24', 'A23', 12), ('A24', 'A31', 22),
    ('A24', 'A25', 24), ('A24', 'A14', 12), ('A24', 'A15', 24), ('A25', 'A24', 24),
    ('A25', 'A16', 28), ('A25', 'A26', 20), ('A25', 'A30', 26), ('A26', 'A25', 20),
    ('A26', 'A27', 12), ('A26', 'A30', 26), ('A26', 'A17', 22), ('A27', 'A26', 12),
    ('A27', 'A28', 5), ('A27', 'A29', 12), ('A27', 'A20', 14), ('A28', 'A27', 5),
    ('A28', 'A20', 5), ('A28', 'A29', 5), ('A29', 'A28', 5), ('A29', 'A27', 12),
    ('A29', 'A30', 10), ('A30', 'A29', 10), ('A30', 'A26', 22), ('A30', 'A25', 26),
    ('A30', 'A31', 22), ('A30', 'B', 5), ('A31', 'A30', 22), ('A31', 'A24', 22),
    ('A31', 'A23', 10), ('B', 'A30', 5)
]

edges_data_2 = [
    ('A', 'A1', 5), ('A1', 'A', 5), ('A1', 'A2', 17), ('A1', 'A10', 4),
    ('A1', 'A4', 19), ('A1', 'A9', 3), ('A1', 'A8', 5), ('A2', 'A1', 17),
    ('A2', 'A3', 4), ('A2', 'A11', 4), ('A3', 'A2', 4), ('A3', 'A12', 3),
    ('A4', 'A1', 19), ('A4', 'A5', 3), ('A4', 'A7', 5), ('A5', 'A4', 3),
    ('A5', 'A6', 3), ('A6', 'A5', 3), ('A6', 'A7', 8), ('A6', 'A13', 3),
    ('A7', 'A6', 8), ('A7', 'A4', 5), ('A7', 'A8', 7), ('A7', 'A14', 3),
    ('A8', 'A7', 7), ('A8', 'A1', 5), ('A8', 'A9', 3), ('A8', 'A15', 3),
    ('A9', 'A8', 3), ('A9', 'A16', 3), ('A9', 'A10', 3), ('A9', 'A1', 3),
    ('A10', 'A9', 4), ('A10', 'A11', 9), ('A10', 'A1', 4), ('A10', 'A17', 4),
    ('A11', 'A10', 9), ('A11', 'A18', 5), ('A11', 'A2', 4), ('A11', 'A12', 6),
    ('A11', 'A17', 5), ('A12', 'A11', 6), ('A12', 'A3', 3), ('A12', 'A19', 3),
    ('A13', 'A6', 3), ('A13', 'A14', 8), ('A13', 'A21', 5), ('A14', 'A13', 8),
    ('A14', 'A7', 3), ('A14', 'A15', 4), ('A14', 'A24', 11), ('A14', 'A21', 7),
    ('A15', 'A14', 4), ('A15', 'A16', 6), ('A15', 'A8', 3), ('A15', 'A24', 11),
    ('A16', 'A15', 6), ('A16', 'A17', 8), ('A16', 'A9', 3), ('A16', 'A25', 11),
    ('A17', 'A16', 8), ('A17', 'A10', 4), ('A17', 'A11', 5), ('A17', 'A18', 10),
    ('A17', 'A26', 11), ('A18', 'A17', 7), ('A18', 'A19', 3), ('A18', 'A20', 2),
    ('A18', 'A11', 5), ('A19', 'A18', 3), ('A19', 'A12', 3), ('A19', 'A20', 2),
    ('A20', 'A19', 2), ('A20', 'A18', 2), ('A20', 'A27', 6), ('A20', 'A28', 6),
    ('A21', 'A22', 3), ('A21', 'A23', 3), ('A21', 'A13', 3), ('A21', 'A14', 7),
    ('A22', 'A21', 3), ('A22', 'A23', 3), ('A23', 'A22', 3), ('A23', 'A21', 3),
    ('A23', 'A24', 5), ('A23', 'A31', 10), ('A24', 'A23', 5), ('A24', 'A31', 10),
    ('A24', 'A25', 9), ('A24', 'A14', 11), ('A24', 'A15', 11), ('A25', 'A24', 9),
    ('A25', 'A16', 11), ('A25', 'A26', 3), ('A25', 'A30', 9), ('A26', 'A25', 3),
    ('A26', 'A27', 6), ('A26', 'A30', 10), ('A26', 'A17', 11), ('A27', 'A26', 6),
    ('A27', 'A28', 7), ('A27', 'A29', 4), ('A27', 'A20', 6), ('A28', 'A27', 7),
    ('A28', 'A20', 6), ('A28', 'A29', 5), ('A29', 'A28', 10), ('A29', 'A27', 8),
    ('A29', 'A30', 10), ('A30', 'A29', 10), ('A30', 'A26', 16), ('A30', 'A25', 17),
    ('A30', 'A31', 17), ('A30', 'B', 5), ('A31', 'A30', 17), ('A31', 'A24', 16),
    ('A31', 'A23', 10), ('B', 'A30', 5)
]

# Combine edges_data_1 and edges_data_2, and calculate the average for each edge
combined_edges_data = [(edge[0], edge[1], (edge[2] + edges_data_2[idx][2]) // 2) for idx, edge in enumerate(edges_data_1)]

# Adding combined edges to the town
for edge in combined_edges_data:
    town.addEdge(*edge)
print(town.edges)

start_node = "A"
end_node = "B"

shortest_path = town.djikstraAlgorithm(start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")

else:
    print(f"No path from {start_node} to {end_node} found.")

