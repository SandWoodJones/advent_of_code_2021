input = open("3_input.txt", "r").read() # Get input as string
input = input.split('\n') # Split input into separate lines

def most_common(lst):
    val = max(set(lst), key=lst.count) # python magic thanks to https://stackoverflow.com/a/1518632/9353072
    return val

gamma = ''

for col in range(len(input[0])):
    nums = []
    for row in range(len(input)):
        nums.append(input[row][col])
    
    gamma += most_common(nums)

epsilon = ''.join(['1' if i == '0' else '0' for i in gamma]) # invert gamma and save that in epsilon using list comprehension

# convert both to decimal values
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma, "*", epsilon, "=", gamma * epsilon, sep=" ")
