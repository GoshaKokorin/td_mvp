from rest_framework import mixins, viewsets

from td_mvp.apps.feedbacks.models import FeedbackCall, FeedbackQuestion
from .serializers import FeedbackCallSerializer, FeedbackQuestionSerializer


class FeedbackCallViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FeedbackCall.objects.none()
    serializer_class = FeedbackCallSerializer


class FeedbackQuestionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FeedbackQuestion.objects.none()
    serializer_class = FeedbackQuestionSerializer
