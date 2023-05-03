from django.shortcuts import render
from account.models import Account

# Create your views here.

def home_screen_views(request):

	context = {}
	# context['some_string'] = 'This is some string of context variable'

	# list_of_values = []
	# list_of_values.append("first entry")
	# # list_of_values.append("second entry")
	# # list_of_values.append("third entry")
	# # context['list_of_values'] = list_of_values

	# questions = Question.objects.all()
	# context["questions"] = questions

	accounts = Account.objects.all()
	context["accounts"] = accounts

	return render(request, "personal/home.html", context)