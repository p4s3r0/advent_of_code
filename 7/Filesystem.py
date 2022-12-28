import Folder
import File

class Filesystem():
    __X = 0
    def __init__(self):
        self.content = {"/": Folder.Folder(None, "/")}
        self.curr_folder = self.content["/"]
        self.all_folders = dict()

    # -----------------------------------------------------------------------------
    # adds the file size to all parent directories
    def addSizeToParents(self, size: int):
        folder_i = self.curr_folder 
        folder_i.size += size
        while folder_i.parent != None:
            folder_i = folder_i.parent
            folder_i.size += size
    
    # -----------------------------------------------------------------------------
    # gets all folders with size below boundary
    def getFoldersBelowSize(self, boundary: int):
        return [size for size in self.all_folders.values() if size <= boundary]

    # -----------------------------------------------------------------------------
    # get smallest folder to free up enough space
    def getFolderForEnoughSpace(self, total_space: int, space_needed: int):
        free_space = total_space - self.content['/'].size
        sorted_sizes = [size for size in self.all_folders.values()]
        sorted_sizes.sort()
        for size in sorted_sizes:
            if size + free_space >= space_needed:
                return size

    # -----------------------------------------------------------------------------
    # iterates recursivly over the directories and adds each directory to the filesystem
    def iterateOverDirectories(self, curr_folders: dict()):
        for folder in curr_folders.folders:
            if len(curr_folders.folders) == 0:
                return
            self.iterateOverDirectories(curr_folders.folders[folder])

        name = curr_folders.name
        if name in self.all_folders:
            self.__X += 1
            name = f"{curr_folders.name}_X{self.__X}"

        self.all_folders[name] = curr_folders.size
        return