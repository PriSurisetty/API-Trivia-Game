from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

""" What this module does:
- Initializes an empty list, and creates a for loop to iterate though all the data in question_data
- Calls the 'Question' by creating a variable called 'new_question', passing in the parameters 'question_text'
and 'question_answer' which were previously created by getting ahold of the keys 'correct_answer'
and 'question'
- We then appended the new_question for all the data (question and answers) into our question_bank
- Then we finally pass 'new_question' as the q_list instance from the Quizbrain class and store this into
an variable 'quiz'
- 
"""