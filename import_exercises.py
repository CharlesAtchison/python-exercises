#!/usr/bin/env python
# coding: utf-8

from function_exercises import is_vowel
from function_exercises import calculate_tip
from function_exercises import get_letter_grade as glg

print(glg(99))


# ### Read about and use the itertools module from the python standard library to help you solve the following problems:
# 
# * How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# * How many different combinations are there of 2 letters from "abcd"?
# * How many different permutations are there of 2 letters from "abcd"?

from itertools import product, permutations, combinations

print(list(product(['a', 'b', 'c'], [1, 2, 3])))
print(list(combinations(['a', 'b', 'c', 'd'], 2)))
print(list(permutations(['a', 'b', 'c', 'd'], 2)))


# ### Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# * Total number of users
# * Number of active users
# * Number of inactive users
# * Grand total of balances for all users
# * Average balance per user
# * User with the lowest balance
# * User with the highest balance
# * Most common favorite fruit
# * Least most common favorite fruit
# * Total number of unread messages for all users
from json import load, dumps

json_tup_of_dicts = load(open('./codeup-data-science/python-exercises/profiles.json'))    


total_number_of_active_users = 0
total_number_of_inactive_users = 0
grand_total_balance = 0
total_users = 0
user_with_lowest_balance = [[], 0]
user_with_highest_balance = [[], 0]
fruit_counts = dict()
total_unread_messages = 0



for each_person in json_tup_of_dicts:
    # Counts total users
    total_users += 1
    
    # Counts each active user
    if each_person['isActive']:
        total_number_of_active_users += 1
    # Counts each inactive user
    if not each_person['isActive']:
        total_number_of_inactive_users += 1
        
    # Formats balance to float to compare
    balance = float(each_person['balance'].replace('$', '').replace(',', ''))
    
    # On-going tally of total balance
    grand_total_balance += balance
    
    # Checks for users with highest balance
    if balance >= user_with_highest_balance[1]:
        if balance == user_with_highest_balance[1]:
            user_with_highest_balance[0].append(each_person['name'])
        else:
            user_with_highest_balance[0] = [each_person['name']]
            user_with_highest_balance[1] = balance
    
    # Checks for users with lowest balance
    if balance <= user_with_lowest_balance[1] or user_with_lowest_balance[1] == 0 :
        if balance == user_with_lowest_balance[1]:
            user_with_lowest_balance[0].append(each_person['name'])
        else:
            user_with_lowest_balance[0] = [each_person['name']]
            user_with_lowest_balance[1] = balance
    # On-going dict tally for fruits
    fav_fruit = each_person['favoriteFruit']
    if fav_fruit not in fruit_counts.keys():
        fruit_counts[fav_fruit] = 1
    else:
        fruit_counts[fav_fruit] += 1
    
    # On-going count of unread messages as an int
    total_unread_messages += int(each_person['greeting'].split('have ')[-1].split(' ')[0])
    
average_balance_per_user = grand_total_balance/total_users

print(f'The total number of users: {total_users}')
print(f'The number of active users: {total_number_of_active_users}')
print(f'The number of inactive users: {total_number_of_inactive_users}')
print(f'Grand total of balances for all users: ${grand_total_balance}')
print(f'Average balance per user: ${average_balance_per_user:0.2f}')
print(f'User with lowest balance: {user_with_lowest_balance[0][0]}')
print(f'User with highest balance: {user_with_highest_balance[0][0]}')
print(f'Most common favorite fruit: {max(fruit_counts)}')
print(f'Least common favorite fruit: {min(fruit_counts)}')
print(f'Total number of unread messages for all users: {total_unread_messages}')

