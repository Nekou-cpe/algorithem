import matplotlib.pyplot as plt
import numpy as np
"""insertion sort"""
def insertionSort(arr):
    len_arr = len(arr)  # Get the length of the array
      
    if len_arr <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, len_arr):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  

"""selection sort"""
# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])


"""bubble sort"""
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
	
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	swapped = False
	# Traverse through all array elements
	for i in range(len_arr-1):
		# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, len_arr-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			# if we haven't needed to make a single swap, we 
			# can just exit the main loop.
			return

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
len_arr=int(input('please tell me how many numbers you want enter?'))
arr=[]
for i in range(len_arr):
	arr.append(int(input()))
	
insertion=insertionSort(arr)
print("sorting by insertion : ",'\n',arr)

selection=selectionSort(arr , len_arr)
print("sorting by selection sort : ",'\n',arr)

bubble = bubbleSort(arr)
print("sorting by bubble sort : ",'\n',arr)

x =np.arange()
y1 = [insertion[i] for i in insertion] 
y2 = [selection[i] for i in selection] 
y3 = [bubble[i] for i in bubble] 
plt.plot(x,y1) 
plt.plot(x,y2) 
plt.plot(x,y3) 
plt.title("order between insertion,selection,bubble sort") 
plt.xlabel("arr") 
plt.ylabel("y") 
plt.show() 


