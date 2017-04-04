kurung = ['(',')']
s = []

valid = "Valid"

for i in kurung :
	if (i == '(') :
		s.append(i)
	elif (i == ')') :
		if (len(s) != 0) :
			for j in s :
				if (j == '(') :
					s.remove(j)
					valid = "Valid"
					break
				elif (j != '(') :
					valid = "Tidak Valid"
					break
		elif (len(s) == 0) :
			valid = "Tidak Valid"
			break

if (len(s) != 0) :
	valid = "Tidak Valid"

print(s)
print(valid)

		