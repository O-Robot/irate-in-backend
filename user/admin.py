from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'lastname', 'firstname']
    search_fields = ('id', 'email', 'lastname', 'firstname')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
            'fields': ('lastname', 'firstname')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important Info'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'lastname', 'firstname', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
