from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ticket.models import *
from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.db import connection
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os

from datetime import datetime
from django.contrib.auth import authenticate


@csrf_exempt
def ingresar(request):


	if request.method == 'POST':

		dato = request.GET

		return HttpResponse(simplejson.dumps('Usuario Incorrecto'))

		

		username = dato['username']

		password = dato['password']

		user = authenticate(username=username, password=password)


		if user is not None:

			if user.is_active:

				login(request, user)

				return HttpResponse(simplejson.dumps('Activado')) 

			else:

				return HttpResponse(simplejson.dumps('Desactivado')) 
		else:

			return HttpResponse(simplejson.dumps('Usuario Incorrecto'))


