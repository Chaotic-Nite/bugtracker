from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from bug_user_app.models import CustomUser
from django.utils.translation import ugettext_lazy as _

# Based on Stack Overflow user nip3o's solution and neverwalkaloner's comment

class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        moedl = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomChangeForm

    fieldsets = ((None, {'fields': ('username', 'password')}), 
    (_('Personal info'), 
    {'fields': ('displayname', 'first_name', 'last_name', 'email')}), 
    (_('Permissions'), 
    {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    (_('Important dates'), {'fields': ('last_login',)}))

admin.site.register(CustomUser, CustomUserAdmin)