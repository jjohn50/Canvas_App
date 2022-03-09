from canvasapi import Canvas

# Canvas API URL
API_URL = ""
# Canvas API key 
API_KEY = ""

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#the stevens canvas urls contains the numbers for canvas 
course = canvas.get_course() 
print(course.name)
# print(type(canvas))

# users = course.get_users()

# This is how we print out multiple students within a class
# for user in users:
#     print(user)

# This is how we print out a single user -> ID number within parentheses
student1 = course.get_user()
print(student1) 

# user = canvas.get_user()
# # courses = user.get_courses()
# print(user.name) 