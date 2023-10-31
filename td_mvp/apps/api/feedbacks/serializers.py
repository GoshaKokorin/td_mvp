from rest_framework import serializers

from td_mvp.apps.feedbacks.models import FeedbackCall, FeedbackQuestion


class FeedbackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackCall
        fields = ['name', 'number', 'email']


class FeedbackQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackQuestion
        fields = ['name', 'number', 'email', 'text']
