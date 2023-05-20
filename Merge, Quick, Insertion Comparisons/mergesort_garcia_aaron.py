'''
1- Please use the code template below to complete your assignment.
2- Your code must be written in the pa1_mergesort method. 
3- You can define as many as functions needed but 
4- Your algorithms' execution must be started from the 
   pa1_mergesort method.
5- Do not change any other code. 
6- The evaluation code uses this template to run your test cases.
   Any changes other than the pa1_mergesort method would cause 
   the evaluation program error and you will not get credit for your
   submission.


name: Aaron Garcia
studentID: 030556771

assignment:PA1
'''

import sys
import random
import time

# to allow our sorting function to sort large arrays
sys.setrecursionlimit(2500)

class Solution:
	
# this function returns a descending sorted array.
	def function_a (self, elements_count: int) -> list:
		output = []
		for i in range(elements_count,0, -1):
			output.append(i)
		return output

	# this function returns an ascending sorted array.	
	def function_b (self, elements_count: int) -> list:
		output = []
		for i in range(1, elements_count):
			output.append(i)
		return output

	# this function returns a randomly generated array	
	def function_c(self, elements_count: int, seed: int):
		output = []
		random.seed(seed)
		for i in range(0,elements_count+1):
			output.append(random.randint(1,1000000))

		return output

	# this function selects a correct action based on the input a, b or c.	
	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if 	input_type == "b":
			output = self.function_b(elements_count)
		if 	input_type == "c":
			output = self.function_c(elements_count, seed)
		return output	

	def merge(self, left, mid, right, arr):
		n1 = mid - left + 1
		n2 = right - mid

		# create temp subarrays
		lh_arr = [0] * n1
		rh_arr = [0] * n2

		# copy data to the temp subarrays above
		for i in range(0, n1):
			lh_arr[i] = arr[left + i]

		for j in range(0, n2):
			rh_arr[j] = arr[mid + 1 + j]

		# create initial indices for the temp subarrays
		i = 0 # first subarray
		j = 0 # second subarray
		k = left # merged subarray

		# compare the two sub arrays and sort through them
		while i < n1 and j < n2:
			if lh_arr[i] > rh_arr[j]:
				arr[k] = lh_arr[i]
				i = i + 1
			else:
				arr[k] = rh_arr[j]
				j = j + 1
			k = k + 1

		# if there are any remaining elements of the left hand arr,
		# copy them to the original arr
		while i < n1:
			arr[k] = lh_arr[i]
			i = i + 1
			k = k + 1

		# if there are any remaining elements of the right hand arr,
		# copy them to the original arr
		while j < n2:
			arr[k] = rh_arr[j]
			j = j + 1
			k = k + 1


	def merge_sort(self, left, right, arr):
		if left < right:
			# calc mid
			mid = int((left + (right-1)) / 2)

			# recurse through the array
			self.merge_sort(left, mid, arr)
			self.merge_sort(mid+1, right, arr)

			# merge the two halfs
			self.merge(left, mid, right, arr)


	def pa1_mergesort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)

		# get the start time
		st = time.process_time()
		
    	# your merge sort algorithm comes here ...
		self.merge_sort(0, n - 1, query_list)
    	# end of merge sort
		
		et = time.process_time()
		res = et - st

		return [query_list, res]




if __name__ == '__main__':
	# the input type is either a, b or c 
	# corresponding to function_a, function_b and functin_c.
	input_type = sys.argv[1]

	elements_count = int(sys.argv[2])

	# input seed as 2, so we have the same randomly 
	# generated array.
	# you can change it for your testing.
	seed = sys.argv[3]
	
	obj = Solution()
	# the return value is an array of array.
	ret = obj.pa1_mergesort(input_type, elements_count, seed)
	print(ret)

