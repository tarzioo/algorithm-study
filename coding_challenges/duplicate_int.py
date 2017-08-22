def duplicate_int(lst):
    """given an array of ints between 1 and 1,000,000, one integer is in the array twice"""


    return [x for x in lst if lst.count(x) == 2]