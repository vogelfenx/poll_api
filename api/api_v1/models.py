import uuid

from django.db import models


class Poll(models.Model):
    title = models.CharField('Опрос', max_length=100)
    description = models.TextField('Описание', max_length=500)

    # setting auto_now or auto_now_add to True will cause the field to have editable=False
    start_date = models.DateTimeField(
        'Дата старта', auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания')

    def __str__(self):
        return ("%s" % (self.title,))


class Question(models.Model):
    question = models.CharField("Вопрос", max_length=100)
    question_type = models.IntegerField(
        "Тип вопроса", 
        choices=(
            (1, "TEXT"),
            (2, "ONE_CHOICE"),
            (3, "MULTI_CHOICE"), 
        )
    )

    poll_id = models.ForeignKey(Poll, related_name="questions", on_delete=models.CASCADE)
    
    def __str__(self):
        return ("%s" % (self.question,))


class Answer(models.Model):
    answer = models.CharField("Вариант ответа", max_length=100)

    question_id = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    
    def __str__(self):
        return ("%s" % (self.answer,))


class UserAnswer(models.Model):
    answer_id = models.ForeignKey(Answer, related_name="userAnswers", on_delete=models.CASCADE) 
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    answerOnTextQuestion = models.CharField("Ответ пользователя текстом", max_length=100, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['answer_id','user_id'], name="UserAnswerUniq"),
        ]

    # def create(cls, answer_id):
    #     breakpoint()
    #     user_answer = cls(answer_id, user_id)

    # def create(cls, answer_id, user_id):
    #     breakpoint()
    #     user_id = user_id
    #     user_answer = cls(answer_id, user_id)
