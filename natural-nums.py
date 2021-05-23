def printer(n):
    if n == 0:
        return 
    printer(n-1)
    print(n)


if __name__ == "__main__":
    printer(5)
