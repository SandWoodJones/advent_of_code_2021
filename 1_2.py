input = open("1_input.txt", "r").read() # Get input as string
input = input.split() # Split input into a list of strings
input = list(map(int, input)) # Convert input into a list of ints

last_window = input[0] + input[1] + input[2]
num_increments = 0

for i in range(len(input) - 3): # for each index of the input save the last 3
    i += 1 # Add offset to skip first window
    window = input[i] + input[i + 1] + input[i + 2] # get the 3 measurement window
    if window > last_window: # if there was an increment
        num_increments += 1
    last_window = window

print(num_increments)
    
        
