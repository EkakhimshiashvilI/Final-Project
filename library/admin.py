from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Author, Genre, Book

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    list_display = ('username', 'email', 'full_name', 'is_staff')
    ordering = ('-date_joined',)
    

admin.site.register(User, UserAdminConfig)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
