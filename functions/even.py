

def even(numbers):
    count =0
    for row in numbers:

        if(row%2==0):
            count +=1

    print("Count of even numbers",count)

numbers = [10, 15, 22, 33, 40, 51, 60]

even_numbers = even(numbers)