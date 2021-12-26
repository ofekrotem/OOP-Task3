import random
import sys

from src.GraphInterface import GraphInterface
from src import Node, Edge

""" Nodes: { node_id : Node }
    edgesIn: { node1_id : { node2_id : weight } }
    edgesOut: { node1_id : { node2_id : weight } }
    allEdges: { "node1_id , node2_id": Edge() }  
"""


class DiGraph(GraphInterface):
    def __init__(self, nodes: dict, edgesIn: dict, edgesOut: dict, allEdges: dict):
        self.nodes = nodes
        self.edgesIn = edgesIn
        self.edgesOut = edgesOut
        self.mc = 0
        self.allEdges = allEdges
        self.maxX = sys.float_info.min
        self.maxY = sys.float_info.min
        self.minX = sys.float_info.max
        self.minY = sys.float_info.max
        self.minZ = sys.float_info.max
        self.maxZ = sys.float_info.min
        self.init_min_max()  # Initialize range to random determine x,y,z values for empty Node()

    def set_nodes(self, nodes: dict):
        self.nodes = nodes

    def set_allEdges(self, all: dict):
        self.allEdges = all

    def set_edgesIn(self, i: dict):
        self.edgesIn = i

    def set_edgesOut(self, q: dict):
        self.edgesOut = q

    def init_min_max(self):
        for k, v in self.nodes.items():
            if (v.get_x() > self.maxX): self.maxX = v.get_x()
            if (v.get_x() < self.minX): self.minX = v.get_x()
            if (v.get_y() > self.maxY): self.maxY = v.get_y()
            if (v.get_y() < self.minY): self.minY = v.get_y()
            if (v.get_z() < self.minZ): self.minZ = v.get_z()
            if (v.get_z() > self.maxZ): self.maxZ = v.get_z()

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.allEdges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edgesIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edgesOut.get(id1)

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (not id1 in self.nodes or not id2 in self.nodes): return False
        e = Edge(self.nodes.get(id1), self.nodes.get(id2), weight)
        s = id1 + "," + id2
        if s in self.allEdges:
            if weight == self.allEdges.get(s):
                return False
            else:
                self.allEdges.update({s: weight})
                self.edgesOut.get(id1).update({id2: weight})
                self.edgesIn.get(id2).update({id1: weight})
        else:
            self.allEdges.update({s: weight})
            if id1 in self.edgesOut:
                self.edgesOut.get(id1).update({id2: weight})
            else:
                self.edgesOut.update({id1: {id2: weight}})
            if id2 in self.edgesIn:
                self.edgesIn.get(id2).update({id1: weight})
            else:
                self.edgesIn.update({id2: {id1: weight}})
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if (node_id in self.nodes):
            return False
        else:
            if (not pos):
                x = random.uniform(self.minX, self.maxX)
                y = random.uniform(self.minY, self.maxY)
                z = random.uniform(self.minZ, self.maxZ)
                pos = (x, y, z)

            n1 = Node(node_id, pos[0], pos[1], pos[2])
            self.nodes.update({node_id: n1})
            self.mc += 1
            self.init_min_max()
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        else:
            self.nodes.pop(node_id)
            if node_id in self.edgesOut:
                self.edgesOut.pop(node_id)
            if node_id in self.edgesIn:
                self.edgesIn.pop(node_id)
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        s = node_id1 + "," + node_id2
        if s not in self.allEdges:
            return False
        else:
            self.allEdges.pop(s)
            self.edgesOut.get(node_id1).pop(node_id2)
            self.edgesIn.get(node_id2).pop(node_id1)
            self.mc += 1
