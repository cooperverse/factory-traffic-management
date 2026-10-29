from django.contrib import admin
from .models import SignalState, Junction
# Register your models here.
admin.site.register(Junction)
admin.site.register(SignalState)
