age_input = input("Welcome to the program, user. Please enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    total_sum = 0
    for number in range(1, age + 1):
        total_sum += number
    print(f"The sum of all numbers from 1 to {age} is: {total_sum}")
else:
    print("Oops! Please enter a valid positive number for your age.")
