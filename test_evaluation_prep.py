import evaluation_prep as fc
def test_add():
    expected1 = 10
    expected2 = 15
    result = fc.add(10,5)
    print("\n the result = add(10+5): " + str(result))
    assert result == expected2
    assert result != expected1
    #or
    # assert evaluation_prep.add(1, 1) == 2


def sum_of_list_test():
    test_list = [5, 7, 9, 14, 2]
    result = fc.sum_of_list(test_list)
    print("\n the result of the sum of the list is " + str(result))
    assert result != 32
    assert result == 37


def test_wordsCount():
    test_words_list = ["alan", "bing", "daniel", "evan", "patty", "evan"]
    expected_dict = {"alan": 1, "bing": 1, "daniel": 1, "evan": 2, "patty": 1}
    result_dict = fc.wordsCount(test_words_list)
    print("\n the amount of times the value appears in the list is " + str(result_dict))
    assert result_dict == expected_dict

def test_all():
    test_add()
    sum_of_list_test()
    test_wordsCount()
    print("Passed all tests.")
test_all()


