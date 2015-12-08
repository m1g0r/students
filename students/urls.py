from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin

from student.views.views_students import *
from student.views.views_groups import *
from student.views.views_journal import *

urlpatterns = patterns('',

# Students urls
    url(r'^$', student_list, name='home'),
	url(r'^students/add/$', student_add, name='students_add'),
	url(r'^students/(?P<sid>\d+)/edit/$', student_edit, name='students_edit'),
	url(r'^students/(?P<sid>\d+)/delete/$', student_delete, name='students_delete'),

# Groups urls
	url(r'^groups/$', groups_list, name='groups'),
	url(r'^groups/add/$', groups_add, name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$', groups_edit, name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$', groups_delete, name='groups_delete'),

# Groups urls
	url(r'^journal/$', journal_list, name='journal'),
                      
# admin
	url(r'^admin/', include(admin.site.urls)),
)