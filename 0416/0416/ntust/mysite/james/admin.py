from django.contrib import admin

# Register your models here.

from .models import Name, Birthday, Gender

admin.site.register(Name)
admin.site.register(Birthday)
admin.site.register(Gender)