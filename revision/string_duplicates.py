'''def removeDuplicates(str, n, i, ans, prev):
    if i == n:
        return ans
    if prev == str[i]:
        return removeDuplicates(str, n, i+1, ans, prev)
    else:
        return removeDuplicates(str,n,i+1,ans+str[i],str[i])

def remove(str):
    return removeDuplicates(str, len(str), 0, '', '*')

print(remove('abcbbbbcjsjduhsjbjhsbckahydaibcajhvcuyahibvjhuhiugdfbekdjviugioufeqq g7feft7f7tfuge'))'''
#User function Template for python3

class Solution:
    def removeDuplicates(self, str, n, i, ans, prev):
        if i == n:
            return ans
        if prev == str[i]:
            return self.removeDuplicates(str, n, i+1, ans, prev)
        else:
            return self.removeDuplicates(str, n, i+1, ans+str[i], str[i])
        
    def removeConsecutiveCharacter(self, S):
        return self.removeDuplicates(S, len(S), 0, '', '*')

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends