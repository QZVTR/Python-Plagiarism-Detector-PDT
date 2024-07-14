def main():
    f = TeacherRecord()
    f.add_student("John", 101)
    print(f.search_student(101))


class TeacherRecord:
    def __init__(self):
        self.students = {}

    # Comment 1
    def add_student(self, name, roll_no):
        self.students[roll_no] = name

    def search_student(self, roll_no):
        return self.students.get(roll_no)

    # Comment 2
    def remove_student(self, roll_no):
        if roll_no in self.students:
            del self.students[roll_no]

    # Comment 3


# Comment 6
# Comment 4


# Comment 5

if __name__ == "__main__":
    main()
