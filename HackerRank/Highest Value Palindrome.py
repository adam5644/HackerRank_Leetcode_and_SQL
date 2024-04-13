def highestValuePalindrome(s, n, k):
    s = list(s)
    # Track changes needed to make palindrome
    diff = [0] * (n // 2)
    
    for i in range(n // 2):
        if s[i] != s[-1 - i]:
            diff[i] = 1
    
    # Make palindrome
    for i in range(n // 2):
        if diff[i] == 1:
            if k > 0:
                higher = max(s[i], s[-1 - i])
                s[i], s[-1 - i] = higher, higher
                k -= 1
            else: 
                return '-1'
    
    # Optimize to make the value the highest possible
    for i in range(n // 2):
        if k <= 0:
            break
        if s[i] != '9':
            if diff[i] == 1 and k >= 1:
                s[i] = s[-1 - i] = '9'
                k -= 1
            elif diff[i] == 0 and k >= 2:
                s[i] = s[-1 - i] = '9'
                k -= 2
    
    # Handle odd length case
    if n % 2 == 1 and k >= 1:
        s[n // 2] = '9'
    
    return ''.join(s)