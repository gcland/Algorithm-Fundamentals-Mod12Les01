#Case Study: Analyzing Big O Complexity for a Sorting Algorithm


#1

def simple_sort(arr):      #given array 'arr' - trying to sort elements ascending
    n = len(arr)    #gets length of arr
    for i in range(n):  #i is index of array, loops through each element in arr
        for j in range(0, n-i-1):   #loops through each element in range 0 - (arr-index-1), index of this array is j
            if arr[j] > arr[j+1]: #if the current element in arr is greater than the next element in the array: (perform next line)
                arr[j], arr[j+1] = arr[j+1], arr[j] # swap position of current element and next element
    print(arr)
arr = [10, 4, 2, 1, 20, -1, 8, -5]

# simple_sort('Simple:', arr)


#2

# With two for loops one nested within another this algorithm is quadratic O(n)
# As the size of the input grows the run time grows exponentially

#3

#The above array is quadratic O(n^2). In sorting, two comparisons will need to be run to move variables across the array

# Alternative (but similar):

def sort2(arr):
    for i in range(1, len(arr)): #start at 1 (because comparison to prev index) to end of arr
        j = i - 1 # j = index - 1 (previous index)

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their index
        #stops loop when a swap occurs or current value at index (i) is greater than current value at prev index (j)
        while j >= 0 and arr[i] < arr[j]: 
            arr[j + 1] = arr[j] #value at i (arr[j+1]) becomes value at j (arr[j])
            j -= 1 
        arr[j + 1] = arr[i]
    print(arr)


sort2(arr)

#This method is quadratic as is the simple_sort above. I prefer simple_sort due to fewer lines of code and being easier to read