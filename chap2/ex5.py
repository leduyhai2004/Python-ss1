def daysOfWeek(day: int, month: int, year: int) -> str:
    # Step 1: Compute y0
    y0 = year - (14 - month) // 12
    
    # Step 2: Compute x0
    x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
    
    # Step 3: Compute m0
    m0 = month + 12 * ((14 - month) // 12) - 2
    
    # Step 4: Compute D
    D = (day + x0 + (31 * m0) // 12) % 7
    
    # Mapping to days
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    return days[D]

print(daysOfWeek(29, 9, 2022))  # 'Thursday'
print(daysOfWeek(2, 10, 2022))  # 'Sunday'
