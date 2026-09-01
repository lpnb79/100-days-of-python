from question_model import Question
from data import question_data
from quiz_brain import Quiz


question_bank = []
#print(question_data[0]["text"])
#print(question_data[0]["answer"])

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_q = Question(text=question_text, answer=question_answer)
    question_bank.append(new_q)

quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

final_score = quiz.score

print(f"You've completed the quiz.\nFinal score: {final_score}/{len(question_bank)}.\n")




#class example
#attributes = things it has
#methods = things it does

#class User:
#
#    def __init__(self, user_id, username):
#        self.id = user_id 
#        self.username = username
#        self.followers = 0
#        self.following = 0
#        print("new user being created")
#
#    #method
#    def follow(self, user):
#        user.followers += 1
#        self.following += 1
#
#
#user_1 = User("001", "name")
##user_1.id = "001"
##user_1.username = "name"
#print(user_1.username)
#print(user_1.followers)
#
#
#
#user_2 = User("002", "jack")
##user_2.id = "002"
##user_2.username = "name2"
##print(user_2.username)
#
#user_1.follow(user_2)
#print(user_1.followers)
#print(user_1.following)
#
#print(user_2.followers)
#print(user_2.following)