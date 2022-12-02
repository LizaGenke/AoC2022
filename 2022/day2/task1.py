def ConvertEncryptedToNormalMoveNames(move):
    if (move == "A" or move == "X"):
        return "Rock"
    elif (move == "B" or move == "Y"):
        return "Paper"
    else:
        return "Scissors"

input = "input.txt"
elf_moves = []
suggested_moves = []

#read moves
with open(input) as f:
    while True:
        line = f.readline()
        if not line:
            break   
        moves = line.split()
        elf_moves.append(ConvertEncryptedToNormalMoveNames(moves[0]))
        suggested_moves.append(ConvertEncryptedToNormalMoveNames(moves[1]))

def DecideOutcome(your_move, opponent_move):
    if your_move == opponent_move:
        return 3
    elif ((your_move == "Rock" and opponent_move != "Paper") or
          (your_move == "Paper" and opponent_move != "Scissors") or
          (your_move == "Scissors" and opponent_move != "Rock")):
          return 6
    else:
        return 0

def GetExtraPointsForShape(move):
    if move == "Rock":
        return 1
    elif move == "Paper":
        return 2
    else:
        return 3

final_score = 0

for i in range(len(elf_moves)):
    score = DecideOutcome(suggested_moves[i], elf_moves[i])
    score += GetExtraPointsForShape(suggested_moves[i])
    final_score += score

print(final_score)


