# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    n = len(numbers)
    total = 0.0 
    for number in numbers:
        total += number
    return(total/n)

print(average([1,2,3,3,4,5,6,7,8]))


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
