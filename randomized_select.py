''' Randomized select takes a list of *distinct* numbers, the start
 index p, the end index r, and the number of elements smaller than or
 equal to the selected number.
Can be used for fining the median of an array. 
Expected runing time O(n). '''
import random

def randomized_select(A, p, r, i):
	if p == r:
		return A[p]
	q=randomized_partition(A,p,r)
	k = q-p+1
	if i == k:
		return A[q]
	elif i < k:
		return randomized_select(A, p, q-1, i)
	else:
		return randomized_select(A, q+1, r, i-k)


def randomized_partition (A, p, r):
	i=random.randint(p,r)
	A[i], A[r] = A[r], A[i]
	return partition(A,p,r)

def partition (A, p, r):
	x=A[r]
	i=p-1
	for j in range(p, r):
		if (A[j] <= x):
			i=i+1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	return i+1
