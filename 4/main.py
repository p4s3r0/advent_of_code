ARGS = {
    "file_name": "inputs/input.txt"
}

# -----------------------------------------------------------------------------
# reads the file @file_name line by line and splits it in half. A list is returned
# which has the following structure [[LeftSide],[RightSide]]
def readFile(file_name: str):
    all_cleaning_areas = list()
    f = open(file_name, 'r')

    for line in f:
        curr_rooms_left  = line.replace('\n', '').split(',')[0].split('-')
        curr_rooms_right = line.replace('\n', '').split(',')[1].split('-')
        ranged_left  = list(range(int(curr_rooms_left[0]), int(curr_rooms_left[1])+1))
        ranged_right =  list(range(int(curr_rooms_right[0]), int(curr_rooms_right[1])+1))
        all_cleaning_areas.append([ranged_left, ranged_right])
    f.close()
    return all_cleaning_areas


def checkFullIntersactionAwithB(a: list, b: list):
    if a[0] >= b[0] and a[-1] <= b[-1]:
        return True
    if b[0] >= a[0] and b[-1] <= a[-1]:
        return True
    return False

def checkAnyIntersactionAwithB(a: list, b: list):
    return len(list((set(a) & set(b))))

def checkIfIntersection(all_cleaning_areas: list, full_intersaction: bool):
    how_many_intersections = 0
    func_intersaction = checkFullIntersactionAwithB if full_intersaction else checkAnyIntersactionAwithB
    for elf_pair in all_cleaning_areas:
        how_many_intersections += 1 if func_intersaction(elf_pair[0], elf_pair[1]) else 0
    
    return how_many_intersections

            
# -----------------------------------------------------------------------------
# main function
def main():
    all_cleaning_areas = readFile(ARGS["file_name"])
    intersections = checkIfIntersection(all_cleaning_areas, False)
    print(f"[PART 1] -> There were {intersections} intersections")
    # PART 1
    
    
   
if __name__ == "__main__":
    main()