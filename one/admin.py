from django.contrib import admin
from one.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','email','Address')
    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price')

admin.site.register(Student,StudentAdmin)
admin.site.register(Product,ProductAdmin)