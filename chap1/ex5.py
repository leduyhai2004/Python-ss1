number = int(input("Enter a number (from 0 to 999): "))
sum_of_digits = (int)(number//100) + (int)((number//10)%10) + (int)(number%10)
print("The sum of digits is:", sum_of_digits)