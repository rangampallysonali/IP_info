import random

def generate_random_numbers(count, min_val, max_val):
    """Generates a list of random numbers within a specified range.

    Args:
        count: The number of random numbers to generate.
        min_val: The minimum possible value for the random numbers.
        max_val: The maximum possible value for the random numbers.

    Returns:
        A list of random numbers.
    """
    random_numbers = []
    for _ in range(count):
        random_numbers.append(random.randint(min_val, max_val))
    return random_numbers

if __name__ == "__main__":
    num_count = 10
    min_range = 1
    max_range = 100
    random_list = generate_random_numbers(num_count, min_range, max_range)
    print(f"Generated random numbers: {random_list}")