# -*- coding: utf-8 -*-

"""
Main URL mapping configuration file.

Include other URLConfs from external apps using method `include()`.

It is also a good practice to keep a single URL to the root index page.

This examples uses Django's default media
files serving technique in development.
"""

from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

# App routers
from partners.urls import partner_router
from finance.urls import finance_router
from billing.urls import billing_router

admin.autodiscover()


URL_VERSION = r'^(?P<version>v[1])'

public_apis = [

    # # django-admin:
    # re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # re_path(r'^admin/', admin.site.urls),

    # # Apps:
    # re_path(r'^main/', include(main_urls)),

    # Text and xml static files:
    re_path(r'^robots\.txt$', TemplateView.as_view(
        template_name='txt/robots.txt',
        content_type='text/plain',
    )),
    re_path(r'^humans\.txt$', TemplateView.as_view(
        template_name='txt/humans.txt',
        content_type='text/plain',
    )),

    # # It is a good practice to have explicit index view:
    # re_path(r'^$', index, name='index'),

    # Partners
    re_path(f'{URL_VERSION}/partners/', include(partner_router.urls)),

    # Finance
    re_path(f'{URL_VERSION}/finance/', include(finance_router.urls)),

    # Billing
    re_path(f'{URL_VERSION}/billing/', include(billing_router.urls)),

]


urlpatterns = public_apis + [

    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        re_path(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        re_path(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        re_path(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            re_path(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
