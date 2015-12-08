# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def journal_list(request):
		journal = (
			{'id': 1,
			'first_name': u'Андрій',
			'last_name': u'Корост'},
			
			{'id': 2,
			'first_name': u'Дмитро',
			'last_name': u'Колобов'},

			{'id': 3,
			'first_name': u'Роман',
			'last_name': u'Іваненко'}
			)

		return render(request, 'students/visits_list.html', {'journal': journal})