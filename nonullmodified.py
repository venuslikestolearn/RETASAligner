import sys
one=[]
two=[]
lone=0
ltwo=0
with open(sys.argv[1],'r') as file1, open(sys.argv[2],'w') as file2:
	for line in file1:
		line= line.strip().split()
		if line[0]==line[1] and not one and not two:
			#file2.write(line[0]+'\n')
			#file2.write(line[1]+'\n')
			lone=0
			ltwo=0
		if line[0]==line[1] and one:
			if lone!=0 and ltwo==0:
				file2.write(' '.join(one) +'\n\n')
			else:
				file2.write(' '.join(one) +'\n')
			#file2.write(line[0]+'\n')
			#file2.write(line[1]+'\n')
			one=[]
			lone=0
			ltwo=0
			continue
		elif line[0]==line[1] and two:
			if lone==0 and ltwo!=0:
				file2.write(' '.join(two) +'\n\n')
			else:
				file2.write(' '.join(two) +'\n')
			two=[]
			#file2.write(line[0]+'\n')
			#file2.write(line[1]+'\n')
			lone=0
			ltwo=0
			continue	
		elif line[1] == "null" and not two:
				one.append(line[0])
				lone=len(one)
		elif line[0] == "null" and one:
			file2.write(' '.join(one) +'\n')
			lone=len(one)
			one=[]
			two.append(line[1])
			ltwo=len(two)
		elif line[0] == "null" and not one:
			two.append(line[1])
			ltwo=len(two)
	if one and not two:
		file2.write(' '.join(one) +'\n')
		one=[]
	if two and not one:
		file2.write(' '.join(two) +'\n')
		two=[]
			
			
