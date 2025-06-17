from question_model import Question
from data import question_data
from quiz_brain import quizbrain


question_bank = []
   
for question in question_data:
        text = question["text"]
        answer = question["answer"]
        new_question = Question(text, answer)
        question_bank.append(new_question)
 
quiz= quizbrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
