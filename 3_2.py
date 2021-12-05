input = open("3_input.txt", "r").read() # Get input as string
input = input.split('\n') # Split input into separate lines

def count_nums(lst):
    result = [0, 0]
    for i in lst:
        if i == '0':
            result[0] += 1
        else:
            result[1] += 1
    return result

def ox_gen_rate(lst): # returns the oxygen generator rating
    col = 0
    while len(lst) > 1: 
        last_mode_bit = 0
        nums = []

        for row in range(len(lst)):
            nums.append(lst[row][col])

        
        count = count_nums(nums)
        if count[1] >= count[0]: # if '1' is more common or they both have the same frequency
            last_mode_bit = '1'
        else: # if '0' is more common
            last_mode_bit = '0'

        lst = [i for i in lst if i[col] == last_mode_bit] # Remove all numbers which don't match the bit criteria
        col += 1
    return lst[0]

def co2_scrub_rate(lst): # returns the CO2 scrubber rating
    col = 0
    while len(lst) > 1: 
        last_mode_bit = 0
        nums = []

        for row in range(len(lst)):
            nums.append(lst[row][col])

        count = count_nums(nums)
        if count[0] <= count[1]: # if '0' is less common or they both have the same frequency
            last_mode_bit = '0'
        else: # if '1' is less common
            last_mode_bit = '1'

        lst = [i for i in lst if i[col] == last_mode_bit] # Remove all numbers which don't match the bit criteria
        col += 1
    return lst[0]

ox = int(ox_gen_rate(input), 2)
co2 = int(co2_scrub_rate(input), 2)

print(ox, "*", co2, "=", ox * co2, sep=" ")
