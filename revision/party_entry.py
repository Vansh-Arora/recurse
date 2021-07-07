def entry(n):
    # bASE CASE:
    if n <= 1:
        return 1
    return entry(n-1) + (n-1) * entry(n-2) 
print(entry(3))