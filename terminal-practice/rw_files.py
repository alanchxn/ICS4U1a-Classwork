with open("some_file2.txt", "w") as f:
    for number in range(1, 51):
        f.write(str(number) + "\n")


with open("some_file2.txt", 'r') as ff:
    contents = ff.read()

print(contents)        