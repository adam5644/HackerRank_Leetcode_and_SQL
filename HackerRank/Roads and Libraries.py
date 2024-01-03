def roadsAndLibraries(n, c_lib, c_road, cities):
    # print(n)
    # print(c_lib)
    # print(c_road)
    # print(cities)
    
    if c_lib<c_road:
        return c_lib*n
    city=[{i} for i in range(n+1)]
    for [x,y] in cities:
        if city[x]is not city[y]:
            for k in city[y]:
                city[x].add(k)
                city[k]=city[x]
                
        print('x,y=',x,y)
        print('city = ', city)
        print()
                
        # if city[x]is not city[y]:
        #     for k in city[y]:
        #         city[x].append(k)
        #         city[k]=city[x]
                
    cityset = set([id(c) for c in city[1:]])
    print('cityset=',cityset)
    print('len = ', len(cityset))
    return len(cityset)*c_lib+(n-len(cityset))*c_road

n = 3
c_lib = 2
c_road = 1
cities = [[1, 2], [3, 1], [2, 3]]
print(roadsAndLibraries(n, c_lib, c_road, cities))