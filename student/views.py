# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def student_list(request):
		students = (
			{'id': 1,
			'first_name': u'Андрій',
			'last_name': u'Корост',
			'ticket': 2123,
			'image': 'img/1.jpg'},
			
			{'id': 2,
			'first_name': u'Дмитро',
			'last_name': u'Колобов',
			'ticket': 2175,
			'image': 'img/2.jpg'},

			{'id': 3,
			'first_name': u'Роман',
			'last_name': u'Іваненко',
			'ticket': 2176,
			'image': 'img/3.jpg'}
			)

		return render(request, 'students/students_list.html', {'students': students})

def student_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def student_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def student_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)


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
