x = "alan_global"
y = "alan_global2"
z = "alan_global3"
def main():
    x = "alan_local"
    print(x)
print(y)
if __name__ == "__main__":
    main()
    print(x)
print(z)