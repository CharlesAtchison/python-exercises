# Author: Charles Atchison
# Created: 7/11/21
# Exercises for CodeUp demonstrating function use and other various features within Python.


# 1)
def is_two(inpt):
    '''
    Define a function named is_two. 
    It should accept one input and return True if the passed
    input is either the number or the string 2, False otherwise.'''

    # Takes input of any type and then converts it to a string to test if is '2'
    return True if str(inpt) == '2' else False

# 2)
def is_vowel(some_char):
    '''
    Returns True if some_char is a vowel, and False otherwise'''

    # Takes a string input and lowers the case and then iterates through list of vowels
    # to see if the char is in that list, and returns a Bool True if is
    return True if some_char.lower() in [vowel for vowel in 'aeiou'] else False

# 3)
def is_consonant(some_char):
    '''
    Returns True if some_char is a consonant otherwise returns False'''

    # Takes a string input and lowers the case and then iterates through list of consonants
    # to see if the char is in that list, and returns a Bool True if is
    return True if some_char.lower() in [char for char in 'bcdfghjklmnpqrstvwxyz'] else False

# 4)
def capitalize(some_string):
    '''
    Capitalizes the first letter if the string starts with a consonant.'''

    # takes a string and capitalizes the first char if it 
    #  is a consonant (refers to previous funct) which returns a True/False
    return some_string.capitalize() if is_consonant(some_string[0]) else some_string

# 5)
def calculate_tip(tip_percentage, bill):
    '''
    Takes number between 0 and 1( float) and bill amount (float/int) and returns the amount to tip'''

    # Takes a float tip_percentage and a bill amount (float/integer) and returns a formatted
    # string that multiplies the bill amount by the tip to 2 decimal places
    return f'${(bill * tip_percentage):0.2f}'

# 6)
def apply_discount(orig_price, disc_percent):
    '''
    Takes an original price and a discount percentage as an int
     and returns the price after discount'''

    # Takes an integer or float original price and an integer disc_percentage
    # It takes the disc_percent divides by 100 to get the discount in decimal.
    # Then subtracts that decimal from 1 to get the decimal that the person will pay 
    # and multiplies it by the original price and returns it as a currency formatted str.
    return f'${(orig_price * (1-(disc_percent/100))):0.2f}'
# 7)
def handle_commas(num_as_string):
    '''
    removes commas from a string input number and returns value as an int'''

    # Takes a string and uses the 'replace()' method to replace commas with nothing. 
    # Then it returns a converted string into an integer
    return int(num_as_string.replace(',', ''))

# 8)
def get_letter_grade(grade_num):
    '''
    takes a number, integer and returns a string letter grade associated with that number (A-F)'''

    # If grade_num isn't an int or float it will just return the string that is not a 
    # valid number.
    if type(grade_num) != int and type(grade_num) != float:
        return 'That is not a valid number'
    # Test cases for each grade where the cutoff is every 10%
    if grade_num >= 90:
        return 'A' 
    elif grade_num >= 80:
        return 'B'
    elif grade_num >= 70:
        return 'C'
    elif grade_num >= 60:
        return 'D'
    elif grade_num >=0:
        return 'F'
    # If the number was greater than 100 or lower than 0 it returns this string.
    else:
        return 'Grade must be between 0-100'

# 9)
def remove_vowels(inpt_string):
    '''
    Takes a string input and removes the vowels'''

    # sets a null new_string to put the string in as it removes the vowels 
    new_str = str()

    # Iteraters through each character and uses the is_vowel funct to return if it is or not
    # if it is not a vowel, it will add it to the new_str and be returned after all iterations
    for each_char in inpt_string:
        if is_vowel(each_char) == False:
            new_str += each_char
    return new_str

# 10)
def normalize_name(some_str):
    '''
    takes a string and removes invalid python identifiers'''

    # Sets a blank new_string to put the values in after we check if they are valid
    new_string = None

    # Iterates through each char in the string
    for each_char in some_str:
        # If the new_string is still None, it will check only for a number or an alpha numeric
        # value so that the leading whitespace is removed and then adds the first char to the
        # new string
        if not new_string:
            if each_char.isnumeric() or each_char.isalnum():
                new_string = each_char
        
        # If the new_string has a value, it will check if each char is an alpha numeric 
        # value, a number, or is a space, everything else will not be added to the new str
        elif each_char.isnumeric() or each_char.isalnum() or each_char.isspace():
            new_string += each_char
    
    # The cleaned string new is put all to lowercase, the strip() method removes all trailing
    # whitespace that may exist and the replace() method replaces all spaces with underscores
    return new_string.lower().strip().replace(' ', '_')
    
# 11)
def cumulative_sum(lst_of_nums):
    '''
    Takes a list of numbers and returns a list that is the cumulative sum.

    Example:
    cumulative_sum([1, 1, 1]) returns [1, 2, 3]'''

    # Takes the list lst_of_nums, enumerates through the iteration to get a changing index
    # which will start at 1 (the first value, 0 will be itself) and then sums the 
    # dynamically shifting index which will be a list
    return [sum(lst_of_nums[0:n]) for n, each_num in enumerate(lst_of_nums, 1)]

# 12)
def twelveto24(time):
    '''
    Takes a string in the format of HH:MM am/pm
     and converts to a string representing 24 hour time'''

    # Splits the time into hours, minutes and then sets is_pm to True if it the 'pm' string is on the end
    hours, minutes, is_pm = time.split(':')[0], time.split(':')[1][0:2], (True if (time.split(':')[1][2:]) == 'pm' else False)

    # converts hours to an int and adds 12 if is_pm is True, then concats the ':' with minutes
    return str((int(hours)+12 if is_pm else hours)) + ':' +str(minutes)

# 13) 
def twentyfourto12(time):
    '''
    Takes a time string in 24 hour format and 
    converts it back to 12 hour time as a string'''

    # Splits hours and minutes on the ':' into strings and formats as ints to perform tests
    hours, minutes = int(time.split(':')[0]), int(time.split(':')[1])

    # Formats hours into an integer to divide by 12 to see if it is greater than 1,
    #  which would mean that it is_pm (True)
    is_pm = True if (hours / 12) >= 1 else False

    # Converts hours to str after subtracting 12 if is_pm is True and then concats 
    # ':' to the minutes and adds 'pm' if is_pm is True and 'am' if it's False
    return str(hours-12 if is_pm else hours) + ':' + str(minutes) + ('pm' if is_pm else 'am')
    
# 14)
def col_index(sprdsht_col_name):
    '''
    Takes a spreadsheet col name as a string and returns the index as an int

    Example:
    col_index('A') returns 1
    col_index('B') returns 2
    col_index('AA') returns 27
    '''
    
    # lowers the spreadsheet col name to compare to lowercase chars
    sprdsht_col_name = sprdsht_col_name.lower()
    
    # The count will have string numbers to hold raw letter values in each position
    count = ''

    # Iterates through each column within the col_name numerically
    # Such as there would be 3 columns for the col_index name ('AAA')
    for each_col in range(len(sprdsht_col_name)):
        # Iterates through the alphabet useing enumerate to keep count of what letter value (starting at 1)
        for n, each_char in enumerate([each_letter for each_letter in 'abcdefghijklmnopqrstuvwxyz'], 1):
            # If the character is the same as that specific col name, it adds that count STRING to 
            # the coun and then stops the iteration and begins on the next col
            if each_char == sprdsht_col_name[each_col]:
                count += str(n)
                break
    
    # This sets the mathematical total to 0
    total = 0
    # Since the matematical extrapolation requires more than 1 digit, just return same val
    # for any col_index of len 1
    if len(count) == 1:
        return (int(count))
    # If there is a col length greater than 1, iterate through each count place holder (str)
    else:
        # enumerate through each value to get the index (base 1) and placeholder value (str)
        for n, each_val in enumerate(count, 1):
            # Checks if the last value is up by comparing length of orig string to what index
            # is currently being checked.
            if n == len(count):
                # Adds raw value, after converted to an int to the total int
                total += int(each_val)
            else:
                # If it is not the final value, multiply the value by 26 to count the iterations required
                # Example: 
                # the Col_index of 'BB' would have the count of '22' as string and would require 2 
                # iterations through the alphabet to get the first 'B' which would be 26 * 2 = 52
                # then it would require 2 more tests 'A then B' to get to 'B' being 2.
                # Therefore, 52+2 = 54.
                total += int(each_val) * 26
    return total
