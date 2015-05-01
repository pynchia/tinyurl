from django.conf.urls import include, url
from django.contrib import admin
import short

urlpatterns = [
    # Examples:
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'', include('short.urls', 
                     namespace='short',
                     app_name='short')),
    url(r'^admin/', include(admin.site.urls)),
]
