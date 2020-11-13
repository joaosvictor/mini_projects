# the time complexity is О(n^2)

arr=[84,2,78,67,9,1,5]
for i in range(len(arr)):
	n = len(arr)
	for i in range(n-1):
		for j in range(0,n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1],arr[j]

print(arr) # [1,2,5,9,67,78,84]
