from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def get_graph(self) -> GraphInterface:
        pass

    def load_from_json(self, file_name: str) -> bool:
        pass

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
