'''
Please use the code template below to complete your assignment.
Your code must go under pa3 method.
Do not change any other code.
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method
stop working and you will not get credit for your submission.

name: Aaron Garcia
studentID: 030556771

assignment:PA2
'''

import sys

# to allow our sorting function to sort large arrays
sys.setrecursionlimit(2500)

class Solution:

	def part(self, low, high, arr):
        # choose far right element as pivot
		pivot = arr[high]
        # pointer for smaller element
		i = low - 1

		for j in range(low, high):
			if not arr[j] > pivot:  # sort in ascending order...
					# if element larger that pivot is found
					# swap it with the element pointed at by i
					i = i + 1

					# swap values
					temp = arr[i]
					arr[i] = arr[j]
					arr[j] = temp

		# swap pivot element value with lower element specified by i
		temp = arr[i+1]
		arr[i+1] = arr[high]
		arr[high] = temp

		return i + 1

	# this is a quick sort function that has been modified to search for the 
	# kthsmallest element, returning early once it has been found
	def quick_kthSmallest(self, k, low, high, arr):
		if (low == high):
			return arr[low]
		p = self.part(low, high, arr)
		q = p - low + 1
		if(q == k):
			return arr[q]
		if(q > k):
			return self.quick_kthSmallest(k, low, p - 1, arr)
		return self.quick_kthSmallest(k - q, p + 1, high, arr)
		
	# driver function for the assignment
	def pa2 (self, arr: list[int], k: int )	-> int:
		print(arr, k)
		n = len(arr)
		retval = self.quick_kthSmallest(k, 0, n - 1, arr)
		# your code must return a boolean
		# for example return True
		return retval


# Please make your function call as
# PA3_yourname.py 2,3,4,5 4

if __name__ == '__main__':
	arr = []
	arrtemp = sys.argv[1].split(",")
	for item in arrtemp:
		arr.append(int(item))

	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa2(arr, k)
	print(ret)

