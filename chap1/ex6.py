money = int(input("Enter an amount of money (divisible by 1000): "))
temp = money
# Tính số tờ 5000
fiveThousand = money // 5000
money %= 5000

# Tính số tờ 2000
twothousand = money // 2000
money %= 2000

# Tính số tờ 1000 (update repo master)
oneThousand = money // 1000
print(temp, "= [",fiveThousand,"]*5000", "+ [", twothousand, "]*2000", "+ [", oneThousand, "]*1000")
