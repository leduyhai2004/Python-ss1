def money_exchange():
    # Get input from user
    amount = int(input("Enter an amount of money (divisible by 1000): "))
    
    # Validate input
    if amount % 1000 != 0:
        print("Error: Amount must be divisible by 1000")
        return
    
    if amount <= 0:
        print("Error: Amount must be positive")
        return
    
    # Calculate coins using greedy algorithm
    coin_5000 = amount // 5000
    remaining = amount % 5000
    
    coin_2000 = remaining // 2000
    remaining = remaining % 2000
    
    coin_1000 = remaining // 1000
    
    # Display the result
    print(f"{amount} = [ {coin_5000} ]*5000 + [ {coin_2000} ]*2000 + [ {coin_1000} ]*1000")

# Run the program
money_exchange()