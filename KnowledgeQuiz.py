
questions = [
    {
        "prompt" : "What is the capital of France?",
        "options" : ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer" : "A"
    },
    {
        "prompt" : "Which Singer sung the song Thriller?",
        "options" : ["A. Michael Jordan","B. Billy Joel","C. Lady Gaga","D. Michael Jackaon"],
        "answer" : "D"
    },
    {
        "prompt" : "What is 120 x 3",
        "options" : ["A. 40", "B. 360", "C. 480", "D. 240"],
        "answer" : "B"
    },
    {
        "prompt" : "Which famous poet wrote about a raven?",
        "options" : ["A. Walliam Shakesphere", "B. Walt Whitman", "C. Edgar Allan Poe", "D. Emily Dickinson"],
        "answer" : "C"

    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option  in question["options"]:
            print(option)
        answer = input("Enter your answer {A, B, C, or D}: ").upper()
        if answer == question["answer"]:
            print("Correct, Hooray!!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct. ")


run_quiz(questions)