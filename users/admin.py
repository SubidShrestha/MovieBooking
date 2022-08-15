from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = user
    list_display = ('email','first_name','last_name','is_staff', 'is_active','is_superuser',)
    list_filter = ('email','first_name','last_name', 'is_staff', 'is_active','is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','first_name','last_name','is_superuser',)}
        ),
    )
    search_fields = ('email','first_name','last_name',)
    ordering = ('email','first_name','last_name',)


admin.site.register(user, CustomUserAdmin)