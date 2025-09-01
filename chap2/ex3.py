def taxCalculator(income):
    # Convert income from VND to Million VND
    income_million = income / 1_000_000  
    
    if income_million < 5:
        tax = 0 + income_million * 0.05
    elif income_million <= 10:
        tax = 0.25 + (income_million - 5) * 0.10
    elif income_million <= 18:
        tax = 0.75 + (income_million - 10) * 0.15
    elif income_million <= 32:
        tax = 1.95 + (income_million - 18) * 0.20
    elif income_million <= 52:
        tax = 4.75 + (income_million - 32) * 0.25
    elif income_million <= 80:
        tax = 9.75 + (income_million - 52) * 0.30
    else:
        tax = 18.15 + (income_million - 80) * 0.30
    
    # Convert result back to VND
    return round(tax * 1_000_000, 2)


income1 = 4000000
tax1 = taxCalculator(income1)
print(f"taxCalculator({income1}) -> {tax1}")

income2 = 88000000
tax2 = taxCalculator(income2)
print(f"taxCalculator({income2}) -> {tax2}")