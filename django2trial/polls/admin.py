from django.contrib import admin

from .models import Question
from .models import Eat
from .models import Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Eat)