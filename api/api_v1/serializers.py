from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User as auth_User

from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('__all__')
        # read_only_fields = ['start_date']
