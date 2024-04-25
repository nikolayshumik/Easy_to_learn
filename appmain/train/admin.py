from django.contrib import admin
from .models import Topic_to_learn
from .models import Tests_to_do
# Register your models here.

admin.site.register(Topic_to_learn)
admin.site.register(Tests_to_do)