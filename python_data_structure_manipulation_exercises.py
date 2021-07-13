students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# How many students are there? -- 14
number_of_students = len(students)

# How many students prefer light coffee? For each type of coffee roast? -- 3 / [(5, 'dark'), (6, 'medium'), (3, 'light')]
light_coffee = len([stud for stud in students if stud['coffee_preference'] == 'light'])

each_type_of_roast = [([each_student['coffee_preference'] 
for each_student in students].count(chr),chr)
 for chr in set([each_student['coffee_preference'] 
 for each_student in students])]

# How many types of each pet are there? -- [(4, 'horse'), (3, 'dog'), (11, 'cat')]         
numb_types_of_pets = [([each_pet['species'] for each_student in students for each_pet in each_student['pets']].count(chr),chr)
 for chr in set([each_pet['species'] for each_student in students for each_pet in each_student['pets']])]        


# How many grades does each student have? Do they all have the same number of grades? -- 4 and yes
number_of_grades = [len(each_student['grades']) for each_student in students]

# What is each student's grade average? -- [78.5, 83.5, 73.25, 78.5, 81.5, 80.75, 84.5, 88.75, 88.75, 82.5, 81.5, 91.0, 79.0, 89.0]
average_grades = [(sum(each_student['grades']) / len(each_student['grades'])) for each_student in students]

# How many pets does each student have? - [1, 0, 1, 2, 3, 0, 1, 2, 2, 1, 2, 1, 1, 1]
numb_of_pets = [len(each_student['pets']) for each_student in students]

# How many students are in web development? data science? -- 7
numb_in_web_dev = len([each_student for each_student in students if each_student['course'] == 'web development'])

# What is the average number of pets for students in web development? -- 1.2857142857142858
avg_num_of_pets = sum([len(each_student['pets']) 
for each_student in students if each_student['course'] == 'web development'])/len(
    [len(each_student['pets']) for each_student in students
 if each_student['course'] == 'web development'])

# What is the average pet age for students in data science? - 5.444444444444445 years (if they have a pet)
avg_pet_age = sum([each_pet['age']
 for each_student in students 
 for each_pet in each_student['pets'] 
 if each_student['course'] =='data science'])/len(
     [each_pet['age'] for each_student in students 
     for each_pet in each_student['pets'] 
     if each_student['course'] =='data science'])

# What is most frequent coffee preference for data science students? -- Medium
data_science_coff_preff = max([([each_student['coffee_preference'] 
for each_student in students if each_student['course'] == 'data science'].count(chr),chr)
 for chr in set([each_student['coffee_preference'] 
 for each_student in students if each_student['course'] == 'data science'])])[1]

# What is the least frequent coffee preference for web development students? -- ['medium', 'dark']
least_frequet_coffee_pref = [each_count[1] for each_count in [([each_student['coffee_preference'] 
for each_student in students if each_student['course'] == 'web development'].count(chr),chr)
 for chr in set([each_student['coffee_preference'] 
 for each_student in students if each_student['course'] == 'web development'])] if each_count[0] == min([([each_student['coffee_preference'] 
for each_student in students if each_student['course'] == 'web development'].count(chr),chr)
 for chr in set([each_student['coffee_preference'] 
 for each_student in students if each_student['course'] == 'web development'])])[0]]

# What is the average grade for students with at least 2 pets? -- 83.8
avg_grade_2_pets = sum([sum(each_student['grades'])/len(each_student['grades'])
 for each_student in students if len(each_student['pets']) >= 2])/len(
     [sum(each_student['grades']) / len(each_student['grades']) 
     for each_student in students if len(each_student['pets']) >= 2])

# How many students have 3 pets? -- 1
num_of_students_with_3_pets = len([each_student 
for each_student in students 
if len(each_student['pets']) == 3])

# What is the average grade for students with 0 pets?  -- 82.125
avg_grade_0_pets = sum([sum(each_student['grades'])/len(
    each_student['grades']) for each_student in students 
    if len(each_student['pets']) == 0])/len([sum(each_student['grades'])/len(
        each_student['grades']) for each_student in students if len(each_student['pets'])  == 0])

# What is the average grade for web development students? data science students? 81.18 / 84.68
avg_grade_web_dev = sum([sum(each_student['grades'])/len(
    each_student['grades']) for each_student in students 
    if each_student['course'] == 'web development'])/len([sum(each_student['grades'])/len(
        each_student['grades']) for each_student in students 
        if each_student['course'] == 'web development'])
avg_grade_data_science= sum([sum(each_student['grades'])/len(
    each_student['grades']) for each_student in students 
    if each_student['course'] == 'data science'])/len(
        [sum(each_student['grades'])/len(
            each_student['grades']) for each_student in students
             if each_student['course'] == 'data science'])

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers? [99, 65]
grade_range = [max([grade for grades in [each_student['grades'] 
for each_student in students if each_student['coffee_preference'] == 'dark'] 
for grade in grades]), min([grade for grades in [each_student['grades'] 
for each_student in students if each_student['coffee_preference'] == 'dark'] 
for grade in grades])]

# What is the average number of pets for medium coffee drinkers? - 1.1666666666666667 pets
avg_num_of_pets_medium_coffee = sum([len(each_student['pets']) 
for each_student in students if each_student['coffee_preference'] == 'medium'])/ len([len(each_student['pets']) 
    for each_student in students if each_student['coffee_preference'] == 'medium'])

# What is the most common type of pet for web development students? -- horse
common_pet_type = max([([each_pet['species'] for each_student in students 
for each_pet in each_student['pets'] if each_student['course'] == 'web development'].count(chr),chr)
 for chr in set([each_pet['species'] for each_student in students 
 for each_pet in each_student['pets'] if each_student['course'] == 'web development'])])[1]

# What is the average name length? -- 13.642857142857142
name_list =  sum([len(each_student['student']) for each_student in students])/len(
    [len(each_student['student']) for each_student in students])


# What is the highest pet age for light coffee drinkers? - 8
highest_pet_age = max([each_pet['age'] for each_student in students 
for each_pet in each_student['pets'] 
if each_student['coffee_preference'] == 'light'])
