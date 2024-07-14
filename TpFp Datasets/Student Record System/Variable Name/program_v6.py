class Tcord:
    def __init__(self):
        self.abcdefg = {}

    # Comment
    def addent1233(self, n, rollNumber):
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


def ain():
    cord = Tcord()
    cord.addent("Jon", 101)
    print(cord.searent(101))


if __name__ == "__main__":
    ain()
