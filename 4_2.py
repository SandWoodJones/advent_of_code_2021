input = open("4_input.txt", "r").read() # Get input as string
input = input.split('\n') # Split input into a list of strings

input = list(filter(None, input)) # Remove all empty lines

order = input.pop(0).split(',') # Remove the first line, split it, and store it as a list
boards = []

# Separate the boards
for i in range(0, len(input), 5):
    board = []
    for j in range(5):
        line = input[i + j].split(' ') # Split the string of numbers into individual numbers
        line = list(filter(None, line)) # Remove empty entries
        board.append(dict.fromkeys(line, 0)) # turn it into a dictionary and add it to b
    
    boards.append(board)  # Add the new board to the list of boards

           
def get_score(board, last_call):
    unmarked_sum = 0
    for i in board:
        for j in i:
            if i[j] == 0:
                unmarked_sum += int(j)

    return unmarked_sum * int(last_call)


def find_loser():
    winners = []
    for n in order: # for each drawn number
        for b in boards: # Mark called numbers
            for l in b:
                if n in l: # if the current board has the drawn number
                    l[n] = 1 # fill it
            if check_horizontal(b) or check_vertical(b):
                winners.append((b, n))

        boards[:] = [x for x in boards if not (check_horizontal(x) or check_vertical(x))] # Remove boards that have already won 
            
                        
    loser = winners[-1]
    return loser

def check_horizontal(b): # Checks if a board won by filling a horizontal line
    for l in b:
        if sum(l.values()) == 5: # If a horizontal line has been filled
            return True
    return False

def check_vertical(b): # Checks if a board won by filling a vertical line
    for col in range(5):
        vert_sum = 0 # The sum of all items in a column
        for line in range(5):
            idx = list(b[line].keys())[col]
            vert_sum += b[line][idx]
                    
            if vert_sum == 5: # If a vertical line has been filled
                return True
    return False

result = find_loser()

for i in result[0]:
    print(i)
print(result[1], get_score(result[0], result[1]))
