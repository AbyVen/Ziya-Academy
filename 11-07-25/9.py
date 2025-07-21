class Student:
    def __init__(self, marks):
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return 'A'
        elif avg >= 60:
            return 'B'
        else:
            return 'C'


marks_input = input("Enter marks separated by space: ")
marks = list(map(int, marks_input.split()))


s = Student(marks)


print("Average:", s.average())
print("Grade:", s.grade())
