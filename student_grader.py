class Student:
    STUDENT_NAME = ""
    ACADEMIC_YEAR = 0
    TEST_1 = 0
    TEST_2 = 0
    COURSE_WORK = 0
    COURSE_WORK_AVERAGE = (max(TEST_1,TEST_2) + COURSE_WORK)/2
    FINAL_COURSE_WORK = (40/100)*COURSE_WORK_AVERAGE
    FINAL_EXAM = 0
    EXAM_CONTRIBUTION = (60/100)*FINAL_EXAM
    FINAL_MARK =  FINAL_COURSE_WORK+EXAM_CONTRIBUTION


    def capture(value):
        user_input = input(value)
        return user_input
    

    def validate_string(string):
        if string.split().is_digit():
            print("This is not a string")
        else:
            print("This is a string")



