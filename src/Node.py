class Node:
    def __init__(self, id: int, x: float, y: float, z: float):
        self.id = id;
        self.x = x;
        self.y = y;
        self.z = z;
        self.tag = 0

    def get_id(self) -> int:
        return self.id

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def get_z(self) -> float:
        return self.z

    def get_tag(self) -> int:
        return self.tag

    def set_tag(self, ntag: int):
        self.tag = ntag
