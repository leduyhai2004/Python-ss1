def pythagoreanTriplets(num):
    """
    Find all Pythagorean triplets (a, b, c) where:
    - a, b, c are integers
    - a² + b² = c²
    - 0 < a ≤ b < c ≤ num
    """
    # Iterate through all possible combinations of a, b, c
    for a in range(1, num + 1):
        for b in range(a, num + 1):  # b >= a 
            for c in range(b + 1, num + 1):  # c > b 
                # Check if it forms a Pythagorean triplet
                if a * a + b * b == c * c:
                    print((a, b, c))

# Test the function
print("pythagoreanTriplets(10):")
pythagoreanTriplets(10)

print("\npythagoreanTriplets(20):")
pythagoreanTriplets(20)

"""
def pythagoreanTriplets(num):
    triplets = []
    
    # Iterate through all possible values of a and b
    for a in range(1, num + 1):
        for b in range(a, num + 1):  # b >= a to maintain a ≤ b
            # Calculate c² and check if it's a perfect square
            c_squared = a * a + b * b
            c = int(c_squared ** 0.5)
            
            # Check if c is valid and forms a Pythagorean triplet
            if c * c == c_squared and c <= num and b < c:
                triplets.append((a, b, c))
    
    # Print all found triplets
    for triplet in triplets:
        print(triplet)

# Test the function
print("pythagoreanTriplets(10):")
pythagoreanTriplets(10)

print("\npythagoreanTriplets(20):")
pythagoreanTriplets(20)
"""
