
#test sum(numbers: list[float]) -> float
def test_sum():
        assert sum([]) == 0
        assert sum([1, 1, 1]) == 3
        assert sum([1] * 10000) == 10000
        assert sum(9) == 9
#test math.ceil(float) -> int
#test math.floor(float) -> int
#test f strings
def test_f_string():
    a = 5
    aassert f"hello {a}" == "hello5"
#test .format