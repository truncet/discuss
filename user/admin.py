from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import CharField, Textarea, TextInput

from .models import NewUser

# Register your models here.


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('user_email', 'user_name')
    list_filter = ('user_email', 'user_name', 'is_active', 'is_staff')
    ordering = ('-joined_date',)
    list_display = ('user_email', 'user_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('user_email', 'user_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about', 'joined_date')})
    )

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('user_email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


admin.site.register(NewUser, UserAdminConfig)
