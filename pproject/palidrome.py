
    

def isPalindrome(s):
    return s == s[::-1]
 
 

s = "rotor"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

