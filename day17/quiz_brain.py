#ask question
#check correct
#check end of quiz


class Quiz:

    #attributes
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    #methods
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        #if self.question_number < len(self.question_list):
        #    return True
        #else:
        #    return False
        return self.question_number < len(self.question_list)
        """
        the less than operator evaluates to see if the statement is True
        so on first while loop, q_number = 0 which is < len(list) which evaluates True
        it will evaluate false once the numbers are equal which will end the list
        much less code than if/else statement
        """

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"\nYou got it right.")
            self.score += 1
        else:
            print(f"\nWrong.")
            
        print(f"Current score {self.score}/{self.question_number}")
        print(f"Correct answer is: {correct_answer}\n")