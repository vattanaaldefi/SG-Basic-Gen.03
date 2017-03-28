data = "DataSet.txt"

def readData(data):
	x = []
	with open(data) as data :
	    for line in data :
		    x = line.split()
	return x

text = readData(data)
digit = []
index = []
counter = 0
for each in text :
	if (each.isdigit() == True) :
		index.append(counter)
		digit.append(each)
	counter=counter+1
count = len(digit)-1
for i in index :
	text[i]  = digit[count]
	count= count-1

for i,each in enumerate(text) :

	if (each[len(each)-1] == ".") and (i!=len(text)-1):
		text[i+1] = (text[i+1])[0].upper() + (text[i+1])[1:]
text[0] = (text[0])[0].upper() + (text[0])[1:]


data = " ".join(text)
print(data)