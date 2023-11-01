from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, permissions, generics
from rest_framework.response import Response

from td_mvp.apps.api.pagination import PageNumberPagination
from td_mvp.apps.catalog.models import Category, Product
from .serializers import CategoryListSerializer, ProductListSerializer, ProductDetailSerializer


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductViewSet(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductDetailSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        self.get_serializer(request)
        return super().retrieve(request, *args, **kwargs)


class CatalogProductAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]

    def get(self, request, *args, **kwargs):
        product_response = self.list(request, *args, **kwargs)
        return Response({
            "products": product_response.data,
        })

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=slug).filter(is_active=True)
