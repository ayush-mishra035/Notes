# Given a list of tuple with info(name,subject):
# List all unique course 
# List students enrolled in english
# create dictionary (studet, set of courses)

info = [
    ("Alice", "Maths"),
    ("Bob", "English"), 
    ("Alice", "English"),
    ("Charlie", "Maths"),
    ("Bob", "Maths")
]
unique_courses = set()

for tup in info :
    print(tup[0])  # name 
    print(tup[1])  # course
    unique_courses.add(tup[1])
print(unique_courses)
  
# list student enrolled in english

for name,course in info:
    if course == "English":
        print(name)

# create dictionary (student,set of courses)

dict = {}

for name,course in info :
    if(dict.get(name) == None):
        dict.update({name: set()})
    dict[name].add(course)

print(dict)

