def ConvertEncryptedToNormalMoveNames(move):
    if (move == "A"):
        return "Rock"
    elif (move == "B"):
        return "Paper"
    else:
        return "Scissors"

def ConvertEncryptedOutcome(outcome):
    if (outcome == "X"):
        return "Lose"
    elif (outcome == "Y"):
        return "Draw"
    else:
        return "Win"

input = "input.txt"
elf_moves = []
suggested_outcomes = []

#read moves
with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        encrypted_symbols = line.split()
        elf_moves.append(ConvertEncryptedToNormalMoveNames(encrypted_symbols[0]))
        suggested_outcomes.append(ConvertEncryptedOutcome(encrypted_symbols[1]))

def DecideOutcome(your_move, opponent_move):
    if your_move == opponent_move:
        return 3
    elif ((your_move == "Rock" and opponent_move != "Paper") or
          (your_move == "Paper" and opponent_move != "Scissors") or
          (your_move == "Scissors" and opponent_move != "Rock")):
          return 6
    else:
        return 0

def SuggestMove(opponent_move, desired_outcome):
    if (desired_outcome == "Draw"):
        return opponent_move
    if (opponent_move == "Rock"):
        if (desired_outcome == "Win"):
            return "Paper"
        else:
            return "Scissors"
    if (opponent_move == "Paper"):
        if (desired_outcome == "Win"):
            return "Scissors"
        else:
            return "Rock"
    if (opponent_move == "Scissors"):
        if (desired_outcome == "Win"):
            return "Rock"
        else:
            return "Paper"

def GetExtraPointsForShape(move):
    if move == "Rock":
        return 1
    elif move == "Paper":
        return 2
    else:
        return 3

final_score = 0

for i in range(len(elf_moves)):
    my_move = SuggestMove(elf_moves[i], suggested_outcomes[i])
    score = DecideOutcome(my_move, elf_moves[i])
    score += GetExtraPointsForShape(my_move)
    final_score += score

print(final_score)


