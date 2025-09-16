# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True


def is_prime(n):
    if n < 2:
        return False    # Số < 2 không phải số nguyên tố
    for i in range(2, n):
        if n % i == 0:  # Nếu n chia hết cho i thì không phải số nguyên tố
            return False
    return True         # Nếu không chia hết cho số nào thì là số nguyên tố

def countPrime(left: int, right: int) -> int:
    count = 0
    for num in range(left, right + 1):
        if is_prime(num):
            count += 1
    return count


# Example test cases
print(countPrime(1, 10))   # Output: 5  (2, 3, 5, 7)
print(countPrime(15, 20))  # Output: 2  (17, 19)
