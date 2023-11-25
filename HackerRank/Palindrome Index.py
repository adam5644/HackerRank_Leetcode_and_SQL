# def palindromeIndex(s):
#     # A helper function to check if the substring s[l:r] is a palindrome
#     def is_palindrome(l, r):
#         while l < r:
#             if s[l] != s[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True

#     # Main function logic
#     L = 0
#     R = len(s) - 1
#     while L < R: # o(n)
#         if s[L] != s[R]:
#             # If dropping L makes it a palindrome, return L, else return R
#             if is_palindrome(L + 1, R):
#                 return L
#             elif is_palindrome(L, R - 1):
#                 return R
#             else:
#                 # If neither dropping L nor R results in a palindrome,
#                 # it means it's not possible to make it a palindrome by
#                 # removing one character.
#                 return -1
#         L += 1
#         R -= 1
#     # If we exit the loop without returning, the string is already a palindrome or
#     # can become a palindrome by removing a character not checked by the loop (which should not happen in this case).
#     return -1

def palindromeIndex(s):
    def helper(l,r):
        while l<r:
            if s[l] != s[r]: return False
            l+=1
            r-=1
        return True
    
    l=0
    r=len(s)-1
    while l<r:
        if s[l] != s[r]:

            if helper(l+1,r):# drop l
                return l
            if helper(l,r-1):# drop r
                return r
            else: return -1 # dropping either dont create palindrome, return -1
        l+=1
        r-=1
    
    return -1 # s already palindrome
        


# Example usage:
print(palindromeIndex("aaab"))  # Output should be 3
print(palindromeIndex("baa"))   # Output should be 0
print(palindromeIndex("aaa"))   # Output should be -1
