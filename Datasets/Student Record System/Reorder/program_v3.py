class StudentRecord:
    def __init__(self):
        self.students = {}

    def search_student(self, roll_no):
        return self.students.get(roll_no)

    def remove_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]

    def add_student(self, name, roll_no):
        self.students[roll_no] = name


def main():
    student_record = StudentRecord()
    student_record.add_student("John", 101)
    print(student_record.search_student(101))


if __name__ == "__main__":
    main()
