from unpacking.unpacking_json import unpacking_file


def main():
    file_json = "question.json"
    questions = unpacking_file(file_json)

    for question in questions:
        print(question.build_question())
        user_answer = input('Ваш ответ: ')
        question.user_response = user_answer
        print(question.build_feedback())

if __name__ == '__main__':
    main()
