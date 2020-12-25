from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User as auth_User

from .models import Poll, Question, Answer, UserAnswer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('__all__')
        # read_only_fields = ['start_date']

class PollSerializerDetail(serializers.ModelSerializer):

    poll = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    user_answer = serializers.SerializerMethodField()
    # answerOnTextQuestion = serializers.SerializerMethodField()
    
    def get_poll(self, obj):
        # breakpoint()
        self.poll = obj.answer_id.question_id.poll_id.title
        return str(self.poll)

    def get_question(self, obj):
        # breakpoint()
        self.question = obj.answer_id.question_id.question
        return str(self.question)

    def get_user_answer(self, obj):
        # breakpoint()
        self.answer = obj.answer_id.answer
        return str(self.answer)     

    # def get_answerOnTextQuestion(self, obj):
    #     # question_type 1 = Text question type
    #     if obj.answer_id.question_id.question_type == 1:
    #         return obj.answerOnTextQuestion
    #     else:
    #         return False

    class Meta:
        model = UserAnswer
        fields = ("user_id", "poll", "question", "user_answer", "answerOnTextQuestion")
        # read_only_fields = ['start_date']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('__all__')


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('__all__')
