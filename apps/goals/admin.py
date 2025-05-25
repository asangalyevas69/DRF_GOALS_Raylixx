from django.contrib import admin
from .models import Goal, Step


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'progress_display')
    list_filter = ('status', 'user')
    search_fields = ('title', 'description')

    def progress_display(self, obj):
        return f'{obj.progress}%'

    progress_display.short_description = 'Progress'


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'goal', 'is_done')
    list_filter = ('is_done',)
    search_fields = ('title',)
