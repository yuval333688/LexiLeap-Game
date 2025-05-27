from Question import Question
import unittest

FINALS_QUESTION_SESSIONS = 20

class Test:
        _test_counter = 0  # Class variable to ensure unique test codes
        def __init__(self,words):
            self.test_code=Test._test_counter
            Test._test_counter+=1
            self.questions = [Question(word) for word in words]
            self.total_score = 0

        def conduct_test(self):
            print("Starting the test...\n")
            for i, question in enumerate(self.questions, start=1):
                ##print(f"Question {i}:")
                question.ask_question()
                question.evaluate()
                self.total_score += question.point
                print(f"Score for Question {i}: {question.point:.2f}\n")

        def get_results(self):
            correct_answers = sum(q.right for q in self.questions)
            return{
            "total_score": self.total_score,
            "average_score": self.total_score / 20,
            "correct_answers": correct_answers,
            "wrong_answers": 20 - correct_answers,
        }
        def print_summary(self):
            results = self.get_results()
            print("Test Summary:")
            print(f"Total Score: {results['total_score']:.2f}")
            print(f"Average Score: {results['average_score']:.2f}")
            print(f"Correct Answers: {results['correct_answers']}")
            print(f"Wrong Answers: {results['wrong_answers']}")
