def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Get the set of numbers from the user
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter element {}: ".format(i+1)))
    numbers.append(num)

# Count even and odd numbers
even_count, odd_count = count_even_odd(numbers)

# Print the results
print("Even count: ", even_count)
print("Odd count: ", odd_count)
