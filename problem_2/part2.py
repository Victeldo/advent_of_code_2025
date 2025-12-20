

input = open('inputs/input.txt', 'r').read()

def format_input(input):
    input = input.split(',')
    output = []
    for line in input:
        pair = line.split('-')
        output.append((int(pair[0]), int(pair[1])))
    return output


def find_factors(number):
    factors = []
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append(i)
    factors.append(number)
    return factors

"""
This function checks if a number is invalid by checking if all the substrings of the number are equal.
    Args:
        number: The number to check
        divisor: The divisor to check
    Returns:
        True if the number is invalid, False otherwise
"""
def check_invalid(number, divisor):
    string_number = str(number)
    substrings = []
    substring_length = len(string_number) // divisor
    for i in range(divisor):
        substrings.append(string_number[i*substring_length:(i+1)*substring_length])
    return all(substrings[0] == substring for substring in substrings)


"""
This function counts the number of invalid numbers in a given range.
    Args:
        start: The start of the range
        end: The end of the range
    Returns:
        The number of invalid numbers in the range
"""
def count_invalid(start, end):
    invalid_sum = 0
    for i in range(start, end + 1):
        if len(str(i)) > 1: # only check numbers with more than 1 digit
            factors = find_factors(len(str(i)))
            for factor in factors:
                if check_invalid(i, factor):
                    invalid_sum += i
                    break # break out of for loop to next number
    return invalid_sum

total_sum = 0
pairs = format_input(input)


for pair in pairs:
    total_sum += count_invalid(pair[0], pair[1])

print(total_sum)
