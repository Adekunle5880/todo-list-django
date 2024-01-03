from django.contrib import admin

from .models import TodoItem

# Register your models here.
# to allow us modify db and use them

admin.site.register(TodoItem)
