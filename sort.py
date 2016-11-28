import heapq

def bubble_sort(a):
	"""Definition of bubble sort"""
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a

def insertion_sort(a):
	"""Definition of insertion sort"""
	for i in range(1, len(a)):
		j = i
		while j > 0 and a[j] < a[j-1]:
			a[j],a[j-1] = a[j-1],a[j]
			j -= 1
	return a

def merge_sort(a):
	"""Implementation of merge sort"""
	if len(a) > 1:
		mid  = int(len(a)/2)
		left = a[:mid]
		right = a[mid:]

		merge_sort(left)
		merge_sort(right)

		l, r = 0, 0

		for i in range(len(a)):

			lval = left[l] if l < len(left) else None
			rval = right[r] if r < len(right) else None

			if (lval and rval and lval < rval) or rval is None:
				a[i] = lval
				l += 1
			elif (lval and rval and lval >= rval) or lval is None:
				a[i] = rval
				r += 1
			else:
				raise Exception('Could not merge, sub arrays sizes do not match')

	return a

def quick_sort(a):
	if len(a) > 1:
		pivot_idx = int(len(a)/2)
		smaller_items = []
		larger_items = []

		for i, val in enumerate(a):
			if i != pivot_idx:
				if val < a[pivot_idx]:
					smaller_items.append(val)
				else:
					larger_items.append(val)

		smaller_items = quick_sort(smaller_items)
		larger_items = quick_sort(larger_items)
		a = list(smaller_items + [a[pivot_idx]] + larger_items)
	return a

def heap_sort(a):
	heapq.heapify(a)
	a = [heapq.heappop(a) for i in range(len(a))]
	return a

size = int(input("Input the size of array: "))
count = 0
l = []
while count < size:
	k = input("Input element "+str(count+1) + ": ")
	l.append(k)
	count = count + 1
a = list(l)
b = bubble_sort(a)
print("After bubble sort: "+str(b))
a = list(l)
b = insertion_sort(a)
print("After insertion sort: "+str(b))
a = list(l)
b = merge_sort(a)
print("After merge sort: "+str(b))
a = list(l)
b = quick_sort(a)
print("After quick sort: "+str(b))
a = list(l)
b = heap_sort(a)
print("After heap sort: "+str(b))