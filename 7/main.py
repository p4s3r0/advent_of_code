import Folder
import File
import Filesystem

ARGS = {
    "file_name": "inputs/input.txt"
}


# -----------------------------------------------------------------------------
# executes CD command. Adds the folder to the parent directory or goes back
def executeCD(fs: Filesystem, dir: str):
    if dir == '..':
        fs.curr_folder = fs.curr_folder.parent
        return

    fs.curr_folder.addDirectory(Folder.Folder(fs.curr_folder, dir))
    fs.curr_folder = fs.curr_folder.folders[dir]



# -----------------------------------------------------------------------------
# Executes LS command. Reads all listed files and adds it to the folder
def executeLS(fs: Filesystem, commands: list()):
    del commands[0]
    while len(commands) > 0:
        if commands[0][0] == '$':
            break;
        if commands[0][0] == "dir":
            fs.curr_folder.addDirectory(Folder.Folder(fs.curr_folder, commands[0][1]))
        else:
            file = File.File(fs.curr_folder, commands[0][1], commands[0][0])
            fs.curr_folder.addFile(file)
            fs.addSizeToParents(file.size)
        del commands[0]
    


# -----------------------------------------------------------------------------
# Goes through the commands and removes it from the list
def handleCommands(fs: Filesystem, commands: list()):
    del commands[0]
    while len(commands) > 0:
        if commands[0][1] == 'cd':
            executeCD(fs, commands[0][2])
            del commands[0]
        elif commands[0][1] == 'ls':
            executeLS(fs, commands)
        else:
            print("WRONG command", command[1])
            exit()
    fs.iterateOverDirectories(fs.content['/'])
        


# -----------------------------------------------------------------------------
# reads the file @file_name line by line and fills a list commands with the parameter
def readFile(file_name: str):
    commands = list()
    f = open(file_name, 'r')
    for line in f:
        curr_line = line.replace('\n', '').split(' ')
        if curr_line[1] == 'cd':
            commands.append([curr_line[0], curr_line[1], curr_line[2]])
        else:
            commands.append([curr_line[0], curr_line[1]])
    return commands








# -----------------------------------------------------------------------------
# main function
def main():
    # PART 1
    commands = readFile(ARGS["file_name"])
    fs = Filesystem.Filesystem()
    handleCommands(fs, commands)
    summe = sum(fs.getFoldersBelowSize(100000))
    print(f"[PART 1] -> The sum of all directories below {100000} is {summe}")

    size_to_be_deleted = fs.getFolderForEnoughSpace(70000000, 30000000)
    print(f"[PART 2] -> The directory with size {size_to_be_deleted} needs to be deleted")
    
   
if __name__ == "__main__":
    main()