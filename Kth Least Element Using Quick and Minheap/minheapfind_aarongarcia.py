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

class Solution:

	# heap referencing functions, taken from slides
	def parent(self, i) -> int:
		return int((i - 1)/2)
	def left(self, i) -> int:
		return int(i*2 + 1)
	def right(self, i) -> int:
		return int(i*2 + 2)
	
	# wrapper function to help understand psedocode better
	def heap_size(self, arr):
		return len(arr)

	# maintain heap property - heap will natural settle into min heap
	def heapify(self, arr, boundary, i):
		larger = i
		left = self.left(i)
		right = self.right(i)
		
		# the idea to work opposite of the smaller value to traverse through the
		# tree and heapify the ith smallest value to its proper position 

		# if left is inbounds of the array and the left-child node is greater than current node:
		if (left < boundary and arr[left] > arr[larger]):
			# let larger be the left hand side 
			larger = left
		
		# if right is inbounds of the array and the right-child node is greater than current node:
		if (right < boundary and arr[right] > arr[larger]):
			# let larger be the right hand side 
			larger = right

		if (larger != i):
			# swap root and larger node values
			arr[i], arr[larger] = arr[larger], arr[i]
			self.heapify(arr, boundary, larger)

	# build list into min heap
	def build_heap(self, arr):
		length = self.heap_size(arr)
		for i in range(int(length/2), -1, -1):
			self.heapify(arr, length, i)

	# this is a heapsort function that implements minheap
	def minheap_kthSmallest(self, arr):
		self.build_heap(arr)
		for i in range(self.heap_size(arr)-1, -1, -1):
			# swap values
			arr[0], arr[i] = arr[i], arr[0]
			self.heapify(arr, i, 0)
			
		return arr
	
	# driver function for the assignment
	def pa2 (self, arr: list[int], k: int )	-> int:
		print(arr, k)
		n = len(arr)
		arr = self.minheap_kthSmallest(arr)
		# print the outcome array for debugging purposes
		print(arr)
		# retreve value of the array at the index of the kth element
		retval = arr[k-1]
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

