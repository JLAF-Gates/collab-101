import random

# 1

def generate_random_number(min_value=1, max_value=100):
    """
    Generate a random integer within the specified range.

    Args:
        min_value (int): Minimum possible value.
        max_value (int): Maximum possible value.

    Returns:
        int: A randomly generated integer.
    """
    return random.randint(min_value, max_value)


def main():
    random_number = generate_random_number()

    print(f"Random number: {random_number}")


if __name__ == "__main__":
    main()