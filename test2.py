def transpose(m):
    return [ [m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


def transpose2(m):
    result=[]
    for j in range(len(m[0])):
        result.append([])
        for i in range(len(m)):
            result[j].append(m[i][j])
    return result