from list_functions import insert_at

def test_insert_at():
    original = [1, 2, 3, 4]
    expected = [1,2,5,3,4]
    result = insert_at(original, 5, 2)
    assert result == expected