def twoRobots(m, queries):
    prev_bot = queries[0][0]
    mintotal = 0
    containers = [0]*(m+1) # containers[i] is the min distance to reach containers[i]
    
    print('prev_bot = ', prev_bot)
    print('mintotal = ', mintotal)
    for a,b in queries:
        print('----------------------------')
        print('a b = ', a,b)
        distance = abs(a-b)
        traveled = abs(prev_bot-a)+distance
        print('distance = ', distance)
        print('traveled = ', traveled)

        minimums = min(abs(k-a)+v for k,v in enumerate(containers))
        print('minimums = ', minimums)
        minimums = min(mintotal,minimums)
        print('minimums = ', minimums)
        mintotal += traveled
        print(mintotal)

        print('before containers = ', containers)
        containers[:] = [ v+traveled for v in containers ]
        print('after containers = ', containers)
        containers[prev_bot] = minimums+distance
        print('prev_bot = ', prev_bot)
        print('containers[prev_bot] = ', containers[prev_bot])
        prev_bot = b

    print('final containers = ', containers)
    return min(containers)

print(twoRobots(5, ((1, 5), (3, 2), (4, 1), (2, 4))))