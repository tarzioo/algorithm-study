"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    mode_count = {}

    for item in nums:
        mode_count[item] = mode_count.get(item, 0) + 1

    highest_values = max(mode_count.values())

    mode = set()

    for num, count in enumerate(mode_count):
        if count == highest_values:
            mode.add(num)

    print "mode is", mode

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
