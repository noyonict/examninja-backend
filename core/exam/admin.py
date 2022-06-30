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
    # actions = ('set_item_to_published', 'set_item_to_unpublished', 'set_item_to_active', 'set_item_to_unactive')
    # preserve_filters = True
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


class SubjectCategoryResource(resources.ModelResource):

    class Meta:
        model = SubjectCategory


class SubjectCategoryModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'exam_title', 'is_published']
    sortable_by = ('name', 'exam_title')
    list_display_links = ['name', 'exam_title']
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
    search_fields = ('name', 'exam_title')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Topic Info: (Ex: SSC/HSC/Admission)'), {
            'classes': ('wide', 'extrapretty'),
            'fields': (('name', 'exam_title'))
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = SubjectCategory

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


admin.site.register(SubjectCategory, SubjectCategoryModelAdmin)


class SubjectResource(resources.ModelResource):
    
    class Meta:
        model = Subject


class SubjectModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'code', 'subject_category', 'is_published']
    sortable_by = ('name', 'code', 'subject_category')
    list_display_links = ['name', 'code', 'subject_category']
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
    search_fields = ('name', 'code', 'subject_category')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Topic Info: (Ex: SSC/HSC/Admission)'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', ('code', 'subject_category'))
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = Subject

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


admin.site.register(Subject, SubjectModelAdmin)

class ChapterCategoryResource(resources.ModelResource):
    
    class Meta:
        model = ChapterCategory


class ChapterCategoryModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'number_of_question', 'subject', 'is_published']
    sortable_by = ('name', 'number_of_question', 'subject')
    list_display_links = ['name', 'number_of_question', 'subject']
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
    search_fields = ('name', 'number_of_question', 'subject')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Chapter Category Info:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'number_of_question', 'subject')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = ChapterCategory

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



admin.site.register(ChapterCategory, ChapterCategoryModelAdmin)


class ChapterResource(resources.ModelResource):
    
    class Meta:
        model = Chapter


class ChapterModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'chapter_position', 'chapter_category', 'is_published']
    sortable_by = ('name', 'chapter_position', 'chapter_category')
    list_display_links = ['name', 'chapter_position', 'chapter_category']
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
    search_fields = ('name', 'chapter_position', 'chapter_category')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Chapter Info:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', 'chapter_position', 'chapter_category')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = Chapter

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



admin.site.register(Chapter, ChapterModelAdmin)

class BoardYearResource(resources.ModelResource):
    
    class Meta:
        model = BoardYear


class BoardYearModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['board_name', 'year', 'code', 'is_published']
    sortable_by = ('board_name', 'year', 'code')
    list_display_links = ['board_name', 'year', 'code']
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
    search_fields = ('board_name', 'year', 'code')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Board Info:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': (('board_name', 'year'), 'code')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = BoardYear

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


admin.site.register(BoardYear, BoardYearModelAdmin)

class QuestionResource(resources.ModelResource):
    
    class Meta:
        model = Question


class QuestionModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['chapter', 'question', 'is_published']
    sortable_by = ('chapter', 'question',)
    list_display_links = ['chapter', 'question',]
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
    search_fields = ('chapter', 'question', 'uddipok', 'hints')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Question Info:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('chapter', 'question', 'uddipok', 'hints', 'image', 'boards')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = Question

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



admin.site.register(Question, QuestionModelAdmin)


class QuestionCommentResource(resources.ModelResource):
    
    class Meta:
        model = QuestionComment


class QuestionCommentModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['question', 'comment', 'user', 'is_published']
    sortable_by = ('question', 'user')
    list_display_links = ['question', 'comment', 'user']
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
    search_fields = ('question', 'comment', 'user')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Question Commnet:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('question', 'comment', 'user')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = QuestionComment

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



admin.site.register(QuestionComment, QuestionCommentModelAdmin)

class AnswerResource(resources.ModelResource):
    
    class Meta:
        model = Answer


class AnswerModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['value', 'is_published']
    # sortable_by = ('value')
    list_display_links = ['value']
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
    search_fields = ('value', )
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Answer:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('value', )
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = Answer

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



admin.site.register(Answer, AnswerModelAdmin)


class QuestionAnswerResource(resources.ModelResource):
    
    class Meta:
        model = QuestionAnswer


class QuestionAnswerModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['question', 'answer', 'is_published']
    sortable_by = ('question', 'answer')
    list_display_links = ['question', 'answer']
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
    search_fields = ('question', 'answer')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Question Answer:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('question', 'answer')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = QuestionAnswer

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



admin.site.register(QuestionAnswer, QuestionAnswerModelAdmin)

class QuestionPatternResource(resources.ModelResource):
    
    class Meta:
        model = QuestionPattern


class QuestionPatternModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'chapter', 'number_of_questions', 'is_published']
    sortable_by = ('name', 'chapter')
    list_display_links = ['name', 'chapter', 'number_of_questions']
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
    search_fields = ('name', 'chapter')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Question Pattern Info:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', ('chapter', 'number_of_questions'))
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = QuestionPattern

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



admin.site.register(QuestionPattern, QuestionPatternModelAdmin)

class ExamResource(resources.ModelResource):
    
    class Meta:
        model = Exam


class ExamModelAdmin(BaseModelAdmin):
    # form = TopicAdminForm
    list_display = ['name', 'subject', 'exam_title', 'is_published']
    sortable_by = ('name', 'subject', 'exam_title',)
    list_display_links = ['name', 'subject', 'exam_title']
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
    search_fields = ('name', 'subject', 'exam_title')
    readonly_fields = ('created_at', 'created_by', 'updated_at', 'updated_by')
    # exclude = ('created_at', 'created_by', 'updated_at', 'updated_by')
    fieldsets = (
        (_('Exam Info:'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ('name', ('exam_title', 'subject'), ('number_of_questions', 'exam_cost'), 'exam_procedure')
        }),
        (_('Important dates'), {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': (('sequence', 'is_published'), ('created_by', 'created_at'), ('updated_by', 'updated_at'))
        }),
    )

    class Meta:
        model = Exam

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



admin.site.register(Exam, ExamModelAdmin)
