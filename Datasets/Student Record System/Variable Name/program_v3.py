class TeacherRecord:
    def __init__(self):
        self.teachers = {}

    def add_student(self, name, roll_no):
        self.teachers[roll_no] = name

    def remove_student(self, roll_no):
        if roll_no in self.teachers:
            del self.teachers[roll_no]

    def search_student(self, roll_no):
        return self.teachers.get(roll_no)


def main():
    student_record = TeacherRecord()
    student_record.add_student("John", 101)
    print(student_record.search_student(101))


if __name__ == "__main__":
    main()
