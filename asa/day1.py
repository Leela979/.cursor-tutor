def get_even_numbers(limit):
    even_numbers = [num for num in range(limit + 1) if num % 2 == 0]
    return even_numbers