def subparts(N,k):
	if k == 2:
		result = []
		for i in range(N//2+1):
			result.append([i*2])
		return result
	prev = subparts(N,k-1)
	result = []
	for i in prev:
		currentSum = sum(i)
		for j in range((N-currentSum)//k+1):
			if currentSum + j*k <= 365:
				result.append(i + [j*k])
	return result

def perm(n,k):
	if n <= 1 or k <= 1 or type(n) != int or type(k) != int:
		return False
	prod = 1
	for i in range(n-k+1,n+1):
		prod *= i
	return prod

def comb(n,k):
	if n <= 1 or k <= 1 or type(n) != int or type(k) != int:
		return False
	if k < n-k:
		k = n-k
	prod = 1
	for i in range(k+1,n+1):
		prod *= i
	for i in range(2,n-k+1):
		prod //= i
	return prod

def fact(n):
	prod = 1
	for i in range(2,n+1):
		prod *= i
	return prod

def prob(parts,N,k):
	s = 0 # The number of dates we're choosing
	for i in range(len(parts)):
		s += parts[i]//(i+2)
	answer = comb(365,s)
	for i in range(2,k):
		for j in range(parts[i-2]//i+1):
			answer *= comb(N,i)
			N -= i
	answer *= perm(365-s, N-sum(parts))
	return answer/365**N
