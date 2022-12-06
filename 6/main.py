ARGS = {
    "file_name": "inputs/input.txt"
}



# -----------------------------------------------------------------------------
# checks if a list of chars has all unique characters
def checkIfxCharsAreNotEqual(chars: list):    
    if (len(chars) == len(list(set(chars)))):
        return True
    return False
        


# -----------------------------------------------------------------------------
# Returns the index, where previously x characters where different
def checkWherePackageStarts(line: str, x: int):
    line = line.replace('\n', '')
    for i in range(len(line)):
        all_unique = checkIfxCharsAreNotEqual(line[i:i+x])
        if all_unique: 
            return {"index": i+x, "string": line[i:i+x]}
                

# -----------------------------------------------------------------------------
# reads the file @file_name line by line and checks where 4 and 14 consecutive characters
# are not repeated
def readFile(file_name: str):
    start_of_packages_4 = list()
    start_of_packages_14 = list()
    f = open(file_name, 'r')
    for line in f:
        start_of_packages_4.append(checkWherePackageStarts(line, 4))   
        start_of_packages_14.append(checkWherePackageStarts(line, 14))   
    f.close()
    return start_of_packages_4, start_of_packages_14




# -----------------------------------------------------------------------------
# main function
def main():
    # PART 1
    start_of_packages_4, start_of_packages_14 = readFile(ARGS["file_name"])    
    print(f"[PART 1] -> ", end="")
    for packet in start_of_packages_4:
        print(f"The start of the package 4 is at {packet['index']} with {packet['string']}")
    # PART 2
    print(f"[PART 2] -> ", end="")
    for packet in start_of_packages_14:
        print(f"The start of the package 14 is at {packet['index']} with {packet['string']}")
    
   
if __name__ == "__main__":
    main()