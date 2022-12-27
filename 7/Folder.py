class Folder():
    def __init__(self, parent, name: str):
        self.name = name
        self.parent = parent
        self.folders = dict()
        self.files = list()
        self.size = 0

    # -----------------------------------------------------------------------------
    # Adds the directory to the current folder
    def addDirectory(self, dir):
        self.folders[dir.name] = dir
    # -----------------------------------------------------------------------------
    # Adds the file to the current folder
    def addFile(self, file):
        self.files.append(file)
