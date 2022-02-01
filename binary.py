def binary(n,ans):
    if len(ans) == n:
        print(ans)
        return
    if len(ans) == 0 or ans[-1] == '0':
        binary(n,ans+'0')
        binary(n,ans+'1')
    else:
        binary(n,ans+'0')

binary(3,'')