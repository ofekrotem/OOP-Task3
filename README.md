
# Traveling Salesman Problem
OOP Course Ariel University - Task 3.
This project is about implementing algorithms on directed weighted graphs.

## Authors

- Ofek Rotem
- Yonatan Tal


## Graph Plot Screenshots
### Graph A0:
![App Screenshot](Pics for README/A0_Plot.jpeg?text=A0+PLOT)
### Graph A1:
![App Screenshot](Pics for README/A1_Plot.jpeg?text=A1+PLOT)
### Graph A2:
![App Screenshot](Pics for README/A2_Plot.jpeg?text=A2+PLOT)
### Graph A3:
![App Screenshot](Pics for README/A3_Plot.jpeg?text=A3+PLOT)
### Graph A4:
![App Screenshot](Pics for README/A4_Plot.jpeg?text=A4+PLOT)
### Graph A5:
![App Screenshot](Pics for README/A5_Plot.jpeg?text=A5+PLOT)

## Class Explanations
### Node:
This class reperesents a node in the graph and includes a unique ID for each node and its Location (x,y,z).
### Edge:
This class reperesents an edge in the graph and includes its src node, dest node, and its weight.
### DiGraph:
This class implements GraphInterface and reperesents a graph.
It includes these main functions:
- v_size() -> int: Returns the number of vertices (nodes) in this graph.
- e_size() -> int: Returns the number of edges in this graph.
- get_all_v() -> dict: return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data).
- all_in_edges_of_node(id1: int) -> dict: return a dictionary of all the nodes connected to (into) node_id, each node is represented using a pair (other_node_id, weight).
- all_out_edges_of_node(id1: int) -> dict: return a dictionary of all the nodes connected from node_id, each node is represented using a pair (other_node_id, weight).
- get_mc() -> int: Returns the current version of this graph, on every change in the graph state - the MC should be increased.
- add_edge(id1: int, id2: int, weight: float) -> bool: Adds an edge to the graph from Node(id1) to Node(id2) with given weight.
- add_node(node_id: int, pos: tuple = None) -> bool: Adds a node to the graph with node_id as id and pos (x,y,z) as it the nodes location (if pos is not given, one will be assigned to it randomly within the current boundaries of the graph).
- remove_node(node_id: int) -> bool: Removes Node(node_id) from the graph and deletes its edges(if exists).
- remove_edge(node_id1: int, node_id2: int) -> bool: Removes edge (from node_id1 to node_id2) from the graph.
### GraphAlgo:
This class implements GraphAlgoInterface and reperesents the algorithms that can be run on a graph.
It includes these main functions:
- get_graph() -> GraphInterface: Returns the directed graph on which the algorithm works on.
- load_from_json(file_name: str) -> bool: Loads a graph from a json file.
- save_to_json(file_name: str) -> bool: Saves the graph in JSON format to a file.
- shortest_path(id1: int, id2: int) -> (float, list):  Returns the shortest path and the length of the path from node id1 to node id2 using Dijkstra's Algorithm.
- TSP(node_lst: List[int]) -> (List[int], float): Finds the shortest path that visits all the nodes in the list and returns a list of the nodes id's in the path, and the overall distance.
- centerPoint() -> (int, float): Finds the node that has the shortest distance to it's farthest node and returns the nodes id, min-maximum distance.
- plot_graph(self): Plots the graph.

## UML Diagram
![UML](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
