from re import L
import tkinter                  
from tkinter.messagebox import showinfo   
from canvasapi import Canvas   
from datetime import datetime 
from tkinter import Tk,Label,Entry,Menu,TOP,Toplevel, Scrollbar,RIGHT, Y, Listbox, messagebox, LEFT, Button 

#Need to use the following commands to install canvas api:
# pip3 install canvasapi (website: https://pypi.org/project/canvasapi/)
# Need to pip3 install tkinter

# Canvas API URL
API_URL = ""
# Canvas API key 
API_KEY = ""  

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#the stevens canvas urls contains the numbers for canvas 
#The numbers for course can be found in the urls if you are teacher for a class: 
# Ex: https://sit.instructure.com/courses/54864/users

# Prints out the name of the course via course ID
def course_get_name(): # Course Search -> "Get Course Name" (done)
    course_id = canvas_course_ID.get()        
    course = canvas.get_course(course_id)   
    # print(course.name)  
    return messagebox.showinfo('Course Name: ', f'{course.name}')    
    # print(type(canvas))
# Needs to pass course id for this  
# course_get_name()      

# Provides list of students within provided course
# This is how we print out ALL participants within a class (Teacher/TA too.)
# Prints out CANVAS ID, not STEVENS (8-digit) ID
def list_of_users():    # Course Search -> "List All Users in Course" (done)
    w = Toplevel(windw)   
    w.title("List of All Users")  
    w.configure(background="linen")
    sbar = Scrollbar(w)      
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=45,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get()  
    course= canvas.get_course(course_id)  
    users = course.get_users()
    count = 0 
    for user in users:
      #   print(user)
      Lb1.insert(count,user)  
      count+=1     
    Lb1.pack()    
    sbar.config(command=Lb1.yview)
# list_of_users()

# This is how we print out a single user -> ID number within parentheses
# The user id is not the Stevens ID rather it CANVAS ID 
def single_user_in_class(): # Student Search => Find Student in Course (done)
    course_id = canvas_course_ID.get()        
    student_id = canvas_student_ID.get()  
    course= canvas.get_course(course_id)  
    student1 = course.get_user(student_id)
    return messagebox.showinfo('Student Name: ', f'{student1}')

# single_user_in_class(,)

# course = canvas.get_course() 
#allows you to update the course name in real time
def update_course_name(): #   Course Setting ->   Update Course Name (Done) 
    #Window Setup
    w3 = Toplevel(windw)
    w3.title("Update Course Name")
    w3.configure(background="linen")

    #Label and Entry Boxes
    update_label = Label(w3, text="Please Enter New Name: ", background="linen")
    update_label.pack()
    update_entry = Entry(w3, bd=5, width=40)
    update_entry.pack()

    course_id = canvas_course_ID.get()    
    course= canvas.get_course(course_id) 

    #Button Functionality
    def update_course_button():   
        # course.update(course={'name': update_entry.get()})
        name = update_entry.get()       
        return messagebox.showinfo('New Name:            ', f'{name}')

    #Button
    b3 = Button(w3, text="Update Name", command=update_course_button)
    b3.pack()
    
    #this system work only if you have admin privileges  

    # print(course.name)  
# update_course_name() 

#This will give you indiviaul who are the following: teacher, ta, designer, etc
# Can act as a filter for user to specify which people they're looking for
def list_teacher_ta_etc(): # Course Settings -> "Find Personnel in Course" (done)
    w = Toplevel(windw)   
    w.title("List of Teacher/s and TA/s")  
    w.configure(background="linen")
    sbar = Scrollbar(w)       
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id) 
    type_list = ['teacher', 'ta'] 
    fac = course.get_users(enrollment_type=type_list)
    count = 0 
    for i in fac: 
        # print(i)
        Lb1.insert(count,i)
    Lb1.pack()      
    sbar.config(command=Lb1.yview)        
    
# list_teacher_ta_etc()       

#Will print the total amount of student in class -> Student test of get_user
def list_students():   #Course Search -> "List all students in a course" (done)
    w = Toplevel(windw)        
    w.title("List of Students")    
    w.configure(background="linen")
    sbar = Scrollbar(w)       
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id) 
    count = 0 
    list_student = ['student'] 
    student = course.get_users(enrollment_type=list_student)
    for g in student:   
        # print(g)
        Lb1.insert(count,g)
        count+=1
    Lb1.pack()      
    sbar.config(command=Lb1.yview)    
    # print("Total amount of students in class: " + str(count))
# list_students()

#This will print out a list of all the classes the user is taking
#PROBLEM: Requires specific permissions to work properly, protects student privacy
def list_of_user_classes(): # Student Account -> "List of Student's Classes" (done)
    a = 0 
    # w = Toplevel(windw)        
    # w.title("List of Classes")    
    # w.configure(background="linen")  
    # sbar = Scrollbar(w)       
    # sbar.pack(side=RIGHT,fill=Y)   
    # Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    # course_id = canvas_course_ID.get() 
    # student_id = canvas_student_ID.get()
    # user = canvas.get_user(student_id)
    # # print(user)
    # classes = user.get_courses()
    # count = 0   
    # for class_1 in classes:  
    #     # print(i)  
    #     Lb1.insert(count,class_1)   
    #     count+=1
    # Lb1.pack()         
    # sbar.config(command=Lb1.yview) 
    # course = canvas.get_course(course_id) 
    # print(course.name)
# list_of_user_classes()

#The user id is unique to canvas and easiest way to get is getting all users from class and find the indiviual you want to look at
def search_student():   # Student Search -> "Find Student by ID"  (done)
   student_id = canvas_student_ID.get()  
   user = canvas.get_user(student_id)     
   #print(student_id) 
   return messagebox.showinfo('Student ID: ', f'{user}')
# search_student()  

#This will provide a list of students who are teachers and students who are active and invited to class
def active_students(): #Course Search -> "Find Active Students in a Course" (done)
    w = Toplevel(windw)        
    w.title("List of Active Students")         
    w.configure(background="linen")
    sbar = Scrollbar(w)           
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id) 
    users_class = course.get_users(enrollment_type=['student'],enrollment_state=['active', 'invited'])     
    count = 0 
    for user1 in users_class:                  
        # print(u1)  
        Lb1.insert(count,user1)
        count+=1
    Lb1.pack()      
    sbar.config(command=Lb1.yview)
# active_students() 

#--------------------------------------------------------------------------------------------------------------------------------------------------

#This will update the course start and end dates: (done)
def change_start_end_of_course_1(): # "Change Course Start/End Time (Date/Time)"
   #Window Setup
   w1 = Toplevel(windw)
   w1.title("Change Course Start/End Time")
   w1.configure(background="linen")  

   #Starting Year
   starting_year_label = Label(w1, text="Please Enter Starting Year", background="linen", justify=LEFT)
   starting_year_label.pack()
   starting_year_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   starting_year_entry.pack()
   starting_year = starting_year_entry.get()

   #Ending Year
   ending_year_label = Label(w1, text="Please Enter Ending Year", background="linen", justify=LEFT)
   ending_year_label.pack()
   ending_year_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   ending_year_entry.pack()
   ending_year = ending_year_entry.get()

   #Starting Month
   starting_month_label = Label(w1, text="Please Enter Starting Month", background="linen", justify=LEFT)
   starting_month_label.pack()
   starting_month_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   starting_month_entry.pack()
   starting_month = starting_month_entry.get()

   #Ending Month
   ending_month_label = Label(w1, text="Please Enter Ending Month", background="linen", justify=LEFT)
   ending_month_label.pack()
   ending_month_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   ending_month_entry.pack()
   ending_month = ending_month_entry.get()

   #Starting Date
   starting_date_label = Label(w1, text="Please Enter Starting Date", background="linen", justify=LEFT)
   starting_date_label.pack()
   starting_date_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   starting_date_entry.pack()
   starting_date = starting_date_entry.get()

   #Ending Date 
   ending_date_label = Label(w1, text="Please Enter Ending Date", background="linen", justify=LEFT)
   ending_date_label.pack()
   ending_date_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)  
   ending_date_entry.pack()  
   ending_date = ending_date_entry.get()

   #Starting Hour
   starting_hour_label = Label(w1, text="Please Enter Starting Hour (24:00 Time)", background="linen", justify=LEFT)
   starting_hour_label.pack()
   starting_hour_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   starting_hour_entry.pack()
   starting_hour = starting_hour_entry.get()   

   #Ending Hour
   ending_hour_label = Label(w1, text="Please Enter Ending Hour (24:00 Time)", background="linen", justify=LEFT)
   ending_hour_label.pack()
   ending_hour_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)
   ending_hour_entry.pack()
   ending_hour = ending_hour_entry.get()

   #Starting Minute
   starting_minute_label = Label(w1, text="Please Enter Starting Minute", background="linen", justify=LEFT)
   starting_minute_label.pack()
   starting_minute_entry = Entry(w1, bd=5, width = 40, justify=RIGHT) 
   starting_minute_entry.pack()
   starting_minute = starting_minute_entry.get()

   #Ending Minute 
   ending_minute_label = Label(w1, text="Please Enter Ending Minute", background="linen", justify=LEFT)
   ending_minute_label.pack()      
   ending_minute_entry = Entry(w1, bd=5, width = 40, justify=RIGHT)  
   ending_minute_entry.pack()
   ending_minute = ending_minute_entry.get()

   def change_course():  
      change_course_start_end = canvas.get_course(canvas_course_ID.get())
      #First way: Python Datetime Objects
      start =  datetime(starting_year, starting_month, starting_date, starting_hour, starting_minute)
      end = datetime(ending_year, ending_month, ending_date, ending_hour, ending_minute)
      change_course_start_end.update(
         change_course_start_end={
            'start_at': start,   
            'end_at': end
         }
      )
   
   #Button Functionality
   b1 = Button(w1, text="Change Course Start/End", command= change_course)
   b1.pack()

#------------------------------------------------------------------------------------------------------------------------------------------------
#Second method: ISO8601 format date string: (Done)    
def change_start_end_of_course_2(): # "Change Course Start/End Time (ISO Format)"    
    #Window Setup
   w2 = Toplevel(windw)  
   w2.title("Change Course Start/End Time")
   w2.configure(background="linen")  

   #Starting Year
   starting_year_label = Label(w2, text="Please Enter Starting Year", background="linen", justify=LEFT)
   starting_year_label.pack()
   starting_year_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   starting_year_entry.pack()
   starting_year = starting_year_entry.get()

   #Ending Year
   ending_year_label = Label(w2, text="Please Enter Ending Year", background="linen", justify=LEFT)
   ending_year_label.pack()
   ending_year_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   ending_year_entry.pack()
   ending_year = ending_year_entry.get()

   #Starting Month
   starting_month_label = Label(w2, text="Please Enter Starting Month", background="linen", justify=LEFT)
   starting_month_label.pack()
   starting_month_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   starting_month_entry.pack()
   starting_month = starting_month_entry.get()

   #Ending Month
   ending_month_label = Label(w2, text="Please Enter Ending Month", background="linen", justify=LEFT)
   ending_month_label.pack()
   ending_month_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   ending_month_entry.pack()
   ending_month = ending_month_entry.get()

   #Starting Date
   starting_date_label = Label(w2, text="Please Enter Starting Date", background="linen", justify=LEFT)
   starting_date_label.pack()
   starting_date_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   starting_date_entry.pack()
   starting_date = starting_date_entry.get()

   #Ending Date 
   ending_date_label = Label(w2, text="Please Enter Ending Date", background="linen", justify=LEFT)
   ending_date_label.pack()
   ending_date_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)  
   ending_date_entry.pack()  
   ending_date = ending_date_entry.get()

   #Starting Hour
   starting_hour_label = Label(w2, text="Please Enter Starting Hour (24:00 Time)", background="linen", justify=LEFT)
   starting_hour_label.pack()
   starting_hour_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   starting_hour_entry.pack()
   starting_hour = starting_hour_entry.get()   

   #Ending Hour
   ending_hour_label = Label(w2, text="Please Enter Ending Hour (24:00 Time)", background="linen", justify=LEFT)
   ending_hour_label.pack()
   ending_hour_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)
   ending_hour_entry.pack()
   ending_hour = ending_hour_entry.get()

   #Starting Minute
   starting_minute_label = Label(w2, text="Please Enter Starting Minute", background="linen", justify=LEFT)
   starting_minute_label.pack()
   starting_minute_entry = Entry(w2, bd=5, width = 40, justify=RIGHT) 
   starting_minute_entry.pack()
   starting_minute = starting_minute_entry.get()  

   #Ending Minute 
   ending_minute_label = Label(w2, text="Please Enter Ending Minute", background="linen", justify=LEFT)
   ending_minute_label.pack()      
   ending_minute_entry = Entry(w2, bd=5, width = 40, justify=RIGHT)  
   ending_minute_entry.pack()
   ending_minute = ending_minute_entry.get()       

   def change_course2():
      change_course_start_end = canvas.get_course(canvas_course_ID.get())
      start_sequence = str(starting_year) + "-" + str(starting_month) + "-" + str(starting_date) + "T" + str(starting_hour) + ":" + str(starting_minute) + "Z"
      end_sequence = str(ending_year) + "-" + str(ending_month) + "-" + str(ending_date) + "T" + str(ending_hour) + ":" + str(ending_minute) + "Z"
      change_course_start_end.update(
         change_course_start_end={
            'start_at': start_sequence,  
            'end_at': end_sequence
         }
      )

   b2 = Button(w2, text="Change Course Start/End", command= change_course2)
   b2.pack()            

#------------------------------------------------------------------------------------------------------------------------------------------------
#conclude a course (Can not test due to natural of how the API works on our end)
def conclude_course():  # Course Setting -> "End Course" (done)
    a = 0 
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id)
    # course.conclude()  
    return messagebox.showinfo('Ended Course: ', f'{course.name }')  
    # print(str(course_id) + " has been concluded")

#end a course (Can not test due to natural of how the API works on our end)
def delete_course():    # Course Setting -> "Delete Course" (done) 
    a =0 
    course_id = canvas_course_ID.get()         
    course = canvas.get_course(course_id)       
    # course.delete()
    return messagebox.showinfo('Deleted Course: ', f'{course.name }')  
    # print(str(courseid) + " has been deleted")

#Grab information about assignments on Canvas: (done)
def name_of_assignment():    # Assignment Creation -> "Get Assignment Name"  
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id)
    assignment_id = assignment_ID.get()    
    assignment1 = course.get_assignment(assignment_id)            
    return messagebox.showinfo('Assignment Name: ', f'{assignment1}')  
    # print("Here is the assignment for this course: ")
    # print(assignment1)       

#Grab name of all assignments on Canvas: (done)
def all_assignments():     # Assignment Creation -> "List All Assignments"     
    w = Toplevel(windw)        
    w.title("All of the assignments names:")    
    w.configure(background="linen")
    sbar = Scrollbar(w)       
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    count = 0 
    # print("Here are all of the assignments for this course: ")
    for assign in assignments:
        # print(assign)
        Lb1.insert(count,assign)
        count+=1
    Lb1.pack()               
    sbar.config(command=Lb1.yview)

def ungraded_assignment(): # Assignment Settings -> "List Ungraded Assignments" (done)
    w = Toplevel(windw)        
    w.title("All of the ungraded assignments names:")    
    w.configure(background="linen")
    sbar = Scrollbar(w)       
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get()    
    course = canvas.get_course(course_id)
    ungraded_assignements = course.get_assignments(bucket='ungraded')
    # print("Here are all of the assignments for this course: ")
    count = 0 
    for unassign in ungraded_assignements:
        # print(unassign)
        Lb1.insert(count,unassign)       
        count+=1  
    Lb1.pack()      
    sbar.config(command=Lb1.yview)        

#creates assignments: needs button and text entry for assign name (done)   
def creating_basic_assignment():   # Assignment Creation -> "Create Basic Assignments" 
   w4 = Toplevel(windw)
   w4.title("Create A Basic Assignment")
   w4.configure(background="linen")
   
   assignment_name_label = Label(w4, text="Please enter the Assignment's Name: ", background="linen")
   assignment_name_label.pack()
   assignment_name_entry = Entry(w4, bd=5, width=40)     
   assignment_name_entry.pack()
   #assignment_name = str(assignment_name_entry.get())

   def create_assignment():
      course_id = canvas_course_ID.get() 
      course = canvas.get_course(course_id)
      course.create_assignment({          
         'name': str(assignment_name_entry.get())      
      })
      return messagebox.showinfo(f'{"Assignment Created:           "}', str(assignment_name_entry.get()) + ' has been created')

   b4 = Button(w4, text="Create Assignment", command=create_assignment)
   b4.pack()  

#Done            
#create an advanced assignment with Mutiple submission types and possibly publish to canvas : (Hat and Justin will work on this)
def creating_adv_assignment():    # "Create Advanced Assignments"
    w5 = Toplevel(windw)
    w5.title("Create Advanced Assignment")
    w5.configure(background="linen")  

    #Assignment Name -> DONE
    assignment_name_label2 = Label(w5, text="Please Enter The Assignment Name:", background="linen", justify=LEFT)
    assignment_name_label2.pack()
    assignment_name_entry2 = Entry(w5, bd=5, width = 40, justify=RIGHT)
    assignment_name_entry2.pack()

    #Submission Types -> DONE
    submission_types_label = Label(w5, text="Please Enter Submission Types as one of the following (online_upload, online_text_entry)", background="linen", justify=LEFT)
    submission_types_label.pack()  
    submission_types_entry = Entry(w5, bd=5, width = 40, justify=RIGHT)
    submission_types_entry.pack()

    #Allowed Extensions -> WORKING
    allowed_extensions_label = Label(w5, text="Please Enter Extension Types as Follows (pdf doc text): ", background="linen", justify=LEFT)
    allowed_extensions_label.pack()  
    allowed_extensions_entry = Entry(w5, bd=5, width = 40, justify=RIGHT)
    allowed_extensions_entry.pack()

    #Notify of Update -> Done
    notify_update_label = Label(w5, text="Please Enter 'True' or 'False' for Update Notification Status", background="linen", justify=LEFT)
    notify_update_label.pack()
    notify_update_entry = Entry(w5, bd=5, width = 40, justify=RIGHT)
    notify_update_entry.pack()

    #Number of Points Possible -> DONE
    points_possible_label = Label(w5, text="Please Enter Number of Possible Points", background="linen", justify=LEFT)
    points_possible_label.pack()
    points_possible_entry = Entry(w5, bd=5, width = 40, justify=RIGHT)
    points_possible_entry.pack()

    #Due Date -> Done
    due_date_label = Label(w5, text="Please Enter Due Date as Follow(Month Date Year Hour:MinuteAM/PM)", background="linen", justify=LEFT)
    due_date_label.pack()
    due_date_entry = Entry(w5, bd=5, width = 40, justify=RIGHT)
    due_date_entry.pack() 

    #Description -> DONE
    description_label = Label(w5, text="Please Enter The Assignment Description:", background="linen", justify=LEFT)
    description_label.pack()
    description_entry = Entry(w5, bd=5, width = 40, justify=RIGHT)
    description_entry.pack()     

    def creating_adv_assignment():    # "Create Advanced Assignments" 
       course_id = canvas_course_ID.get() 
       course = canvas.get_course(course_id)  
       new_assignment1 = course.create_assignment({        
       'name': str(assignment_name_entry2.get()) ,            #String    
       'submission_types':  [str(submission_types_entry.get())], #List        (only takes one entry) 
       'allowed_extensions': [allowed_extensions_entry.get()],     #List   (can take mutiple entries)  
       'notify_of_update': bool(notify_update_entry.get()),      # boolean     
       'points_possible': int(points_possible_entry.get()),    #String 
       'due_at': datetime.strptime(due_date_entry.get(), '%b %d %Y %I:%M%p'),        
       'description': description_entry.get(),   #String     
       })   
       return messagebox.showinfo(f'{"Assignment Created:           "}', str(assignment_name_entry2.get()) + ' has been created')
      # print("Go to canvas to see your assignment you made: ")
    b10 = Button(w5, text="Create Assignment", command=creating_adv_assignment)
    b10.pack()        

#Updating/Editing Assignments: (done) needs name entry 
def updated_assignment():    # Assignment Setting -> "Update Assignment Elements"
    w7 = Toplevel(windw)
    w7.title("Update Assignment Name               ")
    w7.configure(background="linen")
    
    assignment_name_label = Label(w7, text="Please enter the new assignment Name: ", background="linen")
    assignment_name_label.pack()
    assignment_name_entry = Entry(w7, bd=5, width=40)     
    assignment_name_entry.pack()

    def update_assignment():
        course_id = canvas_course_ID.get()    
        course = canvas.get_course(course_id)        
        assignment_id = assignment_ID.get() 
        new_assignment1 = course.get_assignment(assignment_id)  
        updated_assignments = new_assignment1.edit(
            assignment={'name': str(assignment_name_entry.get()) #edit this value to change the name
            })         
        return messagebox.showinfo('Assignement Name Edited', f'{updated_assignments}')
    
    b5 = Button(w7, text="Update assignment name", command=update_assignment)
    b5.pack()
    # print(updated_assignments) 


#deleting assignements: you get the assignment id from url link from where the assignments are placed
def delete_assignment(): # Assignment Setting -> "Delete Assignment" (done) 
    #Look at the reference guide for more information 
    course_id = canvas_course_ID.get() 
    course = canvas.get_course(course_id) 
    assignment_id = assignment_ID.get() 
    assignment1 = course.get_assignment(assignment_id)
    assignment1.delete()      
    return messagebox.showinfo('Delete Assignment:          ', f'{"Assignment has been deleted!!       "}')
    # print("Assignment has been deleted: ")  


#giving students score for certain assignments: #needs a field for grade entry (done)
def score_student_work(): # "Get Student Scores on an Assignment"
    w6 = Toplevel(windw)
    w6.title("Score Student Work")  
    w6.configure(background="linen")
    
    assignment_name_label = Label(w6, text="Please enter the student's score: ", background="linen")
    assignment_name_label.pack()
    assignment_name_entry = Entry(w6, bd=5, width=40)     
    assignment_name_entry.pack()

    def score_student():
        course_id = canvas_course_ID.get() 
        course = canvas.get_course(course_id)
        assignment_id = assignment_ID.get() 
        assignment = course.get_assignment(assignment_id)
        student_id = canvas_student_ID
        submission = assignment.get_submission(student_id)  
        submission.edit(submission={"posted_grade": int(assignment_name_entry.get())})
    
    b4 = Button(w6, text="Submit student score:", command=score_student)
    b4.pack()  


# get list of student grades for certain assignments
def student_grade_list():    # Assignment Setting -> "List of Students' Grades" (done)
    w = Toplevel(windw)              
    w.title("List of Students' grades")        
    w.configure(background="linen")
    sbar = Scrollbar(w)       
    sbar.pack(side=RIGHT,fill=Y)   
    Lb1 = Listbox(w,height=35,width=55,yscrollcommand=sbar.set)  
    course_id = canvas_course_ID.get() 
    assignment_id = assignment_ID.get()
    course = canvas.get_course(course_id)
    assignment = course.get_assignment(assignment_id)
    submission = assignment.get_submissions()
    count = 0     
    for student in submission:
        # print(student)  
        Lb1.insert(count,student)
        count+=1
    Lb1.pack()       
    sbar.config(command=Lb1.yview)

#Deletes a student as long as student_id is given 
#This id is not the same as stevens id rather SIS ID
#DO NOT RUN THIS FUNCTION 
def delete_student():    # "Delete Student" 
    w8 = Toplevel(windw)
    w8.title("Delete Student")
    w8.configure(background="linen")
   
    assignment_name_label = Label(w8, text="Please enter the student's SIS ID to be deleted: ", background="linen")
    assignment_name_label.pack() 
    assignment_name_entry = Entry(w8, bd=5, width=40)     
    assignment_name_entry.pack()  

    def del_student():
        si_ID=assignment_name_entry.get()          
        user = canvas.get_user(si_ID)     
        # user.delete(si_ID)
        return messagebox.showinfo('Delete Student      :          ', f'{"Student has been deleted!!       "}')
           
    b6 = Button(w8, text="Delete Student", command=del_student)
    b6.pack()   

    def kill_window():  
        w8.destroy()   
  
    b7 = Button(w8, text="End Function", command=kill_window)
    b7.pack()
            
    # for i in range(num_of_students):
    #     si_ID = int(input("Enter student SIS ID: "))
    #     user = canvas.get_user(si_ID)     
    #     user.delete(si_ID) 
    #     print("User has been delete")  

# num_of_students = int(input("How many student do you want to add?: "))

#add mutiple users to a class: 
#DO NOT RUN THIS FUNCTION (done) 
def add_muti_user_to_course():  # Course Settings -> "Add Users to a Course"  
    w9 = Toplevel(windw)
    w9.title("Add Students to Course")
    w9.configure(background="linen")
   
    assignment_name_label = Label(w9, text="Please enter the student's SIS ID to be added: ", background="linen")
    assignment_name_label.pack() 
    assignment_name_entry = Entry(w9, bd=5, width=40)     
    assignment_name_entry.pack()  
    
    course = canvas_course_ID.get()  

    def add_student():
        si_ID=assignment_name_entry.get()          
        user = canvas.get_user(si_ID)     
        # print(user) 
        # course.enroll_user(user,enrollment=None)        
        return messagebox.showinfo('Added Student      :          ', f'{"Student has been added!!       "}')
           
    b8 = Button(w9, text="Add Student", command=add_student)
    b8.pack()   

    def kill_window():  
        w9.destroy()     
  
    b9 = Button(w9, text="End Function", command=kill_window)
    b9.pack()     

# num_students = int(input("How many student do you want to add?: "))

#======================================================== UI STUFF ===========================================================

#UI Window Setup
windw = Tk()    #Implementation for all the TK stuff
windw.title("Canvas Companion")  
windw.geometry("680x500")    #Sets window size  
windw.configure(background="linen")

#Main Title Code
title_label = Label(windw, text="Canvas Companion", font=("Impact", 56), background="linen", fg='OrangeRed2')   #Sets title for window?
title_label.pack(anchor='n')   

#Empty titles for Spacing
empty_entry0 = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry0.pack(anchor='nw')   
empty_entry0_5 = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry0_5.pack(anchor='nw')  


#Canvas Course ID Label and Text Box
title_entry = Label(windw, text="Please Enter Canvas Course ID: ", background="linen", font=('Calibri 14 underline'), justify=LEFT)  #Sets size of label?
title_entry.pack(anchor='nw')    
empty_entry = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry.pack(anchor='nw')   
#Course ID Text Entry Code
canvas_course_ID = Entry(windw, bd = 5, width = 80) #textvariable=course_ID
canvas_course_ID.pack(side = TOP)


#More Empty Titles for Spacing
empty_entry2 = Label(windw, text=" ", font=("Times New Roman", 18))  #Sets size of label?
empty_entry2.pack(anchor='nw')   
empty_entry2_5 = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry2_5.pack(anchor='nw')   


#Canvas Student ID Label and Text Box
title_entry2 = Label(windw, text="Please Enter Canvas Student ID: ", background="linen", font=('Calibri 14 underline'), justify=LEFT)  #Sets size of label?
title_entry2.pack(anchor='nw')   
empty_entry3 = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry3.pack(anchor='nw')   
#Canvas Student ID Text Entry
canvas_student_ID = Entry(windw, bd = 5, width = 80)    #textvariable=student_ID
canvas_student_ID.pack(side = TOP)


#More Empty Titles for Spacing
empty_entry4 = Label(windw, text=" ", font=("Times New Roman", 18))  #Sets size of label?
empty_entry4.pack(anchor='nw')   
empty_entry4_5 = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry4_5.pack(anchor='nw')


#Canvas Student ID Label and Text Box
title_entry3 = Label(windw, text="Please Enter Assignment ID: ", background="linen", font=('Calibri 14 underline'), justify=LEFT)  #Sets size of label?
title_entry3.pack(anchor='nw')   
empty_entry5 = Label(windw, text=" ", font=("Times New Roman", 6))  #Sets size of label?
empty_entry5.pack(anchor='nw')   
#Canvas Student ID Text Entry
assignment_ID = Entry(windw, bd = 5, width = 80)    #textvariable=assignment_ID
assignment_ID.pack(side = TOP)


#================================== MENUBAR CODE =======================================


#Menu Bar Setup   
menubar = Menu(windw) 

#Student Search Tab
student_search_menu = Menu(menubar, tearoff=0, background='medium slate blue') 
student_search_menu.add_command(label="Find Student In Course", command=single_user_in_class)
student_search_menu.add_command(label="Find Student By ID", command=search_student)

#Student Grade Tab 
#student_grade_menu = Menu(menubar, tearoff=0, background='blue')
#student_grade_menu.add_command(label="Get Student Assignment Score", command=score_student_work)

#Student Account Tab 
student_account_menu = Menu(menubar, tearoff=0, background='turquoise')
student_account_menu.add_command(label="List of Student's Courses", command=list_of_user_classes)
student_account_menu.add_separator()
student_account_menu.add_command(label="Delete Students Accounts", command=delete_student)

#Course Search Tab   
course_search_menu = Menu(menubar, tearoff=0, background='pale green')  
course_search_menu.add_command(label="Get Course Name", command=course_get_name)
course_search_menu.add_command(label="List All Users in Course", command=list_of_users)
course_search_menu.add_command(label="List All Students in Course", command=list_students)
course_search_menu.add_command(label="List Personnel in Course", command=list_teacher_ta_etc)
course_search_menu.add_command(label="Find Active Students in Course", command=active_students)  

#Course Setting Tab 
course_setting_menu = Menu(menubar, tearoff=0, background='gold')
course_setting_menu.add_command(label="Change Course Start/End Date (Date/Time Format)", command=change_start_end_of_course_1)
course_setting_menu.add_command(label="Change Course Start/End Date (ISO Format)", command=change_start_end_of_course_2)
course_setting_menu.add_command(label="End Course", command=conclude_course)
course_setting_menu.add_command(label="Update Course Name", command=update_course_name)
course_setting_menu.add_command(label="Add Users to a Course", command=add_muti_user_to_course)
course_setting_menu.add_separator()
course_setting_menu.add_command(label="Delete Course", command=delete_course)   

#Assignment Creation Tab 
assignment_creation_menu = Menu(menubar, tearoff=0, background='dark salmon')
assignment_creation_menu.add_command(label="Get Assignment Name", command=name_of_assignment)
assignment_creation_menu.add_command(label="List All Assignments", command=all_assignments)
assignment_creation_menu.add_command(label="Create Basic Assignments", command=creating_basic_assignment)
assignment_creation_menu.add_command(label="Create Advanced Assignments", command=creating_adv_assignment)

#Assignment Setting Menu   
assignment_setting_menu = Menu(menubar, tearoff=0, background='indian red')  
assignment_setting_menu.add_command(label="Update Assignement Elements", command=updated_assignment)
assignment_setting_menu.add_command(label="List Ungraded Assignments", command=ungraded_assignment)
assignment_setting_menu.add_command(label="Get Students Scores on an Assignment", command=score_student_work)
assignment_setting_menu.add_command(label="List of Students Grades", command=student_grade_list)
assignment_setting_menu.add_separator()
assignment_setting_menu.add_command(label="Delete Assignment", command=delete_assignment)

#Exit Tab 
exit_menu = Menu(menubar, tearoff=0, background='bisque2')
exit_menu.add_command(label="Exit", command=windw.quit)

#Creates the section and dropdown menu
menubar.add_cascade(label="Student Search", menu=student_search_menu)
#menubar.add_cascade(label="Student Grades", menu=student_grade_menu)
menubar.add_cascade(label="Student Accounts", menu=student_account_menu)
menubar.add_cascade(label="Course Search", menu=course_search_menu) 
menubar.add_cascade(label="Course Settings", menu=course_setting_menu)
menubar.add_cascade(label="Assignment Creation", menu=assignment_creation_menu)
menubar.add_cascade(label="Assignment Settings", menu=assignment_setting_menu)
menubar.add_cascade(label="Exit", menu=exit_menu)

windw.config(menu=menubar)

#Runs the UI until closed
windw.mainloop()    #Runs the window until closed by user