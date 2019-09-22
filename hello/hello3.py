def alanchen():
    print("calling multiply with 3 and 7 plus 10 as arguments")
    answer = multiply(3, 7, 9)
    print(answer)
def multiply(x, y, z):
    assert type(z) == int
    assert z < 10
    return (x * y) + z

if __name__ == "__main__":
    alanchen()
