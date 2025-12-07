from django.contrib import admin
from .models import APIVersion, APIChange, SetupGuide


class APIChangeInline(admin.TabularInline):
    model = APIChange
    extra = 1
    fields = ['change_type', 'app_name', 'endpoint', 'title', 'description']


@admin.register(APIVersion)
class APIVersionAdmin(admin.ModelAdmin):
    list_display = ['version', 'release_date', 'is_active', 'changes_count']
    list_filter = ['is_active', 'release_date']
    search_fields = ['version', 'description']
    readonly_fields = ['created_at']
    inlines = [APIChangeInline]
    
    fieldsets = (
        ('Version Information', {
            'fields': ('version', 'release_date', 'is_active')
        }),
        ('Details', {
            'fields': ('description',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def changes_count(self, obj):
        return obj.changes.count()
    changes_count.short_description = 'Number of Changes'


@admin.register(APIChange)
class APIChangeAdmin(admin.ModelAdmin):
    list_display = ['title', 'change_type', 'app_name', 'version', 'created_at']
    list_filter = ['change_type', 'app_name', 'version']
    search_fields = ['title', 'description', 'endpoint']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Change Information', {
            'fields': ('version', 'change_type', 'app_name', 'endpoint')
        }),
        ('Details', {
            'fields': ('title', 'description')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(SetupGuide)
class SetupGuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'guide_type', 'order', 'is_published', 'updated_at']
    list_filter = ['guide_type', 'is_published']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Guide Information', {
            'fields': ('title', 'guide_type', 'order', 'is_published')
        }),
        ('Content', {
            'fields': ('content',),
            'description': 'You can use Markdown formatting in the content field.'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

