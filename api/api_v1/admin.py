from django.contrib import admin

from .models import Poll, Question, Answer, UserAnswer

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserAnswer)
