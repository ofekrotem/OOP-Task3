from src import Node


class Edge:
    def __init__(self, src: Node, dest: Node, w: float):
        self.src = src
        self.dest = dest
        self.weight = w

    def get_src(self) -> Node:
        return self.src

    def get_dest(self) -> Node:
        return self.dest

    def get_weight(self) -> float:
        return self.weight

    def __eq__(self, other) -> bool:
        return self.src == other.src and self.dest == other.dest and self.weight == other.weight
