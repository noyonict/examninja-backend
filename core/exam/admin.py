from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from utils.base_admin import BaseModelAdmin
from import_export import resources
from exam.models import *


class ExamTitleResource(resources.ModelResource):

    class Meta:
        model = ExamTitle


class ExamTitleModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'expansion_of_name', 'is_published']
    sortable_by = ('name', 'expansion_of_name')
    list_display_links = ['name', 'expansion_of_name']
    list_editable = ['is_published', ]
    # list_filter = ['is_published', 'is_active', 'updated_at']
    list_per_page = 20
    # list_max_show_all = 200
    # date_hierarchy = 'created_at'
    # save_as = False
    # save_as_continue = False
    show_full_result_count = True
    # save_on_top = True
    # save_as = True
    # save_as_continue = True
    # actions_on_bottom = True
    # actions_selection_counter = True
    # empty_value_display = '???'
    # filter_vertical = True
    # paginator = Paginator
    # raw_id_fields = ('subject', 'chapter')
    # autocomplete_fields = ()
    preserve_filters = True
    search_fields = ('name', 'expansion_of_name')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Topic Info: (Ex: SSC/HSC/Admission)'), {
            'classes': ('wide', 'extrapretty'),
            'fields': (('name', 'expansion_of_name'))
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = ExamTitle

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     print(db_field.name, kwargs)
    #     if db_field.name == "subject":
    #         kwargs["queryset"] = Subject.objects.filter(is_active=True)
    #         print(db_field, request)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_exclude(self, request):
    #     excludes = super().get_exclude(request)
    #     if not request.user.is_superuser:
    #         excludes.remove('is_active')
    #     return excludes

    # def get_list_display(self, request):
    #     actions = super().get_list_display(request)
    #     if not request.user.has_perm('exam.change_topic'):
    #         del actions['published_questions']
    #         del actions['unpublished_questions']
    #     return actions


admin.site.register(ExamTitle, ExamTitleModelAdmin)
admin.site.register(SubjectCategory)
admin.site.register(Subject)
admin.site.register(ChapterCategory)
admin.site.register(Chapter)
admin.site.register(BoardYear)
