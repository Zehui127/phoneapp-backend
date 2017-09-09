from django.conf.urls import url
from django.contrib import admin
from django.contrib import auth
from rest_framework.urlpatterns import format_suffix_patterns
from activity import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework.authtoken import views as rest_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^activity/$', views.ArticleList.as_view()),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^thumbs/$', views.ArticleThumbnails.as_view()),
    url(r'^login/$', views.UserInformation.as_view()),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', rest_view.obtain_auth_token),                           
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)




urlpatterns = format_suffix_patterns(urlpatterns)
