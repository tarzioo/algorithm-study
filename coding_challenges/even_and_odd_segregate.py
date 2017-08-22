def even_and_odd(lst):
    """move all even to the left and all odd to the right.  return the amount of swaps"""


    left = 0
    right = len(lst) -1
    count = 0

    while left < right:
        while(lst[left] %2 == 0 and left < right):
            left += 1
        while(lst[right] %2 != 0 and left < right):
            right -= 1
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -=1
            count += 1



    return count



