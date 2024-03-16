import psycopg2
from psycopg2 import sql

#connect
#input in the info
connection = psycopg2.connect(dbname="dbName", user="username", password="passWord", host="host", port="port")
#connection = psycopg2.connect(dbname="a3", user="postgres", password="333", host="localhost", port="5432")
cursor = connection.cursor()

#create the table, if it is not created already
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
	student_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	enrollment_date DATE
);""")
connection.commit()


#only insert if there is no data in the table already
cursor.execute("SELECT COUNT(*) FROM students")
if (cursor.fetchone()[0] == 0):
    cursor.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    """)
    connection.commit()

#get all the students
def getAllStudents():
    cursor.execute("SELECT * FROM students;")

    print("Selecting all students:")
    for student in cursor.fetchall():
        print("Student ID:", student[0])
        print("First name:", student[1])
        print("Last name:", student[2])
        print("Email:", student[3])
        print("Enrollment date:", student[4])
        print("")

#add a student into the table, with the provided data
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES(%s, %s, %s, %s);", 
                   (first_name, last_name, email, enrollment_date))   
    connection.commit()

#update the student's email corresponding to their id
def updateStudentEmail(student_id, new_email):
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;",(new_email, student_id))
    connection.commit()

#delete the student using the student's id
def deleteStudent(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = {0};".format(student_id))
    connection.commit()



flag = True
while flag:

    print("\nType: \n 'get' to get all students \n 'add' to add a student \n 'update' to update an email \n 'delete' to remove a student \n 'end' to stop")
    choice = input("provide choice: ")
    match(choice):
        case "get":
            getAllStudents()
    
        case "add":
            first_name = input("input first name: ")
            last_name = input("input last name: ")
            email = input("input the email: ")
            enrollment_date = input("input the enrollment date (following format: yyyy-mm-dd): ")
            addStudent(first_name, last_name, email, enrollment_date)
            
        
        case "update":
            student_id = input("input student's id to update: ")
            new_email = input("input the new email: ")
            updateStudentEmail(student_id, new_email)
        
        case "delete":
            student_id = input("input student id to remove: ")
            deleteStudent(student_id)

        case "end":
            flag = False

    print("")




cursor.close()
connection.close()