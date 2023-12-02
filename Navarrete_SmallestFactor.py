def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return

    for i in range(2, n):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            break

# Get user input
user_input = int(input("Enter an Integer: "))
find_smallest_factor(user_input)

