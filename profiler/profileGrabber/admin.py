from django.contrib import admin
from .models import SavedUser, Tweets


admin.site.register(SavedUser)
admin.site.register(Tweets)