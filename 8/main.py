from outsourced import *

ARGS = {
    "file_name": "inputs/input.txt"
}



# -----------------------------------------------------------------------------
# reads the file @file_name line by line and checks where 4 and 14 consecutive characters
# are not repeated
def readFile(file_name: str):
    forest = list()
    f = open(file_name, 'r')
    for line in f:
        forest.append([char for char in line.replace('\n', '')])
    f.close()
    return forest



# -----------------------------------------------------------------------------
# Checks if one tree is visible from the outer part
def isTreeVisible(forest: list(), x: int, y: int):
    return checkLeftVisible(forest, x, y) or checkRightVisible(forest, x, y) or checkTopVisible(forest, x, y) or checkBotVisible(forest, x, y)

    

# -----------------------------------------------------------------------------
# Checks how many trees are visible from the outer part
def calcAllVisibleTrees(forest: list()):
    amount_visible_trees = len(forest)*2+len(forest[0])*2 - 4
    for y in range(1, len(forest)-1):
        for x in range(1, len(forest[0])-1):
            if isTreeVisible(forest, x, y):
                amount_visible_trees += 1
    return amount_visible_trees



# -----------------------------------------------------------------------------
# Calculates the visible score of one tree
def calcVisibleScore(forest, x, y):
    return getLeftScore(forest, x, y) * getRightScore(forest, x, y) * getTopScore(forest, x, y) * getBotScore(forest, x, y)



# -----------------------------------------------------------------------------
# Calculates the highest possible visible score within the forest
def calcBestVisibleScore(forest: list()):
    curr_best_score = 0
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            curr_score = calcVisibleScore(forest, x, y)
            if curr_score > curr_best_score:
                curr_best_score = curr_score
    return curr_best_score



# -----------------------------------------------------------------------------
# main function
def main():
    # PART 1
    forest = list(zip(*readFile(ARGS["file_name"])))
    visible_trees = calcAllVisibleTrees(forest)
    print(f"[PART 1] -> There are {visible_trees} visible trees")
    # PART 2
    best_visible_score = calcBestVisibleScore(forest)
    print(f"[PART 2] -> The best visible score is {best_visible_score}", end="")
    
   
if __name__ == "__main__":
    main()