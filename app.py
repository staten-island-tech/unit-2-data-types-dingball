def find_factors(number):
    factors = []  # Initialize an empty list to store factors
    for i in range(1, number + 1):  # Loop through all integers from 1 to number (inclusive)
        if number % i == 0:  # Check if i is a factor of number
            factors.append(i)  # Append the factor to the list
    return factors  # Return the list of factors

print(find_factors(100))  # Call the function with 100 and print the result