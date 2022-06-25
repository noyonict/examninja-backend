from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from exam.models import *


class ExamTitleResource(resources.ModelResource):

    class Meta:
        model = ExamTitle


class ExamTitleModelAdmin(ImportExportModelAdmin):
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
    actions = ('set_item_to_published', 'set_item_to_unpublished',
               'set_item_to_active', 'set_item_to_unactive')
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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_active=True)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     print(db_field.name, kwargs)
    #     if db_field.name == "subject":
    #         kwargs["queryset"] = Subject.objects.filter(is_active=True)
    #         print(db_field, request)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_list_filter(self, request):
        filters = ['is_published', 'is_active', 'updated_at']
        if not request.user.is_superuser:
            filters.remove('is_active')
        return filters

    # def get_exclude(self, request):
    #     excludes = super().get_exclude(request)
    #     if not request.user.is_superuser:
    #         excludes.remove('is_active')
    #     return excludes

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     # if request.user.has_perm('exam.delete_exam_title'):
    #     #     del actions['set_item_to_active']
    #     return actions

    # def get_list_display(self, request):
    #     actions = super().get_list_display(request)
    #     if not request.user.has_perm('exam.change_topic'):
    #         del actions['published_questions']
    #         del actions['unpublished_questions']
    #     return actions

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()

    def set_item_to_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, '{} items have been published successfully.'.format(count))

    def set_item_to_unpublished(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(
            request, '{} items have been published successfully.'.format(count))

    def set_item_to_active(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(
            request, '{} items have been published successfully.'.format(count))

    def set_item_to_unactive(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(
            request, '{} items have been published successfully.'.format(count))

    set_item_to_published.short_description = 'Publishing selected items'
    set_item_to_unpublished.short_description = 'Unpublishing selected items'
    set_item_to_active.short_description = 'Activating selected items'
    set_item_to_unactive.short_description = 'Inactive/Delete selected items'


admin.site.register(ExamTitle, ExamTitleModelAdmin)
admin.site.register(SubjectCategory)
admin.site.register(Subject)
admin.site.register(ChapterCategory)
admin.site.register(Chapter)
admin.site.register(BoardYear)
admin.site.register(Question)
admin.site.register(QuestionComment)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(QuestionPattern)
admin.site.register(Exam)
