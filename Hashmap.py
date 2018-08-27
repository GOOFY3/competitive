# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_length, sum):
    s = set()
    for i in range(0, arr_length):
        temp = sum - arr[i]
        print(temp)
        if(temp >=0 and temp in s):
            print("match found %d %d", temp, arr[i])
        s.add(arr[i])
# driver program to check the above function
A = [1,4,45,6,10,-8]
n = 16
printPairs(A, len(A), n)

# This code is contributed by __Devesh Agrawal__
