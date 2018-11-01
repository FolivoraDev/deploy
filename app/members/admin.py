from django.contrib import admin

# Register your models here.
from members import models

admin.site.register(models.User)