# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# create variables and make up values for
#   - the number of hours worked in one week
#   - the hourly rate
#   - how much the week's paycheck will be
#   - write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

print("It's Monday!" if (str(input('Input a day of the week:\n')).lower()
 in ['mon', 'monday'])
 else 'It\'s not monday :(')

print("It's the weekend!" if (str(input('Input a day of the week:\n')).lower()
in ['sun', 'sunday', 'sat', 'saturday']) 
else 'It\'s not the weekend :(')

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

multiplicand = int(input('Enter a number: \n'))

for n in range(10):
    print(f'{multiplicand} x {n+1} = {multiplicand * (n+1)}')

for n in range(9):
    output = ''
    for i in range(n+1):
        output += str(n+1)
    print(output)

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

# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number.
#  (Hints: first make sure that the value the user entered is a valid number,
#  also note that the input function returns a string, so you'll need to convert this to a numeric type.)

is_not_digit = True
while is_not_digit:
    count_to = input('Enter a positive number to count to:\n')
    if count_to.isdigit():
        count_to = int(count_to) + 1
        if count_to >= 0:
            is_not_digit = False

for n in range(count_to):
    print(n)


# Write a program that prompts the user for a positive integer.
# Next write a loop that prints out the numbers from the number
# the user entered down to 1.

is_not_digit = True
while is_not_digit:
    count_from = input('Enter a positive number to countdown from:\n')
    if count_from.isdigit():
        count_from = int(count_from) + 1
        if count_from >= 0:
            is_not_digit = False

for n in range(count_from, 0, -1):
    print(n)

# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, 
# the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1, 101, 1):
    if n % 5 == 0 and n % 3 == 0:
        print('FizzBuzz')
    elif n % 5 == 0:
        print('Buzz')
    elif n % 3 == 0:
        print('Fizz')
    else:
        print(n)

#Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

is_not_digit = True
while is_not_digit:
    count_up = input('What number would you like to go up to? \n')
    if count_up.isdigit():
        count_up = int(count_up) + 1
        if count_up >= 0:
            is_not_digit = False

print('\nHere is your table!\n')
print('number | squared | cubed')
print('------ | ------- | -----')

for n in range(1, count_up, 1):
    print(f'{n:<7}| {n**2:<8}| {n**3}')
    to_continue = input('Do you want to continue?')
    if to_continue.lower() not in ['yes', 'y']:
        break

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

wants_to_continue = True
while wants_to_continue:
    grade = int(input('Input a grade from 0 to 100:\n'))

    if grade >= 95:
        print('A+')
    elif grade >= 90:
        print('A')
    elif grade >= 88:
        print('A-')
    elif grade >= 85:
        print('B+')
    elif grade >= 83:
        print('B')
    elif grade >= 80:
        print('B-')
    elif grade >= 75:
        print('C+')
    elif grade >= 70:
        print('C')
    elif grade >= 67:
        print('C-')    
    elif grade >= 64:
        print('D+')
    elif grade >= 62:
        print('D')
    elif grade >= 60:
        print('D-')
    else:
        print('F')
    if input('Do you want to stop?\n').lower() in ('y', 'yes'):
        wants_to_continue = False

#  Create a list of dictionaries where each dictionary represents a book
#  that you have read. Each dictionary in the list should have the keys title,
#  author, and genre. Loop through the list and print out information 
#  about each book.

# Prompt the user to enter a genre, then loop through your books 
#  and print out the titles of all the books in that genre.

books_read = [
    {
        'title': 'Harry Potter and the Scorerers Stone',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'Harry Potter and the Chamber of Secrets',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'Harry Potter and the Prizoner of Azkaban',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'Harry Potter and the Goblet of Fire',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'Harry Potter and the Order of the Phoenix',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'Harry Potter and the Half Blood Prince',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'Harry Potter and the Deathly Hallows',
        'author': 'J. K. Rowling',
        'genre': 'Fiction'
    },
    {
        'title': 'The Creature of Jekyll Island',
        'author': 'G. Edward Griffin',
        'genre': 'Non-Fiction'
    },
    {
        'title': 'The Bitcon Standard: The Decentralized Alternative to Central Banking',
        'author': 'Saifeadean Ammous',
        'genre': 'Non-Fiction'
    },
    {
        'title': 'I Am Number 4',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    },
    {
        'title': 'The Power of Six',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    },
    {
        'title': 'The Rise of Nine',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    },
    {
        'title': 'The Fall of Five',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    },
    {
        'title': 'The Revenge of Seven',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    },
    {
        'title': 'The Fate of Ten',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    },
    {
        'title': 'United as One',
        'author': 'Pittacus Lore',
        'genre': 'Fiction'
    }
]
book_count = 1
for book_dict in books_read:
    print(f'\nBook {book_count}')
    for key in book_dict.keys():
        print(f'{key}: {book_dict[key]}')
    book_count += 1

# Prompt the user to enter a genre, 
# then loop through your books list and
#  print out the titles of all the books in that genre.

genre = input('Enter a genre:\n').lower()
if genre in [each_book['genre'].lower() for each_book in books_read]:
    for each_title in [each_book['title'] for each_book in books_read if each_book['genre'].lower() == genre]:
        print(each_title)
else:
    print(f'Could not find the genre: {genre} in books read.')