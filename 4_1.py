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


def find_winner():
    for n in order: # for each drawn number
        for b in boards:
            for l in b:
                if n in l: # if the current board has the drawn number
                    l[n] = 1 # fill it
                    
                if sum(l.values()) == 5: # If a horizontal line has been filled
                    return (b, get_score(b, n))

            # Check vertical lines
            for col in range(5):
                vert_sum = 0 # The sum of all items in a column
                for lne in range(5):
                    idx = list(b[lne].keys())[col]
                    vert_sum += b[lne][idx]
                    
                    if vert_sum == 5: # If a vertical line has been filled
                        return (b, get_score(b, n))

                    
def get_score(board, last_call):
    unmarked_sum = 0
    for i in board:
        for j in i:
            if i[j] == 0:
                unmarked_sum += int(j)

    return unmarked_sum * int(last_call)



print(find_winner()[1])

