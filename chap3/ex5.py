def sentinelInput():
    total = 0    # Tổng các số đã nhập
    count = 0    # Số lượng các số đã nhập
    
    while True:
        user_input = input("Enter a positive integer: ")
        
        # Kiểm tra xem có phải là số không
        try:
            num = int(user_input)
        except ValueError:
            print("Please enter a number")
            continue
        
        # Kiểm tra các trường hợp
        if num == 0:
            # Dừng và tính trung bình
            break
        elif num < 0:
            print("The number must be positive")
        else:
            # Số dương: cộng vào tổng và tăng đếm
            total += num
            count += 1
    
    # Tính và trả về trung bình
    #
    if count > 0:
        average = total / count
        return round(average, 2)
    else:
        return 0

# Test function (uncomment to run)
# update at repo
result = sentinelInput()
print(f"Average: {result}")

