# Application of Fibonacci
def count(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    return count(n-2) + count(n-1)

print(count(4))