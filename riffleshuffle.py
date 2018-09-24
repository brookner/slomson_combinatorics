def f(i):
    if 1 <= i <= n:
        return 2*i-1
    elif n+1<=i<=2*n:
        return 2*(i-n)

n=26
def cycleThru(start, sigma):
    tmp = sigma(start)
    orbit = [start]
    while tmp != start:
        orbit.append(tmp)
        tmp = sigma(tmp)
    return orbit
print(cycleThru(1, f))
print(cycleThru(2, f))
print(cycleThru(4, f))


def listDifference(list1, list2):
    return [x for x in list1 if x not in list2]

cardList = list(range(1, 53)) # Zero indexing
start = 1
while len(cardList) > 0:
    currentOrbit = cycleThru(start, f)
    print(currentOrbit)
    cardList = listDifference(cardList, currentOrbit)
    if len(cardList) > 0:
        start = cardList[0]
