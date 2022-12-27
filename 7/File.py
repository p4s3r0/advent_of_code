import Folder

class File():
    def __init__(self, parent: Folder, name: str, size: int):
        self.name = name
        self.parent_dir = parent
        self.size = int(size)