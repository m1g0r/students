"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
# Students urls
	url(r'^$', 'student.views.student_list', name='home'),
	url(r'^students/add/$', 'student.views.student_add', name='students_add'),
	url(r'^students/(?P<sid>\d+)/edit/$', 'student.views.student_edit', name='students_edit'),
	url(r'^students/(?P<sid>\d+)/delete/$', 'student.views.student_delete', name='students_delete'),
# Groups urls
	url(r'^groups/$', 'student.views.groups_list', name='groups'),
	url(r'^groups/add/$', 'student.views.groups_add', name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$', 'student.views.groups_edit', name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$', 'student.views.groups_delete', name='groups_delete'),

# admin
	url(r'^admin/', include(admin.site.urls)),
)