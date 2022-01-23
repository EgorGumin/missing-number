from typing import List


def find_missed_num(numbers: List[int]) -> int:
    """ Searches for the missing number in a shuffled series

    :param numbers: a shuffled series 1..n with one missing number
    :return: int: Missing number
    """
    n = len(numbers) + 1
    progression_sum = int(n * (n + 1) / 2)
    actual_sum = sum(numbers)
    return progression_sum - actual_sum
