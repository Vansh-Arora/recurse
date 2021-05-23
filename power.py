def power(a,b):
    if b == 1:
        return a
    sub = power(a,b//2)
    if b%2 == 0: return sub*sub
    else: return sub*sub*a

print(power(2,5))