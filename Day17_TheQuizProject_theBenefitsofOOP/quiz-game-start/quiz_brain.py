class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        score = 0
        while self.question_number < len(self.question_list):
            # how to call the text: object.attributename
            current_question = self.question_list[self.question_number]
            print_string = f"Q.{self.question_number + 1}: {current_question.text}(True/False)?"
            # ask user input
            user_input = input(print_string)
            # answer object, it is a address in memory
            answer = self.question_list[self.question_number]
            # print(answer.answer)
            self.question_number += 1
            if user_input.lower() == answer.answer.lower():
                score += 1
                print("You are right!")
                # print(f"Current score:{score}/{self.question_number}\n")
            else:
                print("You are wrong.")
            print("The answer is: "+answer.answer)
            print(f"Current score:{score}/{self.question_number}\n")


        print("You've completed the quiz.")
        print(f"Your final score was:{score}/{self.question_number}")






