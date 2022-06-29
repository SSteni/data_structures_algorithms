Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Method 1: This method uses the technique of the Summation formula.

Approach:

# The length of the array is n-1. So, the sum of all n elements i.e. sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. 
# Now find the sum of all the elements in the array and subtract it from the sum of the first n natural numbers, it will give us the value of 
# the missing element.

# Algorithm:

# Calculate the sum of the first n natural numbers as sumtotal= n*(n+1)/2 Create a variable sum to store the sum of the array elements. 
# Traverse the array from start to end. Update the value of sum as sum = sum + array[i] Print the missing number as SumTotal – sum Below 
# is the implementation of the above approach:

def getmissingNo(A):
    n = len(A)
    print(n)
    total = (n+1)*(n+2)/2
    sum_a = sum(A)
    return total - sum_a

A = [1,2,3,4,5,6,8]
getmissingNo(A)


# Complexity Analysis:

# Time Complexity: O(n). Only one traversal of the array is needed.
# Space Complexity: O(1). No extra space is needed

def getMissingNos(a, n):
    n = len(a)+1
    n_elements_sum=n*(n+1)//2
    return n_elements_sum-sum(a)

a = [1, 2, 4, 5, 6]
getMissingNos(a,7)
