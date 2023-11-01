from rest_framework import permissions, mixins, viewsets
from rest_framework.response import Response

from td_mvp.apps.about.models import About, Geo
from .serializers import AboutSerializer, GeoSerializer


class AboutViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        main_response = super().list(request, *args, **kwargs)

        geo_serializer = GeoSerializer(Geo.objects.first())
        return Response({
            'requisites': main_response.data,
            'geo': geo_serializer.data
        })
