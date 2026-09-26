def prime(number):

    count = 0

    for row in range(1,number+1):

        if number % row == 0:

            count +=1

    return count




prime_number = prime(15)

if prime_number == 2:

    print("THe number is  prime number")

else:

    print("The number is not prime number")

