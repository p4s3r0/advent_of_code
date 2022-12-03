ARGS = {
    "file_name": "inputs/input.txt"
}

# -----------------------------------------------------------------------------
# reads the file @file_name line by line and splits it in half. A list is returned
# which has the following structure [[LeftSide],[RightSide]]
def readFile(file_name: str):
    all_backpacks = list()
    f = open(file_name, 'r')

    for line in f:
        all_backpacks.append([ [*line[0:len(line)//2]], [*line[len(line)//2:-1]]])
            
    f.close()
    return all_backpacks



# -----------------------------------------------------------------------------
# translates a char to its given priority: a-z -> 1-26 and A-Z -> 27-52
def translateCharToPriority(char: str):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38



# -----------------------------------------------------------------------------
# iterates over @all_backpacks which has the form [[leftSide],[RightSide]] and
# finds the shared character between leftSide and RightSide. Then the priority
# of the shared character is calculated and put into the return list
def getCommonElements(all_backpacks: list):
    common_elements_priority = list()
    for backpack in all_backpacks:
        common_element = str(list(set(backpack[0]) & set(backpack[1]))[0])[0]
        common_elements_priority.append(translateCharToPriority(common_element))
    return common_elements_priority



# -----------------------------------------------------------------------------
# iterates over @all_backpacks which has the form [[leftSide],[RightSide]] and
# finds the shared character between a 3 pair of backpacks. Then the priority
# of the shared character is calculated and put into the return list
def findCommonElementInNextThreeElf(all_backpacks: list):
    common_elements_priority = list()
    for backpack_index in range(0, len(all_backpacks), 3):
        three_backpacks = [all_backpacks[backpack_index][0] + all_backpacks[backpack_index][1],
                           all_backpacks[backpack_index+1][0] + all_backpacks[backpack_index+1][1],
                           all_backpacks[backpack_index+2][0] + all_backpacks[backpack_index+2][1]]
        common_element = str(list(set(three_backpacks[0]) & set(three_backpacks[1]) & set(three_backpacks[2]))[0])[0]
        common_elements_priority.append(translateCharToPriority(common_element))
    return common_elements_priority



# -----------------------------------------------------------------------------
# main function
def main():
    all_backpacks = readFile(ARGS["file_name"])
    # PART 1
    common_elements = getCommonElements(all_backpacks)
    print(f"[PART 1] -> The sum of the same elements is: {sum(common_elements)}")
    # PART 2
    common_elements = findCommonElementInNextThreeElf(all_backpacks)
    print(f"[PART 2] -> The sum of the same elements of 3 elfes is: {sum(common_elements)}")
    
    
   
if __name__ == "__main__":
    main()