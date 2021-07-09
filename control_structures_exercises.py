## Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
## FIXME
# print("It's Monday!" if (str(input('Input a day of the week:\n')).lower()
#  in ['mon', 'monday'])
#  else 'It\'s not monday :(')

# print("It's the weekend!" if (str(input('Input a day of the week:\n')).lower()
# in ['sun', 'sunday', 'sat', 'saturday']) 
# else 'It\'s not the weekend :(')

one_week = 63
payrate = 50
weekly_pay = ((one_week % 40) * (payrate * 1.5)) + ((one_week-(one_week % 40)) * payrate)
print(weekly_pay)

# Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100.
#   Follow each number with a new line.
count = 0
while count <= 100:
    print(count)
    count += 2

# Alter your loop to count backwards by 5's from 100 to -10.
backward_count = 100
while backward_count >= -10:
    print(backward_count)
    backward_count -= 5

# Create a while loop that starts at 2, and displays the number squared on each 
#   line while the number is less than 1,000,000.

num_squared = 2
while num_squared < 1000000:
    print(num_squared)
    num_squared = num_squared ** 2

# For loops
# Write some code that prompts the user for a number, then shows a multiplication
#  table up through 10 for that number.
# FIXME
# multiplicand = int(input('Enter a number: \n'))

# for n in range(10):
#     print(f'{multiplicand} x {n+1} = {multiplicand * (n+1)}')
# 7
# for n in range(9):
#     output = ''
#     for i in range(n+1):
#         output += str(n+1)
#     print(output)

# Prompt the user for an odd number between 1 and 50.
#  Use a loop and a break statement to continue prompting the user if they enter invalid input.
#  (Hint: use the isdigit method on strings to determine this).
#  Use a loop and the continue statement to output all the odd numbers between
#  1 and 50, except for the number the user entered.
user_num = input('Enter an ODD number between 1 and 50:\n')

# Check if number is a digit
while user_num.isdigit() == False:
    print('That wasn\'t a number, try again.')
    user_num = input('Enter an ODD number between 1 and 50:\n')

while int(user_num) < 1 or int(user_num) > 50 or int(user_num) % 2 == 0:
    if int(user_num) < 1:
        print(f'{user_num} is too low, enter a higher number')
    elif int(user_num) > 50:
        print(f'{user_num} is too high, enter a lower number')
    else:
        print(f'{user_num} is not odd, enter an odd number')
    user_num = input()

for n in range(51):
    if n % 2 == 0 or n == int(user_num):
        if n == int(user_num):
            print(f'Yikes! Skipping number: {n}')
        continue
    print(f'Here is odd number: {n}')

