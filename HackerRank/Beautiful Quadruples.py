def beautifulQuadruples(a, b, c, d):
    a, b, c, d = sorted([a, b, c, d])
    result = 0

    for i in range(1, a + 1):
        for j in range(i, b + 1):
            #xor_pairs = {}
            for k in range(j, c + 1):
                for l in range(k, d + 1):
                    xor_val = i ^ j ^ k ^ l
                    if xor_val != 0:
                        # if (k, l) not in xor_pairs:
                        #     xor_pairs[(k, l)] = True
                        result += 1
    return result