numbers = [int(n) for n in input()]
total = 0

def sumx(x):
    global total
    total += x
    return total

new_list = [sumx(int(x)) for x in numbers]
print(new_list)

'''
# Get user input of numbers
user_input = input()
# Transform str numbers to int numbers
nums = [int(x) for x in user_input]

run_total = [sum(nums[:x + 1]) for x in range(len(nums))]

print(run_total)  # print the running total list
'''