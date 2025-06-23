# function print max and  min value from an integer array

def Max_Min(numbers:int)-> tuple[int, int]:

    max = numbers[0]

    min = numbers[0]

    count = len(numbers)

    for index in range(1, count, 1):

        if numbers[index] > max:
            
            max = numbers[index]

        if numbers[index] < min:

            min = numbers[index]

    return max,min
    
# invocation code

input  = [1, 2, 3, 5, 10, -1]

max_value, min_value = Max_Min(input)



print(f"Max of value is {max_value}, Min of values is {min_value}")