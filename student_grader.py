
class Student:

    STUDENT_NAME = ""
    STUDENT_NAME_RQST = "Please enter Student Name"
    ACADEMIC_YEAR = 0
    TEST_1 = 0
    TEST_2 = 0
    COURSE_WORK = 0
    COURSE_WORK_AVERAGE = (max(TEST_1,TEST_2) + COURSE_WORK)/2
    FINAL_COURSE_WORK = (40/100)*COURSE_WORK_AVERAGE
    FINAL_EXAM = 0
    EXAM_CONTRIBUTION = (60/100)*FINAL_EXAM
    FINAL_MARK =  FINAL_COURSE_WORK+EXAM_CONTRIBUTION


    def capture(self, string):

        print("\nPlease enter "+string+"\n")
        input_d = input(string)
        
        return input_d
    

def validate(string):

    if string.isdigit():
        result = "Number"
    else:
        result = "String"
        
    return result


def capture_student():

    student_1 = Student()
    input_name = student_1.capture("Student name: ")
    validation_result = validate(input_name)

    if validation_result == "String":
        print(input_name+" "+"captured successfully")
        captured_name = input_name
    else:
        print("ERROR 1:"+input_name+" "+"is not a string\n")
        print("Please try Again")
        captured_name = ""
        capture_student()

    return captured_name
        

def capture_ay():

    student_1 = Student()
    input_year = student_1.capture("Academic Year: ")
    validation_result = validate(input_year)

    if validation_result == "String":
        print("ERROR 2:"+input_year+" "+"is not a year\n")
        print("Please try Again")
        student_year = ""
        capture_ay()
    else:
        print(input_year+" "+"captured successfully")
        student_year = input_year

    return student_year


def capture_test():

    student_1 = Student()
    student_name = student_1.capture("\nTest 1 Marks:")

    return student_name


def grade():

    student = capture_student()
    print("Student Name: "+student)

    academic_year = capture_ay()
    print("Academic Year: "+academic_year)


grade()
