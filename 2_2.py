import re

input = open("2_input.txt", "r").read() # Get input as string
input = input.split('\n') # Split input into separate commands

commands = []
h_pos = 0
depth = 0
aim = 0

for line in input:
    num = re.sub("\D", "", line)
    commands.append((line[0], int(num)))

for cmd in commands:
    match cmd[0]:
        case 'f': # forward command
            h_pos += cmd[1]
            depth += aim * cmd[1]
        case 'd': # down command
            aim += cmd[1]
        case 'u': # up command
            aim -= cmd[1]

print(h_pos, "*", depth, "=", h_pos * depth, sep=" ")
