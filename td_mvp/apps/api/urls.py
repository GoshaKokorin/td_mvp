from django.urls import include, path

urlpatterns = [
    path('feedback/', include('td_mvp.apps.api.feedbacks.urls')),
    path('catalog/', include('td_mvp.apps.api.catalog.urls')),
    path('main/', include('td_mvp.apps.api.main.urls')),
    path('about/', include('td_mvp.apps.api.about.urls')),
]