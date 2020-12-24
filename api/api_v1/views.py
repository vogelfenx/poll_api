from datetime import date

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.response import Response

from .models import Poll
from .serializers import PollSerializer


class IsAdminOrReadOnly(BasePermission):
    """
    Object-level permission to only allow edit it if the user is admin.
    """

    def has_object_permission(self, request, view, obj):
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
