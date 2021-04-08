import statistics

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade


def basic_stats(students):
    grades_arr = []
    for score in students:
        grades_arr.append(score.get_grade())

    mean = statistics.mean(grades_arr)
    median = statistics.median(grades_arr)
    mode = statistics.mode(grades_arr)

    tuples = (mean, median, mode)
    return tuples


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]

result = basic_stats(student_list)
print(result)

