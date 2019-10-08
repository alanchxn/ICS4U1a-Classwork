import evaluation
import count  
def test_average():
    assert(10, 5, 0) == 5
    assert(2, 4, 6) == 4
    assert(5, 9, 4) == 6

def test_counter():
    print("what do you want to display? type print wins for wins, print losses for losses, and print ties for ties")
    wlt_list = list('WWWWWLLLLLTT')
    if action = "print wins":
        print("the amount of wins is " + (wlt_list.count('W')))
        assert wlt_list.count('W') == 5
    if action = "print losses" 
        print("the amount of losses is " + (wlt_list.count('L')))
        assert wlt_list.count('L') == 5
    if action = "print ties"
        print("the amount of ties is " + (wlt_list.count('T')))
        assert wlt_list.count('T') == 2
test_counter()

def test_sort_dict():
    test_list = ["W","L","W","T","T"]
    expected = {
        "W": 2,
        "L": 1,
        "T": 2
    }
    result_list = sort_dict(test_list)
    assert expected == result_list  
test_sort_dict()

def test_sort_dict_question4():
    
    test_data = {
        "W": 2,
        "L": 1,
        "T": 2
    }
    result = sort_dict_question4(test_data, "W")
    print("" + str(result))
    assert result == 2            

sort_dict_question4()