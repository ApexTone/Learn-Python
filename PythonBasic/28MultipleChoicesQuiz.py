from Question28 import Question

question_prompt = [
    "Color of apples?\n a.red b.green c.blue\n",
    "Color of bananas?\n a.red b.yellow c.blue\n",
    "Color of strawberries?\n a.red b.green c.blue\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a")
]


def run_test(questions):
    score = 0
    for i in questions:
        ans = input(i.prompt)
        if ans == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))


run_test(questions)