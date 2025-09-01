def maxFiveNumbers(a, b, c, d, e):
    max_value = a 
    
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    if d > max_value:
        max_value = d
    if e > max_value:
        max_value = e
    
    return max_value


# Test cases
print(f"maxFiveNumbers(4, 8, 6, 1, 7) => {maxFiveNumbers(4, 8, 6, 1, 7)}")
print(f"maxFiveNumbers(15.6, 8.3, 65.8, 0.1, 11.7) => {maxFiveNumbers(15.6, 8.3, 65.8, 0.1, 11.7)}")