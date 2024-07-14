import random


class Questionaire:
    def __init__(self, title: str, noQ: int, questions: dict = {}):
        self.title = title
        self.noQ = noQ
        self.questions = questions

    def setQnA(self):
        qAnswers = {}
        for i in range(self.noQ):
            q = input(f"Enter question {i+1}: ")
            a = input("Correct answer: ").lower()
            fa = input("Incorrect answer: ").lower()
            order = random.choice([True, False])
            if order:
                qAnswers[q] = {True: a, False: fa}
            else:
                qAnswers[q] = {False: fa, True: a}
        self.questions = qAnswers

    def p(self):
        score = 0
        print(f"--- {self.title} ---")
        i = 0
        for q, answers in self.questions.items():
            print(f"Question {i+1}: {q}")
            for _, answer in answers.items():
                print(f"Answer: {answer}")

            userAnswer = input("Your answer: ").lower()
            correctAnswer = answers[True]
            if userAnswer == correctAnswer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correctAnswer}")
            i += 1
        print(f"Final score: {score}")
        print(f"You scored {score // self.noQ * 100}%")


def minor():
    title = input("Enter title: ")
    noQ = int(input("How many questions do you have? "))
    quiz = Questionaire(title, noQ)
    quiz.setQnA()
    quiz.p()


if __name__ == "__main__":
    minor()
