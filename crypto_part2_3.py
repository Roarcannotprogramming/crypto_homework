def jiechengliebiao():
    jiecheng = 1
    jiechenglist = [1]
    for i in range(1, 26):
        jiecheng = jiecheng * i
        jiechenglist.append(jiecheng)
    return jiechenglist


def pailieshu(n):
    jiechenglist = jiechengliebiao()
    for i in range(0, n+1):
        yield jiechenglist[n]/jiechenglist[n-i]


print(jiechengliebiao())

sum = 0
for m in pailieshu(25):
    print(m)
    sum += m    
print('sum = {}'.format(sum))
print(jiechengliebiao()[25]/(2**83))
