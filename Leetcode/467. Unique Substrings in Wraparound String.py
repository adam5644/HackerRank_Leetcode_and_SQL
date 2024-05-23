# 467. Unique Substrings in Wraparound String

import collections

dp = collections.Counter({s[0]:1})
print('dp = ', dp)
n = 1
for i in range(1, len(s)):
    if ord(s[i]) - ord(s[i-1]) in [1, -25]:
        n += 1
    else:
        n = 1
    dp[s[i]] = max(dp[s[i]], n)
print(sum(dp.values()))