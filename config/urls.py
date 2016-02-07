# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^manage/', include(admin.site.urls)),
    url(r'^f/', include('fwdform.urls', namespace='fwdform')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

