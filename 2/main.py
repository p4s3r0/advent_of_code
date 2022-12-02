import RPS # Rock Paper Scissors game

ARGS = {
    "file_name": "inputs/input.txt"
}

# -----------------------------------------------------------------------------
# reads the file @file_name line by line and returns a list with the amount of lines
# in the file elements. Each element consists of [<Opponent Move>, <Player Move>]
def readFile(file_name: str):
    all_moves = list()
    f = open(file_name, 'r')

    for line in f:
        all_moves.append([line[0], line[2]])
            
    f.close()
    return all_moves



# -----------------------------------------------------------------------------
# Calculates the total points for every move specified in @all_moves. The @all_moves
# list consists of [<Opponent Move>, <Player Move>]
def calcPoints(all_moves: list):
    total_points = 0
    for move in all_moves:
        total_points += RPS.getPointsForMove(move[0], move[1])
    return total_points


def calcPointsFraud(all_moves: list):
    total_points = 0
    for move in all_moves:
        total_points += RPS.getPointsForFraudMove(move[0], move[1])
    return total_points

# -----------------------------------------------------------------------------
# main function
def main():
    all_moves = readFile(ARGS["file_name"])
    # PART 1
    all_points = calcPoints(all_moves)
    print(f"[PART 1] -> You achieved a total of {all_points} points")
    # PART 2
    all_points = calcPointsFraud(all_moves)
    print(f"[PART 2] -> You achieved a total of {all_points} points")
    
    
    
   
if __name__ == "__main__":
    main()