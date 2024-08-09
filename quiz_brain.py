import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


"""
What this module does:

######################################### CLASS 'QuizBrain' #######################################

- Creates a class called QuizBrain with methods: 
    'still_has_questions', 
    'next_question',
    'check_answer'
- It initiates variables 'question_number' and 'score' to start at 0 since it will be incremented in the other 
methods. 
- It sets the parameter 'q_list', which is expected to be a list, to the instance variable 
self.question_list
- This means that in main.py, the QuizBrain class will store the provided list of 
questions in its question_list attribute for use throughout its methods.
- Variable 'self.current_question' is initialized to 'None' because it is meant to hold a Question object, not an 
integer. It will be assigned an actual question from self.question_list when next_question is called.

################################### METHOD 'still_has_questions' ###################################

- Method called 'still_has_questions' will return a boolean value which will determine if the data still has
questions to provide. 

################################### METHOD 'next_question' #########################################
- Method called 'next_question' will create a variable called current_question which is set to the question number
from the question list. It will gradually increment the value. 
- Creates a local variable 'q_text' (which is why it doesn't have '.self') and it uses html.unescape to get rid of 
the HTML entities in the question text.

################################### METHOD 'check_answer' #########################################
- Method called 'check_answer' gets a hold of the current question's answer, and stores it into a variable called
'correct_answer'. It then checks if the user's answer matches the correct answer; If so, it will increase the score
by 1. Returns a boolean value overall.

"""
