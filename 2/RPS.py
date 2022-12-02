# -----------------------------------------------------------------------------
# A | X -> ROCK
# B | Y -> PAPER
# C | Z -> SCISSOR
MOVES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

OUTCOMES = {
    "WIN": 6,
    "DRAW": 3,
    "LOSS": 0
}

RPS = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSOR": 3
}



# -----------------------------------------------------------------------------
# checks if the player or the opponent won. 
# 0 -> DRAW | 1 -> player WIN | -1 -> opponent WIN 
def winCheck(opponent: chr, player: chr):
    if MOVES[opponent] == MOVES[player]:
        return 0
    if (MOVES[opponent] == RPS["ROCK"] and MOVES[player] == RPS["PAPER"]) or (MOVES[opponent] == RPS["PAPER"] and MOVES[player] == RPS["SCISSOR"]) or (MOVES[opponent] == RPS["SCISSOR"] and MOVES[player] == RPS["ROCK"]):
        return 1
    else:
        return -1
    


# -----------------------------------------------------------------------------
# Calculates the points of the player he got by the last move
# DRAW = player_move_value + 3
# LOSS = player_move_value + 0
# WIN  = player_move_value + 6
def getPointsForMove(opponent: chr, player: chr):
    if winCheck(opponent, player) == 0:
        return MOVES[player] + OUTCOMES["DRAW"]
    if winCheck(opponent, player) == -1:
        return MOVES[player] + OUTCOMES["LOSS"]
    if winCheck(opponent, player) == 1:
        return MOVES[player] + OUTCOMES["WIN"]
    
    
    
# -----------------------------------------------------------------------------    
# returns the move for the player, such that a WIN occurs
def win(opponent: chr):
    if MOVES[opponent] == RPS["ROCK"]:
        return "Y"
    if MOVES[opponent] == RPS["PAPER"]:
        return "Z"
    if MOVES[opponent] == RPS["SCISSOR"]:
        return "X"



# -----------------------------------------------------------------------------
# returns the move for the player, such that a DRAW occurs
def draw(opponent: chr):
    return opponent


# -----------------------------------------------------------------------------
# returns the move for the player, such that a LOSS occurs
def lose(opponent: chr):
    if MOVES[opponent] == RPS["ROCK"]:
        return "Z"
    if MOVES[opponent] == RPS["PAPER"]:
        return "X"
    if MOVES[opponent] == RPS["SCISSOR"]:
        return "Y"
    
        
    
# -----------------------------------------------------------------------------   
# manages the fraud game and returns the collected points 
def getPointsForFraudMove(opponent: chr, outcome: chr):
    if MOVES[outcome] == MOVES["X"]:
        player_move = lose(opponent) 
    if MOVES[outcome] == MOVES["Y"]:
        player_move = draw(opponent) 
    if MOVES[outcome] == MOVES["Z"]:
        player_move = win(opponent) 
    return getPointsForMove(opponent, player_move)
    
        

    