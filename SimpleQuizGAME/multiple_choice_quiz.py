from questions import Questions
# created the entire quiz
all_questions = [
    'What color are strawberries?\na) Red\nb) Yellow\nc) Green\n>>',
    'What color are bananas?\na) Teal\nb) Magenta\nc) Yellow\n>>',
    'What color are apples?\na) Blue\nb) Red\nc) Pink\n>>'
]

# arranged an array
question_answer = [
    Questions(all_questions[0], 'a'),
    Questions(all_questions[1], 'c'),
    Questions(all_questions[2], 'b')
]


def quiz(questions: list):
    """
    Run the quiz GAME
    It takes an array using classes to store 'prompt and answer'
    :param questions:  each single element of the array is a class
    :return: score (correct answers out of the questions) checked between the user input and the class.answer
    """
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'You got {score}/{len(questions)} correct')


quiz(question_answer)
