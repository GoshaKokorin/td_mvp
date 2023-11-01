from rest_framework import mixins, viewsets, permissions
from rest_framework.response import Response

from td_mvp.apps.api.catalog.serializers import CategoryListSerializer
from td_mvp.apps.catalog.models import Category
from td_mvp.apps.main.models import Main
from .serializers import MainListSerializer


class MainViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Main.objects.filter(is_active=True)
    serializer_class = MainListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        main_response = super().list(request, *args, **kwargs)

        category_serializer = CategoryListSerializer(Category.objects.all(), many=True, context={'request': request})
        return Response({
            'slider': main_response.data,
            'category': category_serializer.data
        })
