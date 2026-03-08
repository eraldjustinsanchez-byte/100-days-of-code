questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What language is used for web browsers?", "answer": "javascript"},
    {"question": "What does CPU stand for?", "answer": "central processing unit"}
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ").lower()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Finished!")
print("Your score:", score, "/", len(questions))