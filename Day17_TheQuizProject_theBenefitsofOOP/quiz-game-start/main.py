from question_model import Question
from data import question_data
import quiz_brain_lec

# import data to the question_model
question_bank = []
for dict in question_data:
    question_text = dict["text"]
    question_answer = dict["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = quiz_brain_lec.QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")