from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('entries', views.EntryViewSet)

urlpatterns = [
    url(r'^',
        include(router.urls)),
#    url(r'^showurl/(?P<pk>\d+)/$',
#        views.ShowURLView.as_view(),
#        name='showurl'),
]
