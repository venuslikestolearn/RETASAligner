import os, sys, math
odd=0
even=1
with open(sys.argv[1],'r') as file1, open(sys.argv[2],'w') as file2:
	lines = file1.readlines()	
	for i in range(0, len(lines)):
		try:
			file2.write(lines[odd].strip()+ ' --- ')
			file2.write(lines[even])
		except IndexError:
			pass
		odd=odd+2
		even=even+2
