def LCS(X,Y):
	xlen = len(X) #4
	ylen = len(Y) #2
	L = [[0 for x in range(ylen+1)] for x in range(xlen+1)]
	dir = [[0 for x in range(ylen+1)] for x in range(xlen+1)]
	
	# print(L)

	# Now filling the matrix L
	for i in range(xlen+1):
		for j in range(ylen+1):
			if i == 0 or j == 0:
				L[i][j] = 0
				dir[i][j] = 0

			elif X[i-1] == Y[j-1]:
				L[i][j] = 1 + L[i-1][j-1]
				dir[i][j] = "NE"

			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
				tempMax = max(L[i-1][j], L[i][j-1])

				if tempMax == L[i-1][j]:
					dir[i][j] = "E"
				else:
					dir[i][j] = "N" 

	# print(L)
	# print(dir)
	result = ""
	# print([i[::-1] for i in dir[::-1]])

	i = xlen
	j = ylen
	while(i > 0 and j > 0):
		# print("ï: ", i, " j: ", j, "\n")
		# print("dir[i][j] : ", dir[i][j])
		if dir[i][j] == "N":
			j = j -1
			i = i
		elif dir[i][j] == "E":
			i = i -1
			j = j
		elif dir[i][j] == "NE":
			i = i - 1
			j = j - 1
			result = result + X[i]
	
	result = result[::-1]
	print(result)
	
	# Lookup(L)

# Defining main function 
def main(): 
	# print("hey there")
	str1 = input("Ënter First string\n")
	str2 = input("Ënter Second string\n")
	# print(str1)
	# print(str2)
	# print(dir)
	LCS(str1, str2)
    
  
if __name__=="__main__": 
	main() 