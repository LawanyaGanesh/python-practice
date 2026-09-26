print("Enter the year")
year = int(input())

print("Entered Year",year)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):

    print("The year is leap year")

else:

    print("The year is not leap")