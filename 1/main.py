ARGS = {
    "top_n": 3,
    "file_name": "input.txt"
}

# -----------------------------------------------------------------------------
# reads the file @file_name and adds each line to the previous one. If
# \n is read, the counter starts at 0 again and the previous counter is
# pushed into an array, which is then returned.
def readFile(file_name: str):
    elfs = list()
    f = open(file_name, 'r')
    curr_calories = 0

    for line in f:
        if line == '\n':
            elfs.append(curr_calories)
            curr_calories = 0
            continue
        curr_calories += int(line)
            
    f.close()
    return elfs


# -----------------------------------------------------------------------------
# Places a number @value at index @index of array @top_n. The numbers 
# after @index are pushed back
def fitNumberBetween(top_n: list, value: int, index: int):
    for i in range(len(top_n)-1, index, -1):
        top_n[i] = top_n[i-1]       
    top_n[index] = value 
    return top_n


# -----------------------------------------------------------------------------
# Gets the top @n max values of @all_elfes_calories
def getMaxValuesTopN(n: int, all_elfes_calories: list):
    top_n = [0 for _ in range(n)]
    for curr in all_elfes_calories:
        if top_n[n-1] < curr:
            for i, top_g in enumerate(top_n):
                if top_g < curr:
                    fitNumberBetween(top_n, curr, i)  
                    break
    return top_n    


# -----------------------------------------------------------------------------
# prints the max values computed by getMaxValuesTopN()
def printTopGs(top_gs: list):
    print(f"The {len(top_gs)} Top-Gs are: ")
    for place, top_g in enumerate(top_gs):
        print(f"  [{place}] -> ELF index nr.: {top_gs.index(top_g) + 1} with calories: {top_g}")
    print(f"\nWith a total amount of calories: {sum(top_gs)}")


# -----------------------------------------------------------------------------
# main function
def main():
    elf_summed_calories = readFile(ARGS["file_name"])
    top_n = getMaxValuesTopN(ARGS["top_n"], elf_summed_calories)
    printTopGs(top_n)
    
   
if __name__ == "__main__":
    main()