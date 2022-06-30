from import_export.admin import ImportExportModelAdmin


class BaseModelAdmin(ImportExportModelAdmin):
    actions = ('set_item_to_published', 'set_item_to_unpublished', 'set_item_to_active', 'set_item_to_unactive')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_active=True)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_list_filter(self, request):
        filters = ['is_published', 'is_active', 'updated_at']
        if not request.user.is_superuser:
            filters.remove('is_active')
        return filters

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            del actions['set_item_to_active']
        return actions

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()

    def set_item_to_published(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, '{} items have been published successfully.'.format(count))

    def set_item_to_unpublished(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, '{} items have been published successfully.'.format(count))

    def set_item_to_active(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, '{} items have been published successfully.'.format(count))

    def set_item_to_unactive(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, '{} items have been published successfully.'.format(count))

    set_item_to_published.short_description = 'Publishing selected items'
    set_item_to_unpublished.short_description = 'Unpublishing selected items'
    set_item_to_active.short_description = 'Activating selected items'
    set_item_to_unactive.short_description = 'Inactive/Delete selected items'
