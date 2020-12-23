from datetime import date

from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.response import Response

from .models import Pool
from .serializers import PoolSerializer


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


class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAdminOrReadOnly, )

    def list(self, request):
        """
        Return all pools if the request.user is admin, otherwise return only active pools
        """

        today = date.today()

        if request.user.is_staff:
            queryset = Pool.objects.all()
        else:
            # gte = greater than or equal to.
            queryset = Pool.objects.filter(end_date__gte=today)

        serializer = PoolSerializer(queryset, many=True)
        return Response(serializer.data)
