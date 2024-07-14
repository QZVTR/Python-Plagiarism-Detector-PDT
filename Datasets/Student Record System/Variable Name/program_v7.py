class TeacherRecord:
    def __init__(self):
        self.teachers = {}

    def add_student(self, n, rollNo):
        self.teachers[rollNo] = n

    def remove_student(self, x):
        if x in self.teachers:
            del self.teachers[x]

    def search_student(self, abcdef):
        return self.teachers.get(abcdef)


def main():
    teacherRecords = TeacherRecord()
    teacherRecords.add_student("John", 101)
    print(teacherRecords.search_student(101))


if __name__ == "__main__":
    main()
