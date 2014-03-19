from django.contrib import admin

# Register your models here.
from app1.models import App1, Choice

admin.site.register(App1)
admin.site.register(Choice)