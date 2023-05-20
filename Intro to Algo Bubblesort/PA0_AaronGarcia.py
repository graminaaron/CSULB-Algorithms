'''
Please use the code template below to complete your assignment.
Your code must be written in pa0 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa0 method would cause the evaluation program
failure and you will not get credit for your submission.

name: Aaron Garcia
studentID: 030556771

assignment:PA0
'''
import sys

class Solution:

	def data_conversion(self, data, convert_to):
		if convert_to == "int":
			return int(data)

		if convert_to == "list":
			new_input = []
			data = data.split(",")
			for item in data:
				new_input.append(int(item))

			return new_input

		if convert_to == "bool":
			return bool(data)

	def pa0 (self, s: list ) -> list:
		#temp variable
		temp_var = 0
		l = len(s) # use an int for range
		#for loop for each number
		for i in range(l-1):
			#compare against all other values
			for j in range(0, l-1-i):
				if(s[j] > s[j+1]):
					#swap values with temp variable
					temp_var = s[j]
					s[j] = s[j+1]
					s[j+1] = temp_var

		#return ending list
		return s
		# your code must return a boolean
		# for example return True


if __name__ == '__main__':
	# argv takes the input as a string.
	# to run pa1 we need to convert argv (or input data)
	# to the datatype that pa0 accepts.
	# data_conversion function converts an string to 
	# convert_to variable suitable for pa1 program input. 
	# "convert_to" variable can be one of the followings:
	# "list", "int", "bool"
	# note: a list of integers should be entered as a 
	# comma separated sequence in command line as input for a program.
	# For example, myproject.py 1,2,3,4,5

	# Setting convert_to variable
	convert_to = "list"

	# Read the input string from the command line
	s = sys.argv[1]

	# Craeting an object from Solution class
	obj = Solution()

	# Call "data_conversion" method to convert s (input string )
	# to a desire input datatype that is set for convert_to
	s = obj.data_conversion(s, convert_to)

	# calling tha pa0 mnethod to run the program
	ret = obj.pa0(s)

	print(ret)
