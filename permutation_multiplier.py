class perm:
    def __init__(self, permutation, N):
        self.permutation = permutation
        self.N = N

    def __str__(self):
        return str(self.cycleDecomp())

    def __mul__(multiplicand, multiplier):
        if multiplicand.N > multiplier.N:
            a,b = multiplicand, multiplier
            rev = False
        else:
            a,b = multiplier, multiplicand # a.N >= b.N
            rev = True
        if a.N > b.N: # extend b.permutation to new indices
            def tmpFunction(i):
                if i <= b.N:
                    return b.permutation(i)
                return i
        else:
            tmpFunction = b.permutation
        def composite(i):
            if rev:
                return tmpFunction(a.permutation(i))
            return a.permutation(tmpFunction(i))

        return perm(composite, a.N)

    def cycleDecomp(self):
        cycles, currentCycle, indices = [], [], list(range(1, self.N+1))
        while len(indices) > 0:
            start, tmp = indices[0], self.permutation(indices[0])
            if start == tmp: # fixed point
                cycles.append([start])
                indices.remove(start)
                continue

            currentCycle.append(start)
            indices.remove(start)
            while tmp != start:
                currentCycle.append(tmp)
                indices.remove(tmp)
                tmp = self.permutation(tmp)
            cycles.append(currentCycle)
            currentCycle = []
        return cycles

def listToPerm(myList): # image range(1, N+1) above your list. That is table notation for permutations
    return (lambda x: myList[x-1])

cyclicShift = perm(lambda x: x%5+1, 5)
threeTwo = perm(listToPerm([1,3,2,5,4]), 5)
