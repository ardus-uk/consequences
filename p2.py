#!/usr/bin/python
""" Some examples of using lists """
# Author:  Peter Normington
# Last revision: 2013-11-18

example_number = 0

# The following is used to divide the sections of output
print "--------------------------------------------\n"
with open('./datafiles/Consequences', 'r') as f:
# f is a file handle. 	
	# Read the whole file in one big slurp into a list
	contents_as_a_list_of_lines = f.readlines()
	example_number = example_number + 1
	print "Example", example_number, "\n"

	# use the list indices
	print contents_as_a_list_of_lines[1]
	print contents_as_a_list_of_lines[6]
	
		
	print "--------------------------------------------\n"	

	example_number = example_number + 1
	print "Example", example_number, "\n"

	# Use the list indices in a loop
	# Note that the first argument to range() is the starting value; 
	# the second agument is the number that the sequence goes up to (but is not included)
	for i in range(1,7):
		print contents_as_a_list_of_lines[i]
		
	print "--------------------------------------------\n"	

	example_number = example_number + 1
	print "Example", example_number, "\n"

	# Use the list indices in a loop
	# Note that the third argument to range() is the increment
	for i in range(6,0, -1):
		print contents_as_a_list_of_lines[i]
		
	print "--------------------------------------------\n"	

	example_number = example_number + 1
	print "Example", example_number, "\n"

	# Get rid of those pesky newline characters!
	for i in range(6,0, -1):
		print contents_as_a_list_of_lines[i].strip()

	print "--------------------------------------------\n"	

	example_number = example_number + 1
	print "Example", example_number, "\n"
	# We can shuffle the order by using the "shuffle" function from the "random" package
	from random import shuffle
	indexes = range(1,7)
	print "Before shuffling: "
	print indexes
	shuffle(indexes)
	print "After shuffling: "
	print indexes
	for i in indexes:
		print contents_as_a_list_of_lines[i].strip()
	
		
print "--------------------------------------------\n"	
		

