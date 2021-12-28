import heapq
import json
import math
import os.path
import random
from typing import List

import matplotlib.pyplot as plt

from src.DiGraph import Node, Edge, DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src import Window


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: GraphInterface = None):
        self.graph = graph;

    def get_graph(self) -> GraphInterface:
        return self.graph;

    def load_from_json(self, file_name: str) -> bool:
        print(file_name)
        file_path = os.path.join(file_name)
        print(file_path)
        """
        Convert json file to python list
        :param file: file name
        :return: dict contains json data
        """
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        Nodes = {}
        a = []
        for n in data.get("Nodes"):
            if "pos" in n:
                pos = str(n.pop("pos"))
                p = pos.split(",")
                x = float(p[0])
                y = float(p[1])
                z = float(p[2])
            else:
                x = random.uniform(self.graph.minX, self.graph.maxX)
                y = random.uniform(self.graph.minY, self.graph.maxY)
                z = random.uniform(self.graph.minZ, self.graph.maxZ)
            Nid = int(n.pop("id"))
            nodee = Node(Nid, x, y, z)
            Nodes.update({Nid: nodee})
            self.graph.set_nodes(Nodes)
        allEdges = {}
        edgesIn = {}
        edgesOut = {}

        for e in data.get("Edges"):
            src = int(e.pop("src"))
            dest = int(e.pop("dest"))
            w = float(e.pop("w"))
            ed = Edge(Nodes.get(src), Nodes.get(dest), w)
            s = str(src) + "," + str(dest)
            allEdges.update({s: ed})
            if src in edgesOut:
                edgesOut.get(src).update({dest: w})
            else:
                edgesOut.update({src: {dest: w}})
            if dest in edgesIn:
                edgesIn.get(dest).update({src: w})
            else:
                edgesIn.update({dest: {src: w}})
        self.graph.set_nodes(Nodes)
        self.graph.set_allEdges(allEdges)
        self.graph.set_edgesIn(edgesIn)
        self.graph.set_edgesOut(edgesOut)

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        for k, n in self.graph.get_all_v().items():
            pos = str(n.get_x()) + "," + str(n.get_y()) + "," + str(n.get_z())
            Nid = n.get_id()
            nodes.append({"pos": pos, "id": Nid})
        edges = []
        for k, e in self.graph.get_allEdges().items():
            src = e.get_src().get_id()
            dst = e.get_dest().get_id()
            w = e.get_weight()
            edges.append({"src": src, "w": w, "dest": dst})

        data = {"Edges": edges, "Nodes": nodes}
        with open(file_name, "w") as outfile:
            json.dump(data, outfile)

    def Dijkstra(self, startID: int, allNodes: dict):
        start = self.graph.get_all_v().get(startID)
        tor = [start]
        daddymap = {startID: start}
        for k, n in self.graph.get_all_v().items():
            if n.get_id() != startID:
                daddymap[k] = n
        while len(tor) > 0:
            curr = tor[0]
            if self.graph.all_out_edges_of_node(curr.get_id()) is not None:
                for k, v in self.graph.all_out_edges_of_node(curr.get_id()).items():
                    if daddymap[k].get_tag() == 0:
                        total_length = curr.get_w() + v
                        curr_w = daddymap[k].get_w()
                        if curr_w > total_length:
                            daddymap[k].set_w(total_length)
                            daddymap[k].set_my_daddy(allNodes.get(curr.get_id()))
                            heapq.heappush(tor, daddymap[k])
            curr.set_tag(1)
            heapq.heappop(tor)
        return daddymap

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph is None:
            return math.inf, []
        allNodes = self.graph.get_all_v()
        if allNodes.get(id1) is None or allNodes.get(id2) is None:
            return math.inf, []
        if id1 == id2:
            return 0, [id2]
        self.graph.makeTagsZero()
        self.graph.DijkstraPrep(id1)
        check = self.Dijkstra(id1, allNodes)
        if check[id2].get_tag() == 0:
            return math.inf, []
        temp = []
        curr = check[id2]
        while curr.get_id() != id1:
            temp.append(allNodes.get(curr.get_id()))
            curr = check[curr.whos_my_daddy().get_id()]
        ans = []
        ans.append(id1)
        while len(temp) > 0:
            ans.append(temp.pop().get_id())

        return check[id2].get_w(), ans

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if len(node_lst) == 0:
            return None
        if len(node_lst) == 1:
            return node_lst
        full_path = []
        curr = []
        sum = 0
        curr_ind = node_lst.pop(0)
        flag = False
        last = node_lst[len(node_lst) - 1]
        while len(node_lst) > 0:
            next_ind = 0
            remove_ind = 0
            min_w = math.inf
            for i in range(len(node_lst)):
                (s_p_l, p_s_i) = self.shortest_path(curr_ind, node_lst[i])
                if min_w > s_p_l:
                    min_w = s_p_l
                    next_ind = i
                    remove_ind = i
                    flag = True
                    curr = p_s_i
                    if node_lst[i] == last:
                        sum = min_w
            if not flag:
                return None
            flag = False
            curr_ind = next_ind
            node_lst.pop(remove_ind)
            full_path = curr.copy()

        full_path = list(dict.fromkeys(full_path))
        return full_path, sum

    def centerPoint(self) -> (int, float):
        totalmaxDist = {}
        for src in self.graph.get_all_v().values():
            tempdist = -1
            for dest in self.graph.get_all_v().values():
                sp = self.shortest_path(src.get_id(), dest.get_id())[0]
                if sp > tempdist:
                    tempdist = sp
            totalmaxDist.update({src.get_id(): tempdist})
        maxdist = math.inf
        index = -1
        for k, v in totalmaxDist.items():
            if v < maxdist:
                maxdist = v
                index = k
        return index, maxdist

    def plot_graph(self) -> None:
        """ plots the graph.
            if the nodes have a position, the nodes will be placed there.
            Otherwise, they will be placed in a random but elegant manner.
            @return: None """
        """
        nodes = self.graph.get_all_v()
        for i, n in nodes.items():
            node_x = nodes.get(i).get_x()
            node_y = nodes.get(i).get_y()
            text_x = node_x * 1.000007
            text_y = node_y * 1.000007
            plt.plot(node_x, node_y, ".", markersize=15, color="blue")
            plt.text(text_x, text_y, str(n.get_id()), color="red", fontsize=12)

        for src in nodes.keys():
            if self.graph.all_out_edges_of_node(src) is not None:
                for dest in self.graph.all_out_edges_of_node(src).keys():
                    node_x = nodes.get(src).get_x()
                    node_y = nodes[src].get_y()
                    plt.annotate("", xy=(node_x, node_y), xytext=(nodes[dest].get_x(), nodes[dest].get_y()),
                                 arrowprops=dict(arrowstyle="<-"))
        plt.show()
        """
        Window.game(self)


if __name__ == '__main__':
    graph = DiGraph()
    algo = GraphAlgo(graph)
    algo.load_from_json(r"../data/A3.json")
    algo.save_to_json("test.json")
    ls = [0, 2]
    ans = algo.shortest_path(0, 2)
    print(ans)
    ans = algo.TSP(ls)
    print(ans)
    print(algo.centerPoint())
    algo.plot_graph()
