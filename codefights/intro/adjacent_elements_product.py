#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product.


def adjacentElementsProduct(inputArray):

     if len(inputArray) == 2:
        return inputArray[0] * inputArray[1]
    
    highest = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        temp = inputArray[i] * inputArray[i+1]
        if temp > highest:
            highest = temp
            
            
            
    return highest


def adjacentElementsProduct(inputArray):

    return max([inputArray[i]* inputArray[i+1] for i in range(len(inputArray) -1)])



def adjacentElementsProduct(inputArray):

    return max([ x*y for x, y in zip(inputArray, inputArray[1:])])