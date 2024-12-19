def quiz():
     questions = {
        "What is the fastest land animal?": "cheetah",
        "Which animal is known as the king of the jungle?": "lion",
        "What animal has a long trunk?": "elephant"
    }
     score =0
     for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
            print("--------------------------------------------------")
        else:
            print("Incorrect!")
            print("--------------------------------------------------")
quiz()