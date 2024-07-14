import random


class Questionaire:
    def __init__(self, title: str, noQuestions: int, questions: dict = {}):
        self.title = title
        self.noQuestions = noQuestions
        self.questions = questions

    def setQnA(self):
        questionsAnswers = {}
        for i in range(self.noQuestions):
            q = input(f"Enter question {i+1}: ")
            a = input("Correct answer: ").lower()
            fa = input("Incorrect answer: ").lower()
            order = random.choice([True, False])
            if order:
                questionsAnswers[q] = {True: a, False: fa}
            else:
                questionsAnswers[q] = {False: fa, True: a}
        self.questions = questionsAnswers

    def p(self):
        scoreCount = 0
        print(f"--- {self.title} ---")
        i = 0
        for question, answers in self.questions.items():
            print(f"Question {i+1}: {question}")
            for _, answer in answers.items():
                print(f"Answer: {answer}")

            userAnswer = input("Your answer: ").lower()
            correctAnswer = answers[True]
            if userAnswer == correctAnswer:
                print("Correct!")
                scoreCount += 1
            else:
                print(f"Wrong! The correct answer is: {correctAnswer}")
            i += 1
        print(f"Final score: {scoreCount}")
        print(f"You scored {scoreCount // self.noQuestions * 100}%")


def main():
    title = input("Enter title: ")
    noQ = int(input("How many questions do you have? "))
    quiz = Questionaire(title, noQ)
    quiz.setQnA()
    quiz.p()


if __name__ == "__main__":
    main()
