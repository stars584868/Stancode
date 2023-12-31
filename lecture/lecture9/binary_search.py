def main():
	lst = [3, 6, 9, 10, 11, 23, 33, 45, 66, 99]
	print(binary_search(lst, 7))
	print(binary_search(lst, 23))


def binary_search(lst, target):
	"""
	:param lst: list[int], a Python list storing integers.
	:param target: int, the value to be searched.
	:returns : bool, if target is in the lst or not.
	"""
	# Your Code Here
	low = 0
	high = len(lst)-1
	while low <= high:
		mid = (low+high)/2
		if lst[mid] == target:
			return True
		elif lst[mid] > target:
			high = mid - 1
		elif lst[mid] < target:
			low = mid + 1
	return False


if __name__ == '__main__':
	main()
