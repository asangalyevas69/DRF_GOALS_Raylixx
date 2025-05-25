import django_filters
from .models import Goal


class GoalFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    min_progress = django_filters.NumberFilter(method='filter_min_progress')
    max_progress = django_filters.NumberFilter(method='filter_max_progress')

    class Meta:
        model = Goal
        fields = ['status']

    def filter_min_progress(self, queryset, name, value):
        return [g for g in queryset if g.progress >= value]

    def filter_max_progress(self, queryset, name, value):
        return [g for g in queryset if g.progress <= value]
