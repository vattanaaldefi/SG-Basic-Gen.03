data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

x = readData(data1)
array = []
for each in x:
	if (each == "I" or each == "you" or each == "Then" or each == "and") :
		array.append('*'*len(each))
	else :
		array.append(each)

data = " ".join(array)
print(data)