from question_model import Question
from data import question_data,question_data2
from quiz_brain import QuizBrain

# import data to the question_model
# question_bank = []
# for dict in question_data:
#     question_text = dict["text"]
#     question_answer = dict["answer"]
#     new_question = Question(text=question_text, answer=question_answer)
#     question_bank.append(new_question)

# for question_data2
question_bank = []
for dict in question_data2 :
    question_text = dict["question"]
    question_answer = dict["correct_answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz.next_question()