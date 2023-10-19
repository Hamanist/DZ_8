import json

from class_question.question_class import Question


def unpacking_file(file_json):
    """

    :param file_json: принимает json файл для его чтения
    :return: возвращает список экземпляра класса полученный из json файла
    """
    with open(file_json, "r", encoding="utf-8") as f:
        file = json.load(f)
    questions = []
    for item in file:
        question_text = item["q"]
        complexity = item["d"]
        correct_answer = item["a"]
        question = Question(question_text, complexity, correct_answer)
        questions.append(question)

    return questions


def statistic(questions):
    """

    :param questions: принимает данные json файла
    :return: выводит статистику с правильными ответами и набранными баллами
    """
    balls = 0
    answers_on_questions = 0
    total_questions = 0
    for question in questions:
        total_questions += 1
        if question.is_correct():
            answers_on_questions += 1
            balls += question.get_points()

    print(f'\nВот и всё!\nОтвечено {answers_on_questions} вопроса из {total_questions}\nНабрано баллов: {balls}')
