
def add(a: int, b: int)->int: 
    """Calculate the sum of integers a and b

    Args:
        param1: integers a and b
    Returns:
        The sum of integers a and b
    """
    return a+b

def sum_of_list(list1: list[int])->int:
    '''Calculate the sum of a list of integers
    Args:
        param1: list1
    Returns:
        The sum of integers in the list
    '''
    total = 0
    for x in list1:
        total += x
    return total

def wordsCount(words: list[str])->dict:
    '''Calculate the amount of times a key appears in a list
    Args:
        param1: word list
    Returns:
        The key, along with the amount of times it appears in the dictionary
    '''
    result_dict = {}
    for i in words:
        acc = 1
        if i in result_dict.keys():
            acc = acc + 1
        result_dict[i] = acc
    return result_dict



    