from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csptest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^jinja$', 'csptest.jinja_example.views.jinja_view', name='jinja_view'),
    url(r'^django$', 'csptest.django_example.views.django_view', name='django_view'),
    url(r'^admin/', include(admin.site.urls)),
)
