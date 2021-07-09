## Conditional Baiscs
#a) prompt user for a day of the week, print out whether the day is Monday or not
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

# Loop basics
# a) While:
i = 5
while i <= 15:
    print(i)
    i += 1

count = 0
while count <= 100:
    print(count)
    count += 2

backward_count = 100
while backward_count >= -10:
    print(backward_count)
    backward_count -= 5

num_squared = 2
while num_squared < 1000000:
    print(num_squared)
    num_squared = num_squared ** 2

decrease_by_5 = 100
while decrease_by_5 >= 5:
    print(decrease_by_5)
    decrease_by_5 -= 5

# For loops
# Write some code that prompts the user for a number, then shows a multiplication
#  table up through 10 for that number.

# multiplicand = int(input('Enter a number: \n'))

# for n in range(10):
#     print(f'{multiplicand} x {n+1} = {multiplicand * (n+1)}')

# for n in range(9):
#     output = ''
#     for i in range(n+1):
#         output += str(n+1)
#     print(output)


user_num = input('Enter an ODD number between 1 and 50:\n')

while user_num.isdigit() == False:
    print('That wasn\'t a number, try again.')
    user_num = input('Enter an ODD number between 1 and 50:\n')
while (user_num % 2) != 1 or user_num<1 or user_num>50:
    if user_num < 1:
        print('Number is below 1, enter a number GREATER than 1')
    elif user_num > 50:
        print('Number is above 50, enter a number LESS THAN than 50')
    else:
        print('That wasn\'t an ODD number, try again.')
    user_num = input('Enter an ODD number between 1 and 50:\n')

for n in range(51):
    if n % 2 == 0 or n == int(user_num):
        continue
    print(n)
