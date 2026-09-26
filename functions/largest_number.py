def largest_number():

    numbers = [10,20,30,40,50]

    largest = numbers[0]

    for row in numbers:

        if row > largest:

            largest = row

    return largest




largest_number = largest_number()

print("The largest Number",largest_number)



