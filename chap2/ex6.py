def readFourDigits(number):
    # Special case for zero
    if number == 0:
        return 'zero'
    
    # Define word mappings
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    result = []
    
    # Extract digits
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    remainder = number % 100
    
    # Handle thousands
    if thousands > 0:
        result.append(ones[thousands])
        result.append('thousand')
    
    # Handle hundreds
    if hundreds > 0:
        result.append(ones[hundreds])
        result.append('hundred')
    
    # Handle tens and ones
    if remainder >= 20:
        tens_digit = remainder // 10
        ones_digit = remainder % 10
        result.append(tens[tens_digit])
        if ones_digit > 0:
            result.append(ones[ones_digit])
    elif remainder >= 10:
        # Handle teens (10-19)
        result.append(teens[remainder - 10])
    elif remainder > 0:
        # Handle single digits (1-9)
        result.append(ones[remainder])
    
    # Join with 'and' where appropriate
    final_result = []
    i = 0
    while i < len(result):
        if i > 0 and (result[i-1] == 'thousand' or result[i-1] == 'hundred'):
            final_result.append('and')
        final_result.append(result[i])
        i += 1
    
    return ' '.join(final_result)

# Test the function with the examples
print("Testing readFourDigits function:")
print(f"readFourDigits(4517): '{readFourDigits(4517)}'")
print(f"readFourDigits(9872): '{readFourDigits(9872)}'")
print(f"readFourDigits(5000): '{readFourDigits(5000)}'")
print(f"readFourDigits(3003): '{readFourDigits(3003)}'")

# Additional test cases
print(f"readFourDigits(1234): '{readFourDigits(1234)}'")
print(f"readFourDigits(0): '{readFourDigits(0)}'")
print(f"readFourDigits(15): '{readFourDigits(15)}'")
print(f"readFourDigits(100): '{readFourDigits(100)}'")