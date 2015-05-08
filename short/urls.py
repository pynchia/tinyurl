from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.HomePageView.as_view(),
        name='home'),
    url(r'^searchurl/$',
        views.SearchURLView.as_view(),
        name='searchurl'),
    url(r'^showurl/(?P<pk>\d+)/$',
        views.ShowURLView.as_view(),
        name='showurl'),
    url(r'^r/(?P<pk>\d+)/$',
        views.RedirectToURLView.as_view(),
        name='redirecttourl'),
]
