import json

from class_question.question_class import Question


def unpacking_file(file_json):
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
