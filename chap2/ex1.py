year_input = input("Enter a year: ")
try:
    year = int(year_input)
    if year <= 0:
        print("The number must be positive")
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("YES")
        else:
            print("NO")
except ValueError:
    print("Enter an integer, please")