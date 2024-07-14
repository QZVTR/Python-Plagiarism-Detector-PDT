import random


# Comment 1
class Quiz:
    def __init__(self, title: str, noQuestions: int, questions: dict = {}):
        self.title = title
        self.noQuestions = noQuestions
        self.questions = questions

    # Comment 2
    def setQuestionsAndAnswers(self):
        questionsAnswers = {}
        for i in range(self.noQuestions):
            q = input(f"Enter question {i+1}: ")
            a = input("Correct answer: ").lower()
            fa = input("Incorrect answer: ").lower()  # Comment 3
            order = random.choice([True, False])
            if order:
                questionsAnswers[q] = {True: a, False: fa}
            else:
                questionsAnswers[q] = {False: fa, True: a}
        self.questions = questionsAnswers

    def play(self):  # Comment 4
        scoreCount = 0
        print(f"--- {self.title} ---")
        i = 0
        for question, answers in self.questions.items():  # Comment 5
            print(f"Question {i+1}: {question}")
            for _, answer in answers.items():
                print(f"Answer: {answer}")  # Comment 6

            userAnswer = input("Your answer: ").lower()
            correctAnswer = answers[True]
            if userAnswer == correctAnswer:  # Comment 7
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
    quiz = Quiz(title, noQ)
    quiz.setQuestionsAndAnswers()  # Comment 9
    quiz.play()


if __name__ == "__main__":  # Comment 8
    main()
