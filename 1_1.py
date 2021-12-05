input = open("1_input.txt", "r").read() # Get input as string
input = input.split() # Split input into a list of strings
input = list(map(int, input)) # Convert input into a list of ints

last_num = input[0]
num_increments = 0

for num in input[1:]: # For each number in the input skipping the first
    if num > last_num: # If there was an increment
        num_increments += 1
    last_num = num

print(num_increments)
