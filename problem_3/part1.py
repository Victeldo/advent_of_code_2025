## each line of input is a string of numbers, need to do find the largest 2 digit number, in forward facing order.
### 811111111111119 -> 89
### 234234234234278 -> 78

input = open('inputs/input.txt', 'r').read()

input = input.split('\n')

numbers = []

def largest_joltage(number: str) -> int:
    largest_number = 0
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            if int(number[i]) * 10 + int(number[j]) > largest_number:
                largest_number = int(number[i]) * 10 + int(number[j])
    return largest_number

total_sum = 0

for line in input:
    numbers.append(str(line))
    total_sum += largest_joltage(line)

print(total_sum)
