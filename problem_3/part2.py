"""
This function checks if a new number makes the largest number larger.
    Args:
        number: The list of digits
        test_digit: The digit to test
        digits: The number of digits to consider
    Returns:
        The difference between the current number and the largest number, and the digit to prune
    
    Notes: Diff is guaranteed to be positive because we only change it if the new number is larger.
"""
def does_new_number_make_larger(number: list[str], test_digit: str, digits: int) -> (int, int):

    diff, digit = 0, 0
    curr_number = int(''.join(number))
    
    for i in range(digits):
        temp = number[:]
        temp.pop(i)
        temp.append(test_digit)
        temp = int(''.join(temp))
        if temp - curr_number > diff:
            digit = i
            diff = temp - curr_number
    
    return diff, digit

"""
This function finds the largest 12 digit number in a string of numbers, in forward facing order.
    Args:
        number: The string of numbers
    Returns:
        The largest 2 digit number
"""
def largest_joltage(number: str, digits: int) -> int:
    largest_number = list(number[0:digits])
    for i in range(digits, len(number)):
        larger, bad_digit = does_new_number_make_larger(largest_number, number[i], digits)
        if larger:
            largest_number.pop(bad_digit)
            largest_number.append(number[i])            
    largest_number = int(''.join(largest_number))
    return largest_number

"""
This function finds the total joltage of a list of battery packs.
    Args:
        numbers: The list of numbers
    Returns:
        The total joltage
"""
def total_joltage(numbers: list[str], digits: int) -> int:
    total_sum = 0
    for number in numbers:
        total_sum += largest_joltage(number, digits)
    return total_sum

input = open('inputs/input.txt', 'r').read()
input = input.split('\n')

print(total_joltage(input, 2))