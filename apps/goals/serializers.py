from rest_framework import serializers
from .models import Goal, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'title', 'is_done']


class GoalSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    progress = serializers.IntegerField(read_only=True)

    class Meta:
        model = Goal
        fields = ['id', 'title', 'description', 'status', 'user', 'steps', 'progress']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
