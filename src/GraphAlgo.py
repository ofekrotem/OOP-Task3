import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from src import Node
from src import Edge


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface):
        self.graph = graph;

    def get_graph(self) -> GraphInterface:
        return self.graph;

    def load_from_json(self, file_name: str) -> bool:
        """
        Convert json file to python list
        :param file: file name
        :return: dict contains json data
        """
        with open(file_name) as json_file:
            data = json.load(json_file)
        Nodes = {}
        a = []
        for n in data.get("Nodes"):
            pos = str(n.pop("pos"))
            p = pos.split(",")
            x = float(p.pop(0))
            y = float(p.pop(1))
            z = float(p.pop(2))
            nodee = Node(x, y, z)
            id = int(n.pop("id"))
            Nodes.update({id: nodee})
        allEdges = {}
        edgesIn = {}
        edgesOut = {}

        for e in data.get("Edges"):
            src = int(e.pop("src"))
            dest = int(e.pop("dest"))
            w = float(e.pop("w"))
            ed = Edge(Nodes.get(src), Nodes.get(dest), w)
            s = src + "," + dest
            allEdges.update({s: ed})
            if src in edgesOut:
                edgesOut.get(src).update({dest: ed})
            else:
                edgesOut.update({src: {dest: ed}})
            if dest in edgesIn:
                edgesIn.get(dest).update({src: ed})
            else:
                edgesIn.update({dest: {src: ed}})
        self.graph.set_nodes(Nodes)
        self.graph.set_allEdges(allEdges)
        self.graph.set_edgesIn(edgesIn)
        self.graph.set_edgesOut(edgesOut)

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass
