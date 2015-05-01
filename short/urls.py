from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.HomePageView.as_view(),
        name='home'),
    url(r'^showurl/(?P<slug>\w+)/$',
        views.ShowURLView.as_view(),
        name='showurl'),
    url(r'^r/(?P<slug>\w+)/$',
        views.RedirectToURLView.as_view(),
        name='redirecttourl'),
]
