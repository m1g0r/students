# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups

def groups_list(request):
		groups = (
			{'id': 1,
			'groups_name': u'MTM21',
			'starosta_name': u'Колобов Дмитро'},

			{'id': 2,
			'groups_name': u'MTM22',
			'starosta_name': u'Корост Андрій'},

			{'id': 3,
			'groups_name': u'MTM23',
			'starosta_name': u'Іваненко Роман'},
			)

		return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)

