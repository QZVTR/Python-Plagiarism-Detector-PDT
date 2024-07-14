class Tcord:
    def __init__(self):
        self.abcdefg = {}

    # Comment
    def addent(self, n, rollNumber):
        self.abcdefg[rollNumber] = n

    def remudent(self, x):
        if x in self.abcdefg:  # Comment
            del self.abcdefg[x]

    def searent(self, ro):
        return self.abcdefg.get(ro)  # Comment


"""
1
2
3
4
5
"""

"""
1
23
45678
8
76
"""


def main():
    student_record = Tcord()
    student_record.addent("John", 101)
    print(student_record.searent(101))


if __name__ == "__main__":
    main()
