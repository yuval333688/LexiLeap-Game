from Lesson import Lesson

# Create the Lesson only once
lesson_instance = Lesson()

def getTestByNum_outside(test_num: int):
    return lesson_instance.getTestByNum(test_num)
