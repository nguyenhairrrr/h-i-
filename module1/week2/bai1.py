a = [1,2,34,5,6,7,8,9]
k = 3
result = []
for i in range(len(a)):
    if len(a)-i >= k:
        result.append(max(a[i:(i+k)]))
print(result)
