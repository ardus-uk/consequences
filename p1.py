#!/usr/bin/python
""" Some examples of how to open a file and read data from it """
# Author:  Peter Normington
# Last revision: 2013-11-14

example_number = 0

# The following is used to divide the sections of output
print "--------------------------------------------\n"
example_number = example_number + 1
print "Example ", example_number, "\n"
# Open a file in read-only mode
with open('./datafiles/Consequences', 'r') as f:
# f is a file handle. 
# Read the first line and print it out
	line = f.readline()
	print line
# Read the second line and print it out	
	line = f.readline()
	print line
	
print "--------------------------------------------\n"
example_number = example_number + 1
print "Example ", example_number, "\n"
with open('./datafiles/Consequences', 'r') as f:
	# Read the file line-by-line and print out each line as it is read
	for line in f:
		print line

print "--------------------------------------------\n"
example_number = example_number + 1
print "Example ", example_number, "\n"
with open('./datafiles/Consequences', 'r') as f:
# f is a file handle. 	
	# Read the whole file in one big slurp
	contents = f.read()
	# Print it out
	print contents
		
print "--------------------------------------------\n"
example_number = example_number + 1
print "Example ", example_number, "\n"
with open('./datafiles/Consequences', 'r') as f:
# f is a file handle. 	
	# Read the whole file in one big slurp into a list
	contents_as_a_list_of_lines = f.readlines()
	# Print the lines out one by one
	for line in contents_as_a_list_of_lines:
		print line
		
print "--------------------------------------------\n"
example_number = example_number + 1
print "Example ", example_number, "\n"
with open('./datafiles/Consequences', 'r') as f:
# f is a file handle. 	
	# Read the whole file in one big slurp into a list
	contents_as_a_list_of_lines = f.readlines()
	# Print them out one by one with line numbers
	line_number = 0
	for line in contents_as_a_list_of_lines:
		line_number = line_number+1
		print line_number, ": " , line
		
print "--------------------------------------------\n"	
		

