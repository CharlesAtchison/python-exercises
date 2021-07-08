# This is the first question answer 
the_little_mermaid = 3
brother_bear = 5
hercules = 1

def movie_cost(movie):
    return movie * 3

print(f'You would have to pay {movie_cost(the_little_mermaid) + movie_cost(brother_bear) + movie_cost(hercules)} dollars.')


# Suppose you're working as a contractor for 3 companies: 
# Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

goolge = 400
amazon = 380
facebook = 350

answer = (facebook * 10) + (goolge * 6) + (amazon * 4)

print(f'You earned {answer} dollars this week.')


# A student can be enrolled to a class only if the class is not full
#  and the class schedule does not conflict with her current schedule.

class_is_not_full = True
doesnt_conflict_with_current_schedule = True

enroll_in_class = class_is_not_full and doesnt_conflict_with_current_schedule

# A product offer can be applied only if people buys more than 2 items, and
#  the offer has not expired. Premium members do not need to buy a specific
#  amount of products.

bought_more_than_2_items = True
offer_has_not_expired = True
is_premium_member = True

product_offered = (bought_more_than_2_items or is_premium_member) and offer_has_not_expired


# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

password_at_least_5_chars = len(password) >= 5
username_less_than_20_chars = len(username) < 20
pass_does_not_equal_username = password != username
pass_and_username_not_end_with_whitespace = (password[0] != ' ' and password[-1] != ' ') and (username[0] != ' ' and username[-1] != ' ')

