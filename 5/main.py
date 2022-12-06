import copy

ARGS = {
    "file_name": "inputs/input.txt"
}



# -----------------------------------------------------------------------------
# This function makes a simple translation of a list.   
def translateList(prev_list: list):
    trans_list = list()
    for x in range(len(prev_list[0])):
        one_pile = list()
        for y in range(len(prev_list)-1, -1, -1):
            if prev_list[y][x] != " ":
                one_pile.append(prev_list[y][x])
        trans_list.append(one_pile)
    return trans_list    
    
    

# -----------------------------------------------------------------------------
# reads the file @file_name line by line and creates two lists, "all_piles" which
# has the piles with the crates defined and "all_moves", where all the moves are
# stored in a dictionary with 
# "amount" -> how many crates should be transportet
# "from"   -> from which pile
# "to"     -> to which pile
def readFile(file_name: str):
    f = open(file_name, 'r')
    all_piles = list()
    all_moves = list()
    moves_input = False
    
    for line in f:
        if not moves_input: 
            # get piles
            if line[0:2] == ' 1':
                moves_input = True
            else:
                curr_stack = list()
                for i in range(len(line)//4):
                    curr_stack.append(line[i*4+1:i*4+2])
                all_piles.append(curr_stack)
        else:
            if line == '\n':
                continue
            curr = line.replace('\n', '').split(' ')
            all_moves.append({
                "amount": int(curr[1]),
                "from": int(curr[3])-1,
                "to": int(curr[5])-1
            })
            
    trans_list = translateList(all_piles)
    f.close()
    return trans_list, all_moves



# -----------------------------------------------------------------------------
# Returns a string of the concatinated crate chars
def get_highest_crates(replaced_piles: list):
    highest_cret_string = ""
    for crate in replaced_piles:
        highest_cret_string += crate[-1] 
    return highest_cret_string
                
            
    
# -----------------------------------------------------------------------------
def craneMakeMoves(all_piles_prev: list, all_moves: list):
    all_piles = copy.deepcopy(all_piles_prev)
    for curr_move in all_moves:
        for i in range(curr_move["amount"]):
            all_piles[curr_move["to"]].append(all_piles[curr_move["from"]][-1])
            del all_piles[curr_move["from"]][-1]
    return all_piles    

# -----------------------------------------------------------------------------
# Makes all the moves the crane is supposed to. This variant works with a whole 
# range of piles, since the crane can lift more then 1 crate
def craneMakeMoves9001(all_piles_prev: list, all_moves: list):
    all_piles = copy.deepcopy(all_piles_prev)
    for curr_move in all_moves:
        curr_pile = list()
        for i in range(curr_move["amount"]):
            curr_pile.append(all_piles[curr_move["from"]][-1])
            del all_piles[curr_move["from"]][-1]
        curr_pile.reverse()
        for curr_crate in curr_pile:
            all_piles[curr_move["to"]].append(curr_crate)
    return all_piles    
    


# -----------------------------------------------------------------------------
# main function
def main():
    # PART 1
    all_piles, all_moves = readFile(ARGS["file_name"])    
    replaced_piles = craneMakeMoves(all_piles, all_moves)
    highest_crates = get_highest_crates(replaced_piles)
    print(f"[PART 1] -> The highest crates are {highest_crates}")
    # PART 2
    replaced_piles = craneMakeMoves9001(all_piles, all_moves)
    highest_crates = get_highest_crates(replaced_piles)
    print(f"[PART 2] -> The highest crates are {highest_crates}")
    
    
   
if __name__ == "__main__":
    main()