def shortPalindrome(s):
    s = list(s)
    
    single = [0] * 26
    double = [[0]*26 for _ in range(26)] # original string = ab --> reversed, double[a][b]+=1
    triple = [0] * 26
    res = 0
    while s:
        idx = ord(s.pop())-97
        
        res+=triple[idx]
        
        for i in range(26):
            triple[i] += double[idx][i] #  (j)   (idex)(idex)(j)
            double[idx][i] += single[i]  
            
        '''
        single[a] = 1
        single[b]=2
        double[b][a] = 2
        double[b][b] =1
        triple[a] = 1
        at fourth pop, a
        s=abba --> res+=triple[a] 

        '''
            
        single[idx]+=1


    
    return res%1000000007

print(shortPalindrome('ghhggh'))

'''
reverse = hgghhg

h
single_char_counts[h] = 1

hg
single_char_counts[h] = 1
single_char_counts[g] = 1
pair_counts[h][g] = 1

hgg
single_char_counts[h] = 1
single_char_counts[g] = 2
pair_counts[h][g] = 2
pair_counts[g][g] = 1
potential_triplet_counts['h'] = 1

hggh
single_char_counts[h] = 2
single_char_counts[g] = 2
pair_counts[h][g] = 2
pair_counts[g][g] = 1
pair_counts[h][h] = 1
pair_counts[g][h] = 2
potential_triplet_counts['h'] = 1
total_palindromes = 1

hgghh
single_char_counts[h] = 3
single_char_counts[g] = 2
pair_counts[h][g] = 2
pair_counts[g][g] = 1
pair_counts[h][h] = 3
pair_counts[g][h] = 4
potential_triplet_counts['h'] = 1
potential_triplet_counts['g'] = 1
total_palindromes = 2

'''