import random


class Quiz:
    def __init__(self, title: str, noQuestions: int, questions: dict = {}):
        self.noQuestions = noQuestions
        self.questions = questions
        self.title = title

    def setQuestionsAndAnswers(self):
        questionsAnswers = {}
        for i in range(self.noQuestions):
            fa = input("Incorrect answer: ").lower()
            q = input(f"Enter question {i+1}: ")
            a = input("Correct answer: ").lower()

            order = random.choice([True, False])
            if order:
                questionsAnswers[q] = {True: a, False: fa}
            else:
                questionsAnswers[q] = {False: fa, True: a}
        self.questions = questionsAnswers

    def play(self):
        i = 0
        scoreCount = 0
        print(f"--- {self.title} ---")

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

        print(f"You scored {scoreCount // self.noQuestions * 100}%")
        print(f"Final score: {scoreCount}")


def main():
    noQ = int(input("How many questions do you have? "))
    title = input("Enter title: ")
    quiz = Quiz(title, noQ)
    quiz.setQuestionsAndAnswers()
    quiz.play()


if __name__ == "__main__":
    main()
