def cubeSum(n, operations):
    results = []
    map = {}
    for operation in operations:
        tokens = operation.split(' ')
        if tokens[0] == 'UPDATE':
            [x, y, z, w] = [int(s) for s in tokens[1:]]
            map[(x, y, z)] = w
        elif tokens[0] == 'QUERY':
            [x1, y1, z1, x2, y2, z2] = [int(s) for s in tokens[1:]]
            result = 0
            for (x, y, z) in map:
                if x >= x1 and x <= x2 and y >= y1 and y <= y2 and z >= z1 and z <= z2:
                    result += map[(x, y, z)]
            results.append(result)
    return results