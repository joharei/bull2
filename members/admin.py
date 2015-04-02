from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from members.models import Member, Group as BullGroup


class MemberChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Member


class MemberCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Member


class MemberAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personlig info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'birth_date')}),
        ('Datoer', {'fields': ('last_login',)}),
    )
    form = MemberChangeForm
    add_form = MemberCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    list_filter = ('is_admin', 'groups')
    filter_horizontal = ()


admin.site.register(Member, MemberAdmin)
admin.site.register(BullGroup)
admin.site.unregister(Group)

