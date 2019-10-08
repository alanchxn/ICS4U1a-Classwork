def average(a: float, b: float, c: float)->float: 
    """Calculates the average of 3 numbers

    Args:
        a: an float
        b: another float
        c: a final float
    Returns:
        The average of float numbers a, b, c
    """
    average = (a+b+c)/3
    return average

def num_of_wlt(wlt_list: List[str])->int:
    '''Returns an integer of the occurances of a specific result
    
    Args: 
        wlt_list: a list of words as strings
    Returns:
        An integer with the amount of occurences of the result in the list
    '''
    return result_list

def sort_dict(sorter:list) -> dict:
    '''Returns sorted results of W, L, T in a dictionary

    Args: 
        sorter: a list of results that occurred
    Returns:
        A dictionary with sorted results
    '''

    result = {}
    set_list = set(sorter)
    for i in sorted(set_list):
        result[i] = sorter.count(i)
    return result

def sort_dict_question4(game_result:dict, w:str)->int:
    '''Returns the quantity of the specific result in the result list

    Args: 
        game_result: sorted inventory dictionary
    Returns:
        the quantity of the specific result
    '''

    count = 0
    for k,v in game_result.items:
        if k == w:
            count = count + 1
    return count

    