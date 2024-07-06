def levenshtein_distance(token1, token2):
    distance = [[None]*(len(token2)+1) for _ in range(len(token1)+1)]
    for t1 in range(len(token1)+1):
        distance[t1][0] = t1
    for t2 in range(len(token2)+1):
        distance[0][t2] = t2
    for t1 in range(1, len(token1)+1):
        for t2 in range(1, len(token2)+1):
            if token1[t1-1] == token2[t2-1]:
                distance[t1][t2] = distance[t1-1][t2-1]
            else:
                a = distance[t1][t2-1]
                b = distance[t1-1][t2]
                c = distance[t1-1][t2-1]
                if (a <= b and a <= c):
                    distance[t1][t2] = a+1
                elif (b<=a and b<=c):     
                    distance[t1][t2] = b+1
                else:
                    distance[t1][t2] = c+1
    return distance[t1][t2]
levenshtein_distance('yu', 'you')
