# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:50:26 2018

@author: LBS
"""

# from django.conf.urls import include, url
# from django.contrib import admin

# admin.autodiscover()
# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]

from django.conf.urls import url, include
from django.contrib import admin
from polls import views

urlpatterns = [
    url(r'^$', views.index,name='index'),  # new
    #url(r'^polls/',include('polls.urls'))
    url(r'^admin/', include(admin.site.urls)),
]