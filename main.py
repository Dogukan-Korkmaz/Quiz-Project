from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)

print(question_bank[0].text, question_bank[0].answer)