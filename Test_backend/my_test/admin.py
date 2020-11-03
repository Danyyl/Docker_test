from django.contrib import admin

from my_test import models
admin.site.register(models.Company)
admin.site.register(models.Department)
admin.site.register(models.Status)
admin.site.register(models.Employees)