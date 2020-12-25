import uuid
from datetime import date

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, bad_request
from rest_framework.permissions import SAFE_METHODS, AllowAny, BasePermission
from rest_framework.response import Response

from .models import Answer, Poll, Question, UserAnswer
from .serializers import (AnswerSerializer, PollSerializer, QuestionSerializer,
                          UserAnswerSerializer, PollSerializerDetail)


class IsAdminOrReadOnly(BasePermission):
    """
    Object-level permission to only allow edit it if the user is admin.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_staff


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    def list(self, request):
        """
        Return all polls if the request.user is admin, otherwise return only active polls
        """

        today = date.today()

        if request.user.is_staff:
            queryset = Poll.objects.all()
        else:
            # gte = greater than or equal to.
            queryset = Poll.objects.filter(end_date__gte=today)

        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def list_user_polls_detail(self, request):
        user_id = request.session.get("user_id", None)
        # breakpoint()
        if user_id != None:
            user_polls = UserAnswer.objects.filter(user_id=user_id)
            serializer = PollSerializerDetail(user_polls, many=True)
            return Response(serializer.data)
        return Response()

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )


class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes = (AllowAny, )
    
    def perform_create(self, serializer):
        user_id = self.request.session.get("user_id", str(uuid.uuid4()))
        if not UserAnswer.objects.filter(user_id=user_id).exists():
            self.request.session["user_id"] = user_id         
        try:
            serializer.save(user_id=user_id)
        except Exception as exception:
            # custom validationerror
            raise APIException(detail="The user has already voted")

   
        