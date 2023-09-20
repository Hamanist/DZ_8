class Question:
    def __init__(self, question_text: str, complexity: int, correct_answer):
        self.question_text = question_text
        self.complexity = complexity  # сложность
        self.correct_answer = correct_answer
        self.question_asked = False  # задан ли вопрос
        self.user_response = None  # ответ пользователя
        self.points_question = self.complexity * 10  # баллы за вопрос

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.points_question)

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        if self.correct_answer == self.user_response:
            return True
        return False

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.question_text}\nСложность {self.complexity}/5"

    def build_positive_feedback(self):
        """Возвращает:
        Ответ верный, получено __ баллов
        """
        if self.correct_answer == self.user_response:
            return f"Ответ верный, получено {self.points_question} баллов"
        return f"Ответ неверный, верный ответ {self.correct_answer}"

    # def build_negative_feedback(self): ...
    #
    # """Возвращает :
    # Ответ неверный, верный ответ __
    # """

    # *Вы также можете совместить последние два метода
