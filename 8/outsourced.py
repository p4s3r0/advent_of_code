
# -----------------------------------------------------------------------------
# CHECKS FOR DIRECTIONS VISIBILITY
def checkLeftVisible(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    for i in range(x):
        if forest[i][y] >= tree_heigth:
            return False
    return True


def checkRightVisible(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    for i in range(x+1, len(forest[0])):
        if forest[i][y] >= tree_heigth:
            return False
    return True


def checkTopVisible(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    for i in range(y):
        if forest[x][i] >= tree_heigth:
            return False
    return True
    

def checkBotVisible(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    for i in range(y+1, len(forest)):
        if forest[x][i] >= tree_heigth:
            return False
    return True
# -----------------------------------------------------------------------------






# -----------------------------------------------------------------------------
# CALCULATES HOW MANY TREES ARE SEEN FOR CERTAIN DIRECTION
def getLeftScore(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    curr_score = 0
    if x == 0: return 0
    for i in range(x-1, -1, -1):
        curr_score += 1
        if forest[i][y] >= tree_heigth:
            break
    return curr_score



def getRightScore(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    curr_score = 0
    if x == len(forest[0]): return 0
    for i in range(x+1, len(forest[0])):
        curr_score += 1
        if forest[i][y] >= tree_heigth:
            break
    return curr_score


def getTopScore(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    curr_score = 0
    if y == 0: return 0
    for i in range(y-1, -1, -1):
        curr_score += 1
        if forest[x][i] >= tree_heigth:
            break
    return curr_score

def getBotScore(forest: list(), x: int, y: int):
    tree_heigth = forest[x][y]
    curr_score = 0
    if y == len(forest): return 0
    for i in range(y+1, len(forest)):
        curr_score += 1
        if forest[x][i] >= tree_heigth:
            break
    return curr_score
# -----------------------------------------------------------------------------
