from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class UserResource(resources.ModelResource):

    class Meta:
        model = get_user_model()



class UserAdmin(ImportExportModelAdmin):
    """Define admin model for User model with no username field."""

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('auth.change_user'):
            del actions['activate_users']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'phone_number',
                'password',
                'is_staff',
                'is_superuser',
                'user_permissions',
                'last_login',
                'date_joined',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    fieldsets = (
        (_('Personal info'), {
            'classes': ('wide', 'extrapretty'),
            'fields': (('full_name', 'nick_name'), ('phone_number', 'gender'), ('rank', 'user_marks'), ('present_address', 'user_experience'), 
            ('password_updated_at', 'last_active_at'))
        }),
        (_('Permissions'), {
            'classes': ('wide', 'collapse'),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide',),
            'fields': ('last_login', 'date_joined')
        }),
    )
    list_display = ('phone_number', 'full_name', 'nick_name', 'is_staff')
    sortable_by = ('phone_number', 'full_name', 'nick_name')
    list_display_links = ('phone_number', 'full_name', 'nick_name')
    list_editable = ('is_staff', )
    search_fields = ('phone_number', 'full_name', 'nick_name')
    ordering = ('date_joined',)
    readonly_fields = ('date_joined', 'last_login', 'password_updated_at', 'last_active_at')
    filter_horizontal = ('groups', 'user_permissions')
    actions = [
        'activate_users',
    ]
    list_filter = ['last_login', 'is_staff', 'is_active', 'is_superuser']
    date_hierarchy = 'last_login'
    save_on_top = True
    save_as = True
    save_as_continue = True

    def activate_users(self, request, queryset):
        assert request.user.has_perm('auth.change_user')
        cnt = queryset.filter(is_active=False).update(is_active=True)
        self.message_user(request, 'Activated {} users.'.format(cnt))

    activate_users.short_description = 'Activate Users'  # type: ignore


admin.site.register(get_user_model(), UserAdmin)
