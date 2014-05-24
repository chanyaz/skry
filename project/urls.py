from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import news.views

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # main site
    url(r'^$', news.views.CategoryView.as_view(), name='news_category'),
    url(r'^category/(?P<category>\S+)/$', news.views.CategoryView.as_view(), name='news_category'),

    # api

    url(r'^api/get_article_by_id/$', news.views.ArticleJSONView.as_view()),

    # other apps
    url(r'^prime/', include('prime.urls')),
    url(r'^music/', include('music.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
