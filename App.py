# Prompt for an integer
num = int(input("Enter a number to check: "))

# Check if the number is divisible by 2
if num % 5 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")
